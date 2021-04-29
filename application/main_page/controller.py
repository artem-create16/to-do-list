from flask import render_template, redirect, url_for


def show_form():
    return render_template('base.html')