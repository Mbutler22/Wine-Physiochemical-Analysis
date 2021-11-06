from flask import Flask, render_template, redirect,jsonify,request
from joblib import load
import socket
import os

app = Flask(__name__)



@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/visualizations.html")
def visitations():
   
   return render_template("visualizations.html")

@app.route("/machine_learning.html")
def ml():
   
   return render_template("machine_learning.html")

@app.route('/white_data', methods=['POST'])
def white_data():
    print('white_data')
    outcome="something"
    return render_template("machine_learning.html", routcome=outcome)

@app.route('/red_data', methods=['POST'])
def red_data():
    print('red_data')
    X=[]
    X.append(request.form['rvolacidity'])
    #print('before sulfure')
    X.append(request.form['rTotalSulfur'])
    X.append(request.form['rDensity'])
    X.append(request.form['rSulfates'])
    X.append(request.form['rAlcohol'])
    print("before XX")
    XX=[X]
    print('before load')
    classifier = load('Red_Wine_Quality.joblib')
    print("before predict")
    result=classifier.predict(XX)

    if (result==0):
        outcome="Hmm... there are better wines"
    else:
        outcome="Good Choice!"
    print(f"Sulfur:{request.form['rTotalSulfur']}<br>{outcome}")
    return render_template("machine_learning.html", routcome=outcome)
    

@app.route("/team.html")
def team():
    return render_template("team.html")



if __name__ == "__main__":
    app.run(debug=True)


