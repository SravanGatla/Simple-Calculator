import columns as columns
import data as data
from flask import Flask, render_template, request, url_for, json, jsonify
import pandas as pd

import csv

app = Flask(__name__)


@app.route('/')
def main():  # put application's code here
    return render_template("index.html")


@app.route("/Simple_Calculator")
def Simple_Calculator():
    return render_template("Simple_Calculator.html")


@app.route("/AAA_Testing")
def AAA_Testing():
    return render_template("AAA_Testing.html")


@app.route("/OOPS_Concepts")
def OOPS_Concepts():
    return render_template("OOPS_Concepts.html")


@app.route("/Python_Terminology")
def Python_Terminology():
    return render_template("Python_Terminology.html")


@app.route("/SOLID_Object_Oriente_Design")
def SOLID_Object_Oriente_Design():
    return render_template("SOLID_Object_Oriente_Design.html")


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
        return render_template("Simple_Calculator.html", note=note)
    return render_template("Simple_Calculator.html", result=result, note=note, color=color)


if __name__ == '__main__':
    app.run(debug=True)
