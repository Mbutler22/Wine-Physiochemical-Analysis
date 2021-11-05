from flask import Flask, render_template, redirect,jsonify
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


@app.route("/team.html")
def team():
    return render_template("team.html")



if __name__ == "__main__":
    app.run(debug=True)


