from datetime import datetime
# from flask import Flask, render_template
from . import app

from flask import Flask, request, redirect, url_for, render_template
import requests, json
from pprint import pprint
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField 
from wtforms.validators import DataRequired

# @app.route("/")
# def home():
#     return render_template("home.html")

# @app.route("/about/")
# def about():
#     return render_template("about.html")

# @app.route("/contact/")
# def contact():
#     return render_template("contact.html")

# @app.route("/hello/")
# @app.route("/hello/<name>")
# def hello_there(name = None):
#     return render_template(
#         "hello_there.html",
#         name=name,
#         date=datetime.now()
#     )

# @app.route("/api/data")
# def get_data():
#     return app.send_static_file("data.json")

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')
    # return redirect(url_for('non_med'))


@app.route('/non_med', methods=['GET','POST'])
def non_med():
    if request.method == 'POST':
        response = request.form.getlist('mycheckbox')
        print(response)
        results = testing(response)
        print(results)
        return render_template('nonmedical_results.html')
        # return render_template('nonmedical_results.html')
    else: 
        return render_template('nonmedical.html')

@app.route('/med', methods=['GET','POST'])
def med():
    if request.method == 'POST':
        response = request.form.getlist('mycheckbox')
        print(response)
        results = testing(response)
        print(results)
        return render_template('doctor_results.html')
    else: 
        return render_template('doctor.html')

# def med():
#     return "MEDICAL"

# #his works perfectly for doctor.html
# @app.route('/Medical', methods=['GET','POST'])
# def index():
#     if request.method == 'POST':
#         response = request.form.getlist('mycheckbox')
#         print(response)
#         results = testing(response)
#         print(results)
#         return render_template('index.html')
#     else: 
#         return render_template('doctor.html')

def testing(y):
    cough = 0
    diarrhea = 0
    chestpain = 0
    highfever = 0
    flu = 0
    weakness = 0
    myalgia = 0
    headache = 0
    nausea = 0
    lossoftaste = 0
    swollenlymph = 0
    noappetite = 0
    constipation = 0
    abdominal = 0
    lymphnode = 0
    rash = 0
    highfever=0
    fatigue = 0
    weightloss = 0
    excesssweat = 0

    for x in y:
        if(x=="1"):
            cough = 1
        elif(x=="2"):
            diarrhea = 1
        elif(x=="3"):
            chestpain = 1
        elif(x=="4"):
            highfever = 1
        elif(x=="5"):
            flu = 1
        elif(x=="6"):
            weakness = 1
        elif(x=="7"):
            myalgia = 1
        elif(x=="8"):
            headache = 1
        elif(x=="9"):
            nausea = 1
        elif(x=="10"):
            lossoftaste = 1
        elif(x=="11"):
            swollenlymph = 1
        elif(x=="12"):
            noappetite = 1
        elif(x=="13"):
            constipation = 1
        elif(x=="14"):
            abdominal = 1
        elif(x=="15"):
            lymphnode = 1
        elif(x=="16"):
            rash = 1
        elif(x=="17"):
            highfever
        elif(x=="18"):
            fatigue = 1
        elif(x=="19"):
            weightloss = 1
        else:
            excesssweat = 1

    return cough, diarrhea, chestpain, highfever, flu, weakness, myalgia, headache, nausea, lossoftaste, swollenlymph, noappetite, constipation, abdominal, lymphnode, rash, highfever, fatigue, weightloss, excesssweat
