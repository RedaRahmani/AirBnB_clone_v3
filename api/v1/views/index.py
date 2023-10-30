#!/usr/bin/python3
"""
index content view for API.
"""

from flask import jsonify
import models
from api.v1.views import app_views


@app_views.route("/status", strict_slashes=False)
def view_status():
    """
    status okay for /status
    """
    return jsonify({"status": "OK"})
