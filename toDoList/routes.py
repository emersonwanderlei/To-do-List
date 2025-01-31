from toDoList import app, database
from flask import render_template, redirect, url_for, request
from toDoList.forms import Form_task
from toDoList.models import Task

@app.route('/', methods=['GET', 'POST'])
def home():
    
    show_task = Task.query.all()
    formTask = Form_task()

    return render_template('home.html', formTask=formTask, show_task=show_task)

@app.route('/create', methods=['POST'])
def create():
    formTask = Form_task()
    if formTask.validate_on_submit() and 'button_create' in request.form:
        task = Task(description=formTask.description.data)
        database.session.add(task)
        database.session.commit()
        return redirect(url_for('home'))

@app.route('/delete/<int:id_task>', methods=['POST'])
def delete(id_task):
    formTask = Form_task()
    task = Task.query.get(id_task)
    if task and 'button_delete':
        database.session.delete(task)
        database.session.commit()
        return redirect(url_for('home'))

@app.route('/edit/<int:id_task>', methods=['GET', 'POST'])
def edit(id_task):
    formTask = Form_task()
    task = Task.query.get(id_task)
    if not task:
        return redirect(url_for('home'))
    if task:
        formTask.description.data = task.description

        show_task = Task.query.all()
    return render_template('home.html', id_task=id_task, editing=True, formTask=formTask, show_task=show_task)
        

@app.route('/update/<int:id_task>', methods=['POST'])
def update(id_task):
    formTask = Form_task()
    task = Task.query.get(id_task)
    if task and 'button_update':
        task.description = formTask.description.data

        database.session.commit()

        return redirect(url_for('home'))

