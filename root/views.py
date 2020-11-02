from root import app, db, bcrypt
from flask import render_template, redirect, url_for, flash
from .models import Todo, User
from .forms import TodoForm, UserRegistrationForm, LoginForm
from flask_login import current_user, login_user, logout_user, login_required


# Uncomment it when you deploy in a server where you have SSL certificate
# It will redirect your domain/subdomain to https://

# @app.before_request
# def before_request():
#     if request.url.startswith('http://'):
#         url = request.url.replace('http://', 'https://', 1)
#         code = 301
#         return redirect(url, code=code)


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = TodoForm()
    if form.validate_on_submit():
        obj = Todo(task=form.task.data, tasker_id=current_user.id)
        db.session.add(obj)
        db.session.commit()
        return redirect(url_for('index'))
    tasks = current_user.tasks
    return render_template('index.html', form=form, tasks=tasks)


@app.route('/delete/<int:task_id>')
def delete(task_id):
    obj = Todo.query.filter_by(id=task_id).first()
    db.session.delete(obj)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def registration():
    form = UserRegistrationForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        u = User(username=form.username.data, email=form.email.data, password=hashed_pass)
        db.session.add(u)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('auth_register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('index'))
        else:
            flash(message="Your username and password is incorrect", category='danger')
            return redirect(url_for('login'))
    return render_template('auth_login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
