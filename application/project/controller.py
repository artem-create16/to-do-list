import flask
import datetime
from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user
from application.models import User, users_projects, Project
from application.models import Project
from application import db
from application.project.form import ProjectForm

def show_projects_controller():
    projects = current_user.projects[::-1]
    return render_template("project/all_projects.html", projects=projects)

def show_project_controller(project_id):
    data = Project.query.filter_by(id=project_id).first()
    return render_template("project/project.html", data=data)

def edit_project_controller(project_id):
    project = Project.query.filter_by(id=project_id).first()
    if request.method == "POST":
        form = ProjectForm(request.form, obj=project)
        form.populate_obj(project)
        db.session.commit()
        return redirect(url_for('project.show_project', project_id=project.id))

    form = ProjectForm(obj=project)
    return render_template('project/edit_project.html', project=project, form=form)


def create_project_controller():
    form = ProjectForm()

    if form.validate_on_submit():
        new_project =  Project(
            title = form.title.data,
            subject = form.subject.data,
            short_description = form.short_description.data,
            description = form.description.data)
        user = User.query.filter_by(username=current_user.username).first()
        new_project.users.append(user)
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('project.show_projects')) #project.show_projects
    return render_template('project/creating.html', title='Creating project', form=form)
