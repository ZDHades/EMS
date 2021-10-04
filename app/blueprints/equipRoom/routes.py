from .import bp as equipRoom
from app import db
from flask import current_app as app, render_template, request, redirect, url_for, flash, session
from app.models import User
from flask_login import login_user, logout_user
from werkzeug.urls import url_parse


@equipRoom.route('/main', methods=['GET', 'POST'])
def main():
    pass


