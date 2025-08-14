from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # não é obrigatorio
app.config['SECRET_KEY'] = 'ASDAS5JDK2LNASD_ASNDAASSDNÇ213123LKAJSDLKJ!AS512DJALSKDNASD'

db = SQLAlchemy(app=app)
migrate = Migrate(app=app,db=db)

from app.routes import home
from app.models import Contato

