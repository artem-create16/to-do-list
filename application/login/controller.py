from flask import render_template, redirect, url_for
from .form import LoginForm


def show_login_form():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

    return render_template('form_registration.html', html_form=form)
