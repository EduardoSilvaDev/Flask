from app import app, db
from flask import render_template, url_for, request
from app.models import Contato

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

@app.route('/contato',methods=['GET','POST'])
def contato():
    context= {}
    if request.method=='GET':
        search = request.args.get('search')
        context.update({'search':search})
        print('GET: ',context)
    if request.method=='POST':
        # search = request.form['search']
        # print('POST: ',search)
        
        name = request.form['name'].title()
        email = request.form['email'].lower()
        subject = request.form['subject']
        message = request.form['message']
        
        contato = Contato(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        print(contato)
        db.session.add(contato)
        db.session.commit()
        
    return render_template('formulario.html',context=context)

@app.route('/contatoform')
def contato_form():
    if request.method=='POST':
        pass
    return render_template('contato_form.html')