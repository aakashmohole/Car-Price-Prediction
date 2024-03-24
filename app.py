from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))

@app.route('/', methods = ['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    fule_type_diesel = 0
    if request.method == 'POST':
        year = int(request.form['Year'])
        present_price=float(request.form['Present_Price'])
        kms_driven=int(request.form['Kms_Driven'])
        Kms_driven2=np.log(kms_driven)
        owner=int(request.form['Owner'])
        fuel_type_petrol=request.form['Fuel_Type_Petrol']
        if(fuel_type_petrol=='Petrol'):
                fuel_type_petrol=1
                fule_type_diesel=0
        else:
            fuel_type_petrol=0
            fule_type_diesel=1
            
        year=2024-year
        seller_type_individual=request.form['Seller_Type_Individual']
        if(seller_type_individual=='Individual'):
            seller_type_individual=1
        else:
            seller_type_individual=0	
        transmission_mannual=request.form['Transmission_Mannual']
        if(transmission_mannual=='Mannual'):
            transmission_mannual=1
        else:
            transmission_mannual=0
        prediction=model.predict([[present_price,Kms_driven2,owner,year,fule_type_diesel,fuel_type_petrol,seller_type_individual,transmission_mannual]])
        
        result = round(prediction[0],2)
        
        if result<0:
            return render_template('index.html',prediction_texts="Sorry to inform you that you cannot sell this car")
        else:
            return render_template('index.html',prediction_text=" Congo! You Can Sell The Car at {}".format(result))
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

