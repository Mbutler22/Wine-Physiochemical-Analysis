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
   global rvolacidity, rTotalSulfur, rDensity, rSulfates, rAlcohol
   global routcome 
   routcome = ""
   rvolacidity = 0.12
   rTotalSulfur = 6.0
   rDensity = 0.990
   rSulfates = 0.33
   rAlcohol = 8.4
   return render_template("machine_learning.html", routcome=routcome, rvolacidity=rvolacidity,\
                            rTotalSulfur=rTotalSulfur , rDensity= rDensity, rSulfates=rSulfates, rAlcohol=rAlcohol)

@app.route('/white_data', methods=['POST'])
def white_data():
    print('white_data')
    return render_template("machine_learning.html", routcome=routcome, rvolacidity=rvolacidity,\
                            rTotalSulfur=rTotalSulfur , rDensity= rDensity, rSulfates=rSulfates, rAlcohol=rAlcohol)

@app.route('/red_data', methods=['POST'])
def red_data():
    X=[]
    rvolacidity= request.form['rvolacidity']
    X.append(rvolacidity)
    rTotalSulfur = request.form['rTotalSulfur']
    X.append(rTotalSulfur)
    rDensity= request.form['rDensity']
    X.append(rDensity)
    rSulfates = request.form['rSulfates']
    X.append(rSulfates)
    rAlcohol = request.form['rAlcohol']
    X.append(rAlcohol)
    XX=[X]
    classifier = load('Red_Wine_Quality.joblib')
    result=classifier.predict(XX)

    if (result==0):
        routcome="Hmm... there are better wines"
    else:
        routcome="Good Choice!"
    return render_template("machine_learning.html", routcome=routcome, rvolacidity=rvolacidity,\
                            rTotalSulfur=rTotalSulfur , rDensity= rDensity, rSulfates=rSulfates, rAlcohol=rAlcohol)

    

@app.route("/team.html")
def team():
    return render_template("team.html")



if __name__ == "__main__":
    app.run(debug=True)


