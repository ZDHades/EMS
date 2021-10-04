from .import bp as authentication
from app import db
from flask import current_app as app, render_template, request, redirect, url_for, flash, session
from app.models import User
from flask_login import login_user, logout_user
from werkzeug.urls import url_parse


@authentication.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        r = request.form
        user = User.query.filter_by(email=r.get('email')).first()
        if user is None or not user.check_password(r.get('password')):
            flash("You have either used an incorrect email or password!", 'danger')
            return redirect(url_for('authentication.login'))
        
        next_page = request.args.get('next')
        login_user(user, remember=r.get('remember_me'))
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        flash("You have successfully logged in!", 'success')
        return redirect(next_page)
    return render_template('login.html')

@authentication.route('/logout')
def logout():
    logout_user()
    flash("You have successfully logged out!", 'info')
    return redirect(url_for('authentication.login'))


