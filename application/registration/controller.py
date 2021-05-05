from flask import render_template, redirect, url_for
from .form import RegistrationForm
from application.db_model import User, Role
from application import db
from werkzeug.security import generate_password_hash,  check_password_hash


def show_registration_form():
    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        password_hash = generate_password_hash(password)
        new_user = User(username=username, email=email, password=password_hash, role=Role.user)
        db.session.add(new_user)
        db.session.commit()
        return render_template('successful_registration.html', html_form=form, username=username)

    return render_template('form_registration.html', html_form=form)
