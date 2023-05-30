from flask import Flask, redirect, url_for, render_template , request
import pandas as pd
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict",methods = ["POST"])
def predict():
    displacement = float(request.form["displacement"])
    cylinders = int(request.form["cylinders"])
    horsepower = float(request.form["horsepower"])
    weight = float(request.form["weight"])
    acceleration = float(request.form["acceleration"])

    efficient_car = False

    return render_template("prediction.html",efficient_car = efficient_car)

if __name__ == "__main__":
    app.run()