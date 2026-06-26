from flask import jsonify
from website.resources import get_resource_json

from . import api


RESOURCE_ENDPOINTS = {
    'career': 'career.json',
    'education': 'education.json',
    'leadership': 'leadership.json',
    'repos': 'repos.json',
    'skills': 'skills.json',
}


def _resource(name):
    return get_resource_json(RESOURCE_ENDPOINTS[name])


@api.route('/resume', methods=['GET'])
def resume():
    """
    The key / valued object of all resource files returned as a JSON-ifed response.

    Returns:
        Response: The JSON-ified response of all resource files.
    """
    return jsonify({name: _resource(name) for name in RESOURCE_ENDPOINTS})


@api.route('/career', methods=['GET'])
def career():
    """
    Returns the json found in career.json.

    Returns:
        Response: The JSON-ified file wrapped in a Response object.
    """
    return jsonify(_resource('career'))


@api.route('/education', methods=['GET'])
def education():
    """
    Returns the json found in education.json.

    Returns:
        Response: The JSON-ified file wrapped in a Response object.
    """
    return jsonify(_resource('education'))


@api.route('/leadership', methods=['GET'])
def leadership():
    """
    Returns the json found in leadership.json.

    Returns:
        Response: The JSON-ified file wrapped in a Response object.
    """
    return jsonify(_resource('leadership'))


@api.route('/repos', methods=['GET'])
def repos():
    """
    Returns the json found in repos.json.

    Returns:
        Response: The JSON-ified file wrapped in a Response object.
    """
    return jsonify(_resource('repos'))


@api.route('/skills', methods=['GET'])
def skills():
    """
    Returns the json found in skills.json.

    Returns:
        Response: The JSON-ified file wrapped in a Response object.
    """
    return jsonify(_resource('skills'))
