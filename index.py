import columns as columns
import data as data
from flask import Flask, render_template, request, url_for,json,jsonify
import pandas as pd
import csv

app = Flask(__name__)


@app.route('/')
def main():  # put application's code here
    return render_template("index.html")


@app.route("/simple")
def simple():
    return render_template("simple.html")


@app.route("/first")
def first():
    return render_template("first.html")


@app.route("/second")
def second():
    return render_template("second.html")


@app.route("/third")
def third():
    return render_template("third.html")


@app.route("/fourth")
def fourth():
    return render_template("fourth.html")


@app.route("/calculate", methods=["post"])
def calculate():
    first_number = int(request.form["firstNumber"])
    operation = request.form["operation"]
    second_number = int(request.form["secondNumber"])
    note = ""
    color = "alert-success"
    if operation == "plus":
        result = first_number + second_number
        note = "Addition was performed successfully"
    elif operation == "minus":
        result = first_number - second_number
        note = "subtraction was performed successfully"
    elif operation == "multiply":
        result = first_number * second_number
        note = "multiplication was performed successfully"
    elif operation == "divide":
        result = first_number / second_number
        note = "division was performed successfully"
    else:
        note = "select anyone of the displayed operations"
        color = "alert-danger"
        return render_template("simple.html", note=note)
    return render_template("simple.html", result=result, note=note, color=color)


calculation = pd.DataFrame([[data["first_number"], data["second_number"], data["operation"], data["result"]]], columns = ['first_number', 'second_number', 'operation', 'result'])
calculation.to_csv("calculations.csv", mode='a', index=False, header=False)

if __name__ == '__main__':
    app.run(debug=True)
