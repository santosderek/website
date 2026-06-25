from flask import Blueprint, abort, current_app, send_from_directory

backend_blueprint = Blueprint('backend', __name__)


@backend_blueprint.route('/resume', methods=["GET"])
def resume():
    """Return a download of the generated resume."""
    try:
        return send_from_directory(
            current_app.config['RESUME_DIRECTORY_LOCATION'],
            path=current_app.config['RESUME_FILENAME'],
            as_attachment=True,
        )
    except FileNotFoundError:
        abort(404)
