from flask import Blueprint

bp = Blueprint("authentication", __name__, url_prefix='/')

from .import models, routes
