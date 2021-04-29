from flask import Blueprint
from .controller import show_registration_form
registration_blueprint = Blueprint('/join', __name__, template_folder='templates')


@registration_blueprint.route('/join', methods=['POST', 'GET'])
def show_registration():
    return show_registration_form()
