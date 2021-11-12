from flask import Flask, render_template, redirect,jsonify,request
from joblib import load
import socket
import os

app = Flask(__name__)


class WWines: 
    def __init__(self):
        self.outcome=""
        self.country=1
        self.price=1
        self.variety=1

    def getData(self, request):
        self.country = int(request.form['country'])
        self.price = int(request.form['price'])
        self.variety = int(request.form['variety'])
        # print(self.country)
        # print(self.price)
        # print(self.variety)




@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/visualizations.html")
def visualization():
   
   return render_template("visualizations.html")

# will do: change to class 

@app.route("/machine_learning.html")
def ml():
   global rvolacidity, rTotalSulfur, rDensity, rSulfates, rAlcohol
   global wAcidity, wFreeSulfur, wDensity, wAlcohol
   global gwine 
   global routcome, woutcome  

   return render_template("machine_learning.html", routcome=routcome, rvolacidity=rvolacidity,\
                            rTotalSulfur=rTotalSulfur , rDensity= rDensity, rSulfates=rSulfates, rAlcohol=rAlcohol,\
                            woutcome = woutcome, wAcidity=wAcidity, wFreeSulfur=wFreeSulfur,wDensity = wDensity,\
                            wAlcohol =wAlcohol,\
                            gwine=gwine)


@app.route('/white_data', methods=['POST'])
def white_data():
    global wAcidity, wFreeSulfur, wDensity, wAlcohol  
    global woutcome 
    X=[]
    wAcidity= request.form['wAcidity']
    X.append(wAcidity)
    wFreeSulfur = request.form['wFreeSulfur']
    X.append(wFreeSulfur)
    wDensity= request.form['wDensity']
    X.append(wDensity)
    wAlcohol = request.form['wAlcohol']
    X.append(wAlcohol)
    XX=[X]
    classifier = load('white_wine_model.joblib')
    result=classifier.predict(XX)

    if (result==0):
        woutcome="Hmm... there are better wines"
    else:
        woutcome="Good Choice!"
    return redirect("/machine_learning.html")



@app.route('/red_data', methods=['POST'])
def red_data():
    global rvolacidity, rTotalSulfur, rDensity, rSulfates, rAlcohol
    global routcome  
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
    return redirect("/machine_learning.html")

@app.route('/world_data', methods=['POST'])
def world_data():
    global gwine
    gwine.getData(request)
    testdata = [0] * 45
    testdata[gwine.country-1]= 1
    testdata[gwine.price+36]= 1
    testdata[gwine.variety+6]= 1
    XX=[testdata]
    classifier = load('World_Wine_Quality.joblib')
    result=classifier.predict(XX)

    if (result==0):
        gwine.outcome="Hmm... there are better wines"
    else:
        gwine.outcome="Good Choice!"
    return redirect("/machine_learning.html")    


@app.route("/reset.html")
def reset():
    resetValues()
    return redirect("/machine_learning.html")  

def resetValues():
    global rvolacidity, rTotalSulfur, rDensity, rSulfates, rAlcohol
    global wAcidity, wFreeSulfur, wDensity, wAlcohol
    global gwine 
    global routcome, woutcome 
    
    routcome = ""
    rvolacidity = 0.12
    rTotalSulfur = 6.0
    rDensity = 0.990
    rSulfates = 0.33
    rAlcohol = 8.4
    woutcome =""
    wAcidity = 0.08
    wFreeSulfur = 2.00
    wDensity = 0.987
    wAlcohol = 8.0

    gwine = WWines()


@app.route("/team.html")
def team():
    return render_template("team.html")

resetValues()

if __name__ == "__main__":
    app.run(debug=True)





