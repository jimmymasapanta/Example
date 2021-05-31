import base64
import getpass
import hashlib
import hmac
import pprint
import requests
import json
import csv
from flask import Flask,render_template,Response,request,jsonify

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/informacion')
def informacion():
    return render_template('informacion.html')


@app.route('/informacionD',methods=["POST", "GET"])
def informacionD():
    if request.method=="POST":
        token= request.form['access_t']
        url_aps = "apigw-uswest4.central.arubanetworks.com/monitoring/v1/clients/wireless"
        url_aps_full= "https://" + url_aps + "?access_token=" + token
        result_aps = requests.get(url_aps_full)
        json_parsed_aps = result_aps.json()
        print(json_parsed_aps)
    return (json_parsed_aps)

if __name__== '__main__':
    app.run(debug=True)