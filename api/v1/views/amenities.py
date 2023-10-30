#!/usr/bin/python3
"""
new view for Amenity
"""
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response


@app_views.route('/amenities', strict_slashes=False)
def get_amenities():
    """get all amenities"""
    amenities = storage.all(Amenity)
    if amenities is None:
        abort(404)
    return jsonify([amenity.to_dict() for amenity in amenities.values()])


@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_amenity(amenity_id):
    """get amenity by id"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delette(amenity_id):
    """Delete amenitie by id"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    amenity.delete()
    storage.save()
    return make_response("{}", 200)


@app_views.route('/amenities', methods=['POST'],
                 strict_slashes=False)
def post():
    """POST"""
    res = request.get_json()
    if not res:
        return abort(400, {'message': 'Not a JSON'})
    if 'name' not in res:
        return abort(400, {'message': 'Missing name'})
    new_amenity = Amenity(**res)
    new_amenity.save()
    return jsonify(new_amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def put(amenity_id):
    """put"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    res = request.get_json()
    if res is None:
        return abort(400, {'message': 'Not a JSON'})
    for key, value in res.items():
        if key not in ["id", "state_id", "created_at", "updated_at"]:
            setattr(amenity, key, value)
    storage.save()
    return jsonify(amenity.to_dict()), 200
