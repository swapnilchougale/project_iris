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
def Iris_Model():
    sepallengthCm=6.6
    sepalwidthCm=3.0
    petallengthCm=4.4
    petalwidthCm=1.4
    
    i_class = IrisModel(sepallengthCm,sepalwidthCm,petallengthCm,petalwidthCm)
    result = i_class.get_predicted_class()

    return jsonify ({"Result": f"Predicted iris class is:{result}"})
    # return render_template("home.html")


if __name__=="__main__":
    app.run(debug=True)
    
    