from flask import jsonify

from website.connectors.github import GitHubConnector

from . import api


@api.route('/github/user', methods=['GET'])
def github_user():
    """Return public GitHub profile data used by the React frontend."""
    return jsonify(GitHubConnector().user)
