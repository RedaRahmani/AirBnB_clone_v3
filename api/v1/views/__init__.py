#!/usr/bin/python3
"""
define blueprint for API.
"""

from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix='/api/v1')
"""
blueprint API for airbnb
"""
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
