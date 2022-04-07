from flask import (Blueprint, abort, escape, redirect, render_template,
                   send_from_directory)
from jinja2.exceptions import TemplateNotFound

from website.resources import get_resource_json
from website.resume import RESUME_DIRECTORY_LOCATION, RESUME_FILENAME
from website.connectors.github import GitHubConnector

website_blueprint = Blueprint(
    'website',
     __name__, 
     template_folder='../templates/website', # NOTE: Relative to blueprints root path
     static_folder='../static'
     )

@website_blueprint.route('/', methods=["GET"])
def home():
    """The home route of the website"""

    # Technology, Stars out of 5
    skills = get_resource_json('skills.json')
    technologies = skills['technologies']
    tools = skills['tools']

    # Get career info from JSON file
    careers = get_resource_json('career.json')
    educations = get_resource_json('education.json')
    repos = get_resource_json('repos.json')

    # Sorting lists by number of stars decending
    technologies.sort(key=lambda x: x[1], reverse=True)
    tools.sort(key=lambda x: x[1], reverse=True)

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
        # return send_from_directory(RESUME_DIRECTORY_LOCATION, path=RESUME_FILENAME, filename=RESUME_FILENAME, as_attachment=True)
        return send_from_directory(RESUME_DIRECTORY_LOCATION, path=RESUME_FILENAME, as_attachment=True)
    except FileNotFoundError:
        abort(404)


@website_blueprint.route('/project/<string:project>', methods=["GET"])
def project(project: str):
    """This route redirects to my github"""

    imagesToPreload = {
        'vitality': ['/static/images/vitality/FrontPage.png',
                     '/static/images/vitality/ShowTrainers.png',
                     '/static/images/vitality/Diets.png',
                     '/static/images/vitality/Workouts.png'],
        'santosderek': ['/static/images/santosderek/santosderekDeployment.png']
    }

    try:
        project = escape(project)

        images = ['/static/images/santosderek.png']
        if project in imagesToPreload:
            images += imagesToPreload[project]

        return render_template(f'project/{project}.html', imagesToPreload=images)
    except TemplateNotFound:
        abort(404)


@website_blueprint.route('/github', methods=["GET"])
def github():
    """This route redirects to my github"""
    return redirect('https://github.com/santosderek')


@website_blueprint.route('/linkedin', methods=["GET"])
def linkedin():
    """This route redirects to my linkedin"""
    return redirect('https://www.linkedin.com/in/santosderek/')
