from flask import render_template, redirect, url_for, flash
from werkzeug.security import check_password_hash

from application.db_model import User
from .form import LoginForm


def show_login_form():
    form = LoginForm()

    if form.validate_on_submit():
        enter_username = form.username.data
        enter_password = form.password.data
        try:
            user = User.query.filter_by(username=enter_username).first()
            check_password_hash(user.password, enter_password)
        except AttributeError:
            flash("Error")
        else:
            return redirect(url_for('/to-do-list.greeting'))

    return render_template('form_login.html', html_form=form)
