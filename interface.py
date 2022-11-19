from flask import Flask ,render_template ,jsonify,request,redirect,url_for

import config
from project_app.utils import IrisModel

app  = Flask(__name__)
###########################################################################################
############################### Base API ##################################################
###########################################################################################
@app.route("/") 
def hello_flask():
    print("Welcome to flask")
    return "Welcome to flask"

###########################################################################################
############################### Project API ##################################################
###########################################################################################

@app.route("/predict_class")
def IrisModel():
    sepallengthCm=6.7
    sepalwidthCm=3.5
    petallengthCm=5.3
    petalwidthCm=3
    
    i_class = IrisModel(sepallengthCm,sepalwidthCm,petallengthCm,petalwidthCm)
    classs = i_class.get_predicted_class()

    return jsonify ({"Result": f"Predicted iris class is:{classs}"})


if __name__=="__main__":
    app.run()