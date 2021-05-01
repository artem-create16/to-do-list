from flask import Blueprint

from .controller import show_login_form

login_blueprint = Blueprint('/login', __name__, template_folder='templates')


@login_blueprint.route('/login', methods=['POST', 'GET'])
def show_login():
    return show_login_form()
