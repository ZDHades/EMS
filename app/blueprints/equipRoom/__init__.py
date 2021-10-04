from flask import Blueprint

bp = Blueprint("equipRoom", __name__, urlprefix='/equipRoom')

from .import models, routes
