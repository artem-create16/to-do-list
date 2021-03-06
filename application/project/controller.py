from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user

from application import db
from application.models import Project, User
from application.project.form import ProjectForm


def show_projects():
    projects = current_user.projects
    projects.reverse()
    return render_template("project/all_projects.html", projects=projects)


def show_project(project_id):
    project_data = Project.query.get(project_id)
    return render_template("project/project.html", project_data=project_data)


def save_data(project):
    multiselect = request.form.getlist('members')
    elected_members = map(int, multiselect)
    members = User.query.filter(User.id.in_(elected_members)).all()
    project.users.extend(members)
    db.session.commit()


def create_project():
    members = User.query.all()
    form = ProjectForm()
    form.users.choices = members
    if form.validate_on_submit():
        new_project = Project(form.title.data,
                              form.subject.data,
                              form.short_description.data,
                              form.description.data)
        save_data(new_project)
        return redirect(url_for('project.show_projects'))
    return render_template('project/creating.html', title='Creating project', form=form)


def edit_project(project_id):
    members = User.query.all()
    project = Project.query.get(project_id)
    form = ProjectForm(request.form, obj=project)
    form.users.choices = members
    if form.validate_on_submit():
        form.populate_obj(project)
        save_data(project)
        return redirect(url_for('project.show_project', project_id=project.id))
    return render_template('project/edit_project.html', project=project, form=form)


def delete_project(project_id):
    project = Project.query.get(project_id)
    db.session.delete(project)
    db.session.commit()
    flash(f'The project {project.title} has been deleted')
    return redirect(url_for('project.show_projects'))
