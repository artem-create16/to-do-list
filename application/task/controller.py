from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user

from application import db
from application.models import User, Task, users_projects, Project
from application.task.form import TaskForm


def create_task(project_id):
    project = Project.query.filter_by(id=project_id).first()
    members = User.query.join(users_projects).join(Project).filter(
        users_projects.c.project_id == project.id).all()
    form = TaskForm()
    form.assignee_id.choices = members
    if request.method == 'POST':
        creator = User.query.filter_by(username=current_user.username).first()
        select = request.form.getlist('members')
        assignee_id = int(select[0])
        new_task = Task(
            project_id = project_id,
            subject = form.subject.data,
            description = form.description.data,
            creator_id = creator.id,
            assignee_id = assignee_id,
            status = 'to_do'
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('project.show_project', project_id=project_id))
    return render_template('task/creating.html', title='Creating task', form=form)


def delete_task(task_id, project_id):
    task = Task.query.filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()
    flash(f'The task {task.subject} has been deleted')
    return redirect(url_for('project.show_project', project_id=project_id))


def show_task(task_id, project_id):
    task_data = Task.query.filter_by(id=task_id).first()
    project_data = Project.query.filter_by(id=project_id).first()
    return render_template("task/task.html", task_data=task_data, project_data=project_data)


def show_tasks_for_user(project_id):
    tasks_data = Task.query.filter_by(project_id=project_id, assignee_id=current_user.id).all()
    project_data = Project.query.filter_by(id=project_id).first()
    return render_template('task/users_tasks.html', tasks_data=tasks_data, project_data=project_data)


def edit(task_status):
    pass