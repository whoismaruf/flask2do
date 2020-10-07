from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, 
            template_folder='templates',
            static_folder='static')

db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'rejngorl234crf34rfw'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vault.db'

from . import views