# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def loadpage():
    return render_template('home.html', query="")


@app.route("/", methods=['POST'])
def cancerprediction():
    # Correct dataset URL
    dataset_url = "https://raw.githubusercontent.com/pik1989/MLClasses/refs/heads/main/data/data%20(2).csv"
    df = pd.read_csv(dataset_url)
    
    # Convert user input to float
    inputQuery1 = float(request.form['query1'])
    inputQuery2 = float(request.form['query2'])
    inputQuery3 = float(request.form['query3'])
    inputQuery4 = float(request.form['query4'])
    inputQuery5 = float(request.form['query5'])
 
    # Prepare dataset
    df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})
    features = [
        'radius_mean', 'texture_mean', 'perimeter_mean',
        'smoothness_mean', 'compactness_mean'
    ]
        
    x = df[features]
    y = df['diagnosis']
    X_train, X_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2
    )
    
    # Train model
    model = RandomForestClassifier(n_estimators=500, n_jobs=-1)
    model.fit(X_train, y_train)
    
    # Prepare new input
    new_data = [[
        inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5
    ]]
    new_df = pd.DataFrame(new_data, columns=features)
    
    prediction = model.predict(new_df)[0]
    confidence = model.predict_proba(new_df)[0][1] * 100
    
    # Output messages
    if prediction == 1:
        output1 = "The patient is diagnosed with Breast cancer"
        output2 = "Confidence: {:.2f}%".format(confidence)
    else:
        output1 = "The patient is not diagnosed with Breast cancer"
        output2 = ""
    
    return render_template(
        'home.html',
        output1=output1,
        output2=output2,
        query1=request.form['query1'],
        query2=request.form['query2'],
        query3=request.form['query3'],
        query4=request.form['query4'],
        query5=request.form['query5']
    )
