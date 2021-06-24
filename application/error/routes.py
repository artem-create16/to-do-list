from flask import render_template, Blueprint
import os


template_dir = os.path.abspath('../templates')
error_blueprint = Blueprint('error', __name__, url_prefix='/error', template_folder=template_dir)


@error_blueprint.app_errorhandler(403)
def not_found_error(error):
    return render_template('error/error_403.html'),403
