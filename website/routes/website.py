from flask import Blueprint, abort, current_app, redirect, send_from_directory

from website.spa import send_spa_index

website_blueprint = Blueprint(
    'website',
    __name__,
    static_folder='../static'
)

PROJECT_PAGES = ('project', 'santosderek', 'vitality')


@website_blueprint.route('/robots.txt', methods=["GET"])
def robots():
    """A file for search engines."""
    return send_from_directory('static/txt', 'robots.txt')


@website_blueprint.route('/', methods=["GET"])
def home():
    """Serve the React Router single-page app."""
    return send_spa_index()


@website_blueprint.route('/resume', methods=["GET"])
def resume():
    """This route returns a download of my resume."""

    try:
        return send_from_directory(
            current_app.config['RESUME_DIRECTORY_LOCATION'],
            path=current_app.config['RESUME_FILENAME'],
            as_attachment=True,
        )
    except FileNotFoundError:
        abort(404)


@website_blueprint.route('/project/<string:project>', methods=["GET"])
def project(project: str):
    """This route renders project pages."""

    if project not in PROJECT_PAGES:
        abort(404)

    return send_spa_index()


@website_blueprint.route('/github', methods=["GET"])
def github():
    """This route redirects to my github"""
    return redirect('https://github.com/santosderek')


@website_blueprint.route('/linkedin', methods=["GET"])
def linkedin():
    """This route redirects to my linkedin"""
    return redirect('https://www.linkedin.com/in/santosderek/')
