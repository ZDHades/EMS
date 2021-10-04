from .import bp as main
from app import db
from flask import current_app as app, render_template, redirect, url_for, flash
from app.models import User
from flask_login import current_user, login_required

@main.route('/')
@login_required
def index():
    if current_user.is_authenticated:
        return render_template('login.html')
    else:
        data = []
    return render_template('index.html', data=data)
    