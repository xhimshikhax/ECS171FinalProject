from flask import Flask, redirect, url_for, render_template , request
import pandas as pd
from model import train_classifier, predict_efficiency
app = Flask(__name__)

clf = train_classifier('project.csv')

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

    car_data = [cylinders, displacement, horsepower, weight, acceleration] # input to your model
    prediction = predict_efficiency(clf, car_data)

    # Your model predicts 1 for efficient and 0 for not efficient
    efficient_car = prediction == 1

    return render_template("prediction.html", efficient_car = efficient_car)

if __name__ == "__main__":
    app.run()