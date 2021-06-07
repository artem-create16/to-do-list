from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user

from application import db
from application.models import User, Task, users_projects, Project
from application.task.form import TaskForm


def save_data(form, project_id):
    pass


def create_task(project_id):
    project = Project.query.get(project_id)
    members = project.users
    form = TaskForm()
    form.assignee_id.choices = members
    if request.method == 'POST':
        creator = User.query.get(current_user.id)
        elected_member = request.form.get('members')
        assignee_id = int(elected_member)
        new_task = Task(
            project_id=project_id,
            subject=form.subject.data,
            description=form.description.data,
            creator_id=creator.id,
            assignee_id=assignee_id,
            status='to_do'
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('project.show_project', project_id=project_id))
    return render_template('task/creating.html', title='Creating task', form=form)


def edit_task(task_id):
    task = Task.query.get(task_id)
    project_id = task.project_id
    project = Project.query.get(project_id)
    members = project.users
    form = TaskForm(request.form, obj=task)
    form.assignee_id.choices = members
    if request.method == 'POST':
        form.populate_obj(task)
        db.session.commit()
        return redirect(url_for('task.show_tasks', project_id=project_id))
    return render_template('task/edit_task.html', task=task, project_id=project_id, form=form)


def delete_task(task_id):
    task = Task.query.get(task_id)
    project_id=task.project_id
    db.session.delete(task)
    db.session.commit()
    flash(f'The task {task.subject} has been deleted')
    return redirect(url_for('project.show_project', project_id=project_id))


def show_tasks(project_id):
    tasks_data = Task.query.filter_by(project_id=project_id).all()
    tasks_data.reverse()
    return render_template('task/tasks.html', tasks_data=tasks_data, project_id=project_id)


def show_tasks_for_user(project_id):
    tasks_data = Task.query.filter_by(project_id=project_id, assignee_id=current_user.id).all()
    project_data = Project.query.get(project_id)
    return render_template('task/users_tasks.html', tasks_data=tasks_data, project_data=project_data)



