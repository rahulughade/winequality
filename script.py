#importing libraries
import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request

#creating instance of the class
app=Flask(__name__)

#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

#prediction function for red wine
def Red_ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,6)
    loaded_model = pickle.load(open("model/tuned_redmodel.pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]
    

#prediction function for white wine
def White_ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,5)
    loaded_model = pickle.load(open("model/tuned_whitemodel.pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]
    
#Create route to display prediction for red wine
@app.route('/result_red',methods = ['POST'])
def result_red():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result = Red_ValuePredictor(to_predict_list)
        print(to_predict_list)
        
        if int(result)==0:
            prediction='Poor Wine'
        elif int(result)==1:
            prediction='Average Wine'
        else:
            prediction='Great Wine'
            
        return render_template("result_red.html",prediction_red=prediction)

#Create route to display prediction for white wine
@app.route('/result_white',methods = ['POST'])
def result_white():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result = White_ValuePredictor(to_predict_list)
        
        if int(result)==0:
            prediction='Poor Wine'
        elif int(result)==1:
            prediction='Average Wine'
        else:
            prediction='Great Wine'
            
        return render_template("result_white.html",prediction_white=prediction)