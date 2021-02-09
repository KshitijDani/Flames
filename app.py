import json

from flask import Flask, render_template, request
from api.exposed import returnLetter
from werkzeug.debug import console

app = Flask(__name__)

@app.route('/flames')
def home():
    return render_template('flames.html')

@app.route('/calculateFlames', methods = ['GET'])
def calculateFlames():

    name1 = request.args.get("name1")
    name2 = request.args.get("name2")

    letter = returnLetter(name1, name2)

    return letter

@app.route('/returnLetter', methods = ['GET'])
def randomletter():
    print("inside return")
    return "kshitij"

if __name__ == '__main__':
   app.run()