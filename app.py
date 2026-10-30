from flask import Flask, g, request
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello if you are looking for the word go to /deepseek"
@app.route('/deepseek')       
def deepseek():
    return "Hello your word is apple"
