from flask import render_template, redirect, url_for
from .form import LoginForm
from werkzeug.security import generate_password_hash
from application.db_model import User


def show_login_form():
    form = LoginForm()

    if form.validate_on_submit():
        print(0000)
        enter_username = form.username.data
        enter_password_hash = generate_password_hash(form.password.data)

        user = User.query.filter_by(username=enter_username).first()
        print('PASSWORD IN DB', user.password)
        print('PASSWORD ENTER', enter_password_hash)
        if user.password == enter_password_hash:
            print(111)
            return redirect(url_for('main_page.routes.greeting'))
        else:
            print(222)
            return '<h3>Invalid</h3>'

    return render_template('form_login.html', html_form=form)
