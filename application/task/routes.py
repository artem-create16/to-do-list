import os

from flask import Blueprint
from flask_login import login_required

import application.task.controller as controller
from application.admin import is_admin


template_dir = os.path.abspath('../templates')
task_blueprint = Blueprint('task', __name__, url_prefix='/task', template_folder=template_dir)


@task_blueprint.route('/<project_id>/create-task', methods=['GET', 'POST'])
@login_required
@is_admin
def create_task(project_id):
    return controller.create_task(project_id)


@task_blueprint.route('/<task_id>/delete-task')
@login_required
@is_admin
def delete_task(task_id):
    return controller.delete_task(task_id)


@task_blueprint.route('/<project_id>/tasks', methods=['GET', 'POST'])
@login_required
def show_tasks(project_id):
    return controller.show_tasks(project_id)


@task_blueprint.route('/<task_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    return controller.edit_task(task_id)
