from flask import (
    Flask,
    render_template,
    redirect
)
import json
import requests

GITHUB_REPO_LIST_URL = 'https://api.github.com/users/santosderek/repos?page={number}'
GITHUB_USER_URL = 'https://api.github.com/users/santosderek'

class GithubRequestError(Exception):
    pass


def get_github_repos():
    """Requests from the GITHUB API my user data and returns as JSON(Dict)"""
    returned_value = requests.get(GITHUB_USER_URL)

    if returned_value.status_code != 200:
        raise GithubRequestError("Error Code != 200")

    return returned_value.json()

def get_career_json(): 
    """ Get the career JSON file that holds all information of my career."""
    with open('website/resources/career.json', 'r') as current_file: 
        data = json.loads(current_file.read())
        return data

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    @app.route('/', methods=["GET"])
    def home():
        """The index / home route of the website"""

        # Technology, Stars out of 5
        technologies = [
            ('Python', 5),
            ('Java', 5),
            ('C++', 5),
            ('CSS', 5),
            ('Javascript', 5),
            ('Git', 5),
            ('Docker', 5),
            ('LXC / LXD', 5),
            ('Ansible', 4),
            ('Open Computer Vision', 4),
            ('NGINX', 4),
            ('Flask', 5),
            ('Github', 5),
            ('Gitlab', 5),
            ('Elasticsearch', 3),
            ('Kibana', 3),
            ('Logstash', 3),
            ('REST APIs', 5),
            ('JSON', 5),
            ('YAML', 5),
            ('Kubernetes', 4),
            ('Object Orientated Programming', 4),
            ('UML', 4),
            ('MVC Pattern', 4),
        ]
        tools = [
            ('Proxmox', 5),
            ('Debian', 5),
            ('Ubuntu', 5),
            ('Visual Studio 2019', 4),
            ('Manjaro', 5),
            ('Windows', 5),
            ('VSCode', 5),
            ('VMWare ESXI', 4)
        ]

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
            github_user_json = get_github_repos()
        except GithubRequestError as e:
            github_user_json = {}

        # Get career info from JSON file
        careers = get_career_json()

        return render_template('home.html',
                               technologies_left=technologies_left,
                               technologies_right=technologies_right,
                               tools_left=tools_left,
                               tools_right=tools_right,
                               github_user_json=github_user_json,
                               careers=careers)

    @app.route('/github', methods=["GET"])
    def github():
        """This route redirects to my github"""
        return redirect('https://github.com/santosderek')

    @app.route('/linkedin', methods=["GET"])
    def linkedin():
        """This route redirects to my linkedin"""
        return redirect('https://www.linkedin.com/in/santosderek/')

    return app
