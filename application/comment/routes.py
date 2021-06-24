import os

from flask import Blueprint
from flask_security import login_required

import application.comment.controller as controller
from application.admin import is_admin

template_dir = os.path.abspath('../templates')
comment_blueprint = Blueprint('comment', __name__, url_prefix='/comment', template_folder=template_dir)


@comment_blueprint.route('/<task_id>/comments')
@login_required
def show_comments(task_id):
    return controller.show_comments(task_id)


@comment_blueprint.route('/<task_id>/<parent_id>/reply', methods = ['POST', 'GET'])
@login_required
def create_comment(task_id, parent_id):
    return controller.create_comment(task_id, parent_id)