from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
load_dotenv('.env')


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # não é obrigatorio
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db = SQLAlchemy(app=app)
migrate = Migrate(app=app,db=db)

from app.routes import home
from app.models import Contato

