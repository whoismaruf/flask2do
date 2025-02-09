from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, PasswordField, BooleanField, TextField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from .models import Todo, User



class TodoForm(FlaskForm):
    task = TextField('Task Name',
                     validators=[DataRequired(),
                                 Length(min=5, message='At least 5 characters are required 😁')])
    submit = SubmitField('Add Task')

    def validate_task(self, task):
        if Todo.query.filter_by(task=task.data).first():
            raise ValidationError('Similar tasks are already in the list!')


class UserRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=32)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('Username has been taken already 😪')

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Email has been taken already 😪')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Stay logged in?')
    submit = SubmitField('Login')
