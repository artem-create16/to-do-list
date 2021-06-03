import os

from flask import Blueprint
from flask_security import login_required

import application.project.controller as controller
from application.admin import is_admin

template_dir = os.path.abspath('../templates')
project_blueprint = Blueprint('project', __name__, url_prefix='/project', template_folder=template_dir)


@project_blueprint.route('/my')
@login_required
def show_projects():
    return controller.show_projects()


@project_blueprint.route('/new', methods=['POST', 'GET'])
@login_required
@is_admin
def create_project():
    return controller.create_project()


@project_blueprint.route('/<project_id>')
@login_required
def show_project(project_id):
    return controller.show_project(project_id)


@project_blueprint.route('/<project_id>/edit', methods=['GET', 'POST'])
@login_required
@is_admin
def edit_project(project_id):
    return controller.edit_project(project_id)


@project_blueprint.route('/<project_id>/delete')
@login_required
@is_admin
def delete_project(project_id):
    return controller.delete_project(project_id)
