from flask import render_template, redirect, url_for
from .form import RegistrationForm
from application.db_model import User


def show_registration_form():
    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password_hash = User.set_password(form.username.password)

    return render_template('form_registration.html', html_form=form)
