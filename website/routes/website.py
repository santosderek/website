from flask import Blueprint, abort, current_app, redirect, render_template, send_from_directory

from website.connectors.github import GitHubConnector
from website.resources import get_resource_json

website_blueprint = Blueprint(
    'website',
    __name__,
    # NOTE: Relative to blueprints root path
    template_folder='../templates/website',
    static_folder='../static'
)

PROJECT_PAGES = {
    'project': {
        'template': 'project/project.html',
        'images': [],
    },
    'santosderek': {
        'template': 'project/santosderek.html',
        'images': ['/static/images/santosderek/santosderekDeployment.png'],
    },
    'vitality': {
        'template': 'project/vitality.html',
        'images': [
            '/static/images/vitality/FrontPage.png',
            '/static/images/vitality/ShowTrainers.png',
            '/static/images/vitality/Diets.png',
            '/static/images/vitality/Workouts.png',
        ],
    },
}


@website_blueprint.route('/robots.txt', methods=["GET"])
def robots():
    """A file for search engines."""
    return send_from_directory('static/txt', 'robots.txt')


@website_blueprint.route('/', methods=["GET"])
def home():
    """The home route of the website"""

    # Technology, Stars out of 5
    skills = get_resource_json('skills.json')
    technologies = sorted(skills['technologies'], key=lambda x: x[1], reverse=True)
    tools = sorted(skills['tools'], key=lambda x: x[1], reverse=True)

    # Get career info from JSON file
    careers = get_resource_json('career.json')
    educations = get_resource_json('education.json')
    repos = get_resource_json('repos.json')

    # Splitting to two columns
    technologies_left = technologies[:len(technologies) // 2]
    technologies_right = technologies[len(technologies) // 2:]
    tools_left = tools[:len(tools) // 2]
    tools_right = tools[len(tools) // 2:]

    # Get my github public info
    github_user_json = GitHubConnector().user

    return render_template('home.html',
                           technologies_left=technologies_left,
                           technologies_right=technologies_right,
                           tools_left=tools_left,
                           tools_right=tools_right,
                           github_user_json=github_user_json,
                           careers=careers,
                           educations=educations,
                           repos=repos)


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

    project_page = PROJECT_PAGES.get(project)
    if project_page is None:
        abort(404)

    images = ['/static/images/santosderek.png', *project_page['images']]
    return render_template(project_page['template'], imagesToPreload=images)


@website_blueprint.route('/github', methods=["GET"])
def github():
    """This route redirects to my github"""
    return redirect('https://github.com/santosderek')


@website_blueprint.route('/linkedin', methods=["GET"])
def linkedin():
    """This route redirects to my linkedin"""
    return redirect('https://www.linkedin.com/in/santosderek/')
