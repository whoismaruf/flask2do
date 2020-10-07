from root import app, db
from flask import render_template, redirect, request, url_for
from .models import Todo
from .forms import TodoForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TodoForm()
    if form.validate_on_submit():
            obj = Todo(task=form.task.data)
            db.session.add(obj)
            db.session.commit()
            return redirect(url_for('index'))
    tasks = Todo.query.all()
    print(type(tasks))
    return render_template('index.html', form=form, tasks=tasks)

@app.route('/delete/<int:task_id>')
def delete(task_id):
    obj = Todo.query.filter_by(id=task_id)
    obj.delete()
    db.session.commit()
    return redirect(url_for('index'))