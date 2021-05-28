from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user

from application import db
from application.models import Project
from application.models import User
from application.models import users_projects
from application.project.form import ProjectForm


def show_projects():
    projects = current_user.projects[::-1]
    return render_template("project/all_projects.html", projects=projects)


def show_project(project_id):
    data = Project.query.filter_by(id=project_id).first()
    return render_template("project/project.html", data=data)


def edit_project(project_id):
    members = User.query.all()

    project = Project.query.filter_by(id=project_id).first()

    project_members = User.query.join(users_projects).join(Project).filter(
        users_projects.c.project_id == project.id).all()

    form = ProjectForm(request.form, obj=project)

    form.users.choices = members

    if form.validate_on_submit():
        form.populate_obj(project)
        db.session.commit()
        return redirect(url_for('project.show_project', project_id=project.id))

    return render_template('project/edit_project.html', project=project,
                           project_members=project_members, form=form)


def delete_member_of_project(project_id):
    project_member = User.query.join(users_projects).join(Project).filter(
        users_projects.c.project_id == project_id).first()

    """delete member"""
    db.session.commit()
    return redirect(url_for('project.edit_project', project_id=project_id))


def delete_project(project_id):
    project = Project.query.filter_by(id=project_id).first()
    db.session.delete(project)
    db.session.commit()
    flash(f'The project {project.title} has been deleted ')
    return redirect(url_for('project.show_projects'))


def create_project():
    members = User.query.all()
    form = ProjectForm()
    form.users.choices = members

    if form.validate_on_submit():
        new_project = Project(
            title = form.title.data,
            subject = form.subject.data,
            short_description = form.short_description.data,
            description = form.description.data)

        multiselect = request.form.getlist('members')
        elected_members = (list(map(int, multiselect)))
        for user in elected_members:
            existing_user = User.query.filter_by(id=user).first()
            new_project.users.append(existing_user)
            if existing_user is None:
                flash('Unexpected user')
        main_user = User.query.filter_by(username=current_user.username).first()
        new_project.users.append(main_user)
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('project.show_projects'))
    return render_template('project/creating.html', title='Creating project', form=form)
