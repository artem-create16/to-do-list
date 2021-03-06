from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user

from application import db
from application.models import Task, Project, Status

from application.task.form import TaskForm
from application.helper.notification import send_notification


def create_task(project_id):
    project = Project.query.get(project_id)
    form = TaskForm()
    form.assignee_id.choices = project.users
    if request.method == 'POST':
        assignee_id = int(request.form.get('members'))
        new_task = Task(project_id,
                        form.subject.data,
                        form.description.data,
                        current_user.id,
                        assignee_id,
                        Status.to_do.name)

        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('project.show_project', project_id=project_id))
    return render_template('task/creating.html', title='Creating task', form=form)


def edit_task(task_id):
    task = Task.query.get(task_id)
    form = TaskForm(request.form, obj=task)
    form.assignee_id.choices = task.project.users
    if request.method == 'POST':
        form.populate_obj(task)
        db.session.commit()
        send_notification(task)
        return redirect(url_for('task.show_tasks', project_id=task.project_id))
    return render_template(
        'task/edit_task.html',
        task=task,
        project_id=task.project_id,
        statuses=Status,
        form=form)


def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    flash(f'The task {task.subject} has been deleted')
    return redirect(url_for('project.show_project', project_id=task.project_id))


def show_tasks(project_id):
    tasks_data = Task.query.filter_by(project_id=project_id).order_by(Task.created_at.desc()).all()
    return render_template('task/tasks.html', tasks_data=tasks_data)
