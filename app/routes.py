from app import app, db
from flask import render_template, url_for, request, redirect

from app.models import Contato
from app.form import ContatoForm

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

@app.route('/contatoform', methods = ['GET','POST'])
def contato_form():
    form = ContatoForm()
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('home'))
    return render_template('contato_form.html',context=context,form=form)



@app.route('/contato/lista/')
def contato_lista():
    if request.method == "GET":
        pesquisa = request.args.get('pesquisa','')
    
    dados = Contato.query.order_by('name')
    
    if pesquisa != '':
        dados = dados.filter_by(name = pesquisa)
        
    context = {'dados':dados.all()}
    
    return render_template('contato_lista.html',context=context)

# ROTA DINAMICA
@app.route('/contato/<int:id>/')
def contato_detail(id):
    obj = Contato.query.get(id)
    
    
    return render_template('contato_detail.html',obj=obj)

