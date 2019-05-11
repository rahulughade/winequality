import os
import io
import pandas as pd
import numpy as np
import pickle

from sklearn.linear_model import LogisticRegression

from flask import Flask, request, redirect, url_for, jsonify



app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'Uploads'

# my data
features = ['alcohol', 
            'volatile_acidity', 
            'sulphates', 
            'citric_acidity', 
            'total_sulfur_dioxide', 
            'density']


#my model
# loaded_model = pickle.load(open('tuned_redmodel.pkl, 'rb'))


@app.route('/')
def pred():
    data = [[1, 1, 1, 1, 1, 1]]
    X = pd.DataFrame(data)
    loaded_model = pickle.load(open('tuned_redmodel.pkl', 'rb'))
    output = loaded_model.predict(X).tolist()


    

    """
    # @app.route('/api',methods=['POST'])
    def predict():
    <form method="POST">
    <input name="text">
    <input type="submit">
    </form>




    # Get the data from the POST request.
    data = request.get_json(force=True)
    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([[np.array(data['exp'])]])
    # Take the first value of prediction
    """    
    return jsonify(output)
    

if __name__ == "__main__":
    app.run(debug=True)
