from app import app
from flask import render_template, url_for


@app.route('/')
def home():
    usuario = 'Eduardo'
    context = {
        'user':'Eduardo',
        'idade':30,
        'city':'São Caitano'
    }
    return render_template('index.html',usuario=usuario,context=context)


@app.route('/novo')
def newroute():
    return "new route"
