#!/usr/bin/python3
"""
Endpoint (route) will be to return the status of your API
"""

from flask import Flask, jsonify
from os import getenv
from flask_cors import CORS
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown(self):
    """
    teardown fubction to call storage.close()
    """
    return storage.close()


@app.errorhandler(404)
def error(e):
    """
    404 http error
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    host = getenv("HBNB_API_HOST") if getenv("HBNB_API_HOST") else "0.0.0.0"
    port = getenv("HBNB_API_PORT") if getenv("HBNB_API_PORT") else 5000
    app.run(host=host, port=port, threaded=True)
