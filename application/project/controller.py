import flask
from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user
from application.models import User, users_projects
from application.models import Project
from application import db
from application.project.form import ProjectCreating

def show_projects_controller():
    pass

def create_project_controller():
    form = ProjectCreating()

    if form.validate_on_submit():
        new_project =  Project(
            title = form.title.data,
            subject = form.subject.data,
            short_description = form.short_description.data,
            description = form.description.data)
        db.session.add(new_project)
        user = User.query.filter_by(User.name == current_user)
        new_project.users.append(user)
        db.session.commit()
        return redirect(url_for('main.index')) #project.show_projects
    return render_template('project/creating.html', title='Creating project', form=form)