from flask import render_template, redirect, url_for
from .form import LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from application.db_model import User


def show_login_form():
    form = LoginForm()

    if form.validate_on_submit():
        enter_username = form.username.data
        enter_password = form.password.data
        user = User.query.filter_by(username=enter_username).first()
        if check_password_hash(user.password, enter_password):
            return redirect(url_for('/to-do-list.greeting'))
        else:
            return '<h3>Invalid</h3>'

    return render_template('form_login.html', html_form=form)
