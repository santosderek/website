from flask import jsonify
from website.resources import get_resource_json

from . import api


@api.route('/resume', methods=['GET'])
def resume():
    """
    The key / valued object of all resource files returned as a JSON-ifed response.

    Returns:
        Response: The JSON-ified response of all resource files.
    """
    return jsonify(
        {
            'career': get_resource_json('career.json'),
            'education': get_resource_json('education.json'),
            'leadership': get_resource_json('leadership.json'),
            'repos': get_resource_json('repos.json'),
            'skills': get_resource_json('skills.json'),
        }
    )

@api.route('/career', methods=['GET'])
def career():
    """
    Returns the json found in career.json.

    Returns:
        Response: The JSON-ified file wrapped in a Response object.
    """
    return jsonify(get_resource_json('career.json'))


@api.route('/education', methods=['GET'])
def education():
    """
    Returns the json found in education.json.

    Returns:
        Response: The JSON-ified file wrapped in a Response object.
    """
    return jsonify(get_resource_json('education.json'))


@api.route('/leadership', methods=['GET'])
def leadership():
    """
    Returns the json found in leadership.json.

    Returns:
        Response: The JSON-ified file wrapped in a Response object.
    """
    return jsonify(get_resource_json('leadership.json'))


@api.route('/repos', methods=['GET'])
def repos():
    """
    Returns the json found in repos.json.

    Returns:
        Response: The JSON-ified file wrapped in a Response object.
    """
    return jsonify(get_resource_json('repos.json'))


@api.route('/skills', methods=['GET'])
def skills():
    """
    Returns the json found in skills.json.

    Returns:
        Response: The JSON-ified file wrapped in a Response object.
    """
    return jsonify(get_resource_json('skills.json'))
