from flask import (
    Flask,
    render_template,
    redirect, 
    request,
    escape
)
import json
import requests

GITHUB_REPO_LIST_URL = 'https://api.github.com/users/santosderek/repos?page={number}'
GITHUB_USER_URL = 'https://api.github.com/users/santosderek'


class GithubRequestError(Exception):
    pass


def get_github_user():
    """Requests from the GITHUB API my user data and returns as JSON(Dict)"""
    returned_value = requests.get(GITHUB_USER_URL)

    if returned_value.status_code != 200:
        raise GithubRequestError("Error Code != 200")

    return returned_value.json()


def get_resource_json(filename: str):
    "Return the contents of a resource JSON file."
    with open(f'website/resources/{filename}', 'r') as current_file:
        data = json.loads(current_file.read())
        return data


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    @app.route('/', methods=["GET"])
    def home():
        """The index / home route of the website"""

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
        github_user_json = {}
        try:
            github_user_json = get_github_user()
        except GithubRequestError:
            github_user_json = {}

        return render_template('home.html',
                               technologies_left=technologies_left,
                               technologies_right=technologies_right,
                               tools_left=tools_left,
                               tools_right=tools_right,
                               github_user_json=github_user_json,
                               careers=careers,
                               educations=educations,
                               repos=repos)

    @app.route('/project/<string:project>', methods=["GET"])
    def project(project: str):
        """This route redirects to my github"""

        project = escape(project)
        return render_template(f'project/{project}.html')

    @app.route('/github', methods=["GET"])
    def github():
        """This route redirects to my github"""
        return redirect('https://github.com/santosderek')

    @app.route('/linkedin', methods=["GET"])
    def linkedin():
        """This route redirects to my linkedin"""
        return redirect('https://www.linkedin.com/in/santosderek/')

    return app
