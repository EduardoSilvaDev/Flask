from app import app
from flask import render_template, url_for


@app.route('/')
def home():
    usuario = 'Eduardo'
    return render_template('index.html',usuario=usuario)


@app.route('/novo')
def newroute():
    return "new route"
