import pandas as pd
from flask_ngrok import run_with_ngrok
from flask import request, jsonify, Flask
import random as rk
app = Flask(__name__)
run_with_ngrok(app)

d = {
    "Numero": 1,
    "Nome": "mario",
    "Cidade": "Nova york",
    "Pais": "America",
    "Idade": 20
}


@app.route("/")

def home():
  return jsonify(d)

@app.route("/input")

def input():
  return jsonify(d)

@app.route("/output", methods=['GET','POST']) 

def predJson():
  pred = r.choice(["positive","negative"])
  nd = d
  nd["prediction"]=pred
  return jsonify(nd)

  app.run()
