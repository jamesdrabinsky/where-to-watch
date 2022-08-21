"""
The shows blueprint handles the user management for this application.
Specifically, this blueprint allows for users to search, add, edit, and delete
shows data from their portfolio.
"""

from flask import Blueprint

shows_blueprint = Blueprint('shows', __name__, template_folder='templates')

from . import routes