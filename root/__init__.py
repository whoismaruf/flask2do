from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__,
            template_folder='templates',
            static_folder='static')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "You need to be logged in to get access 🔓"
login_manager.login_message_category = "warning"

app.config['SECRET_KEY'] = 'ringer234crf34rfw'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'


@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(int(user_id))


from . import views
