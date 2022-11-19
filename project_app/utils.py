
import os
import pickle
import json
import config
import numpy as np


class IrisModel():
    def __init__(self,sepallengthCm,sepalwidthCm,petallengthCm,petalwidthCm):
        self.sepallengthCm=sepallengthCm
        self.sepalwidthCm=sepalwidthCm
        self.petallengthCm=petallengthCm
        self.petalwidthCm=petalwidthCm

    def load_model(self):
        with open (config.model_path,'rb') as f:
            self.lg_model=pickle.load(f)
        
        with open(config.json_path,'r') as f:
            self.json_data = json.load(f)

    def get_predicted_class(self):
        self.load_model()

        test_array=np.zeros(len(self.json_data['columns']))

        test_array[0]=self.sepallengthCm
        test_array[1]=self.sepalwidthCm
        test_array[2]=self.petallengthCm
        test_array[3]=self.petalwidthCm

        print("Test array:",test_array) 
        predicted_class = self.lg_model.predict([test_array])
        return predicted_class