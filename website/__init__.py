from .resources import get_resource_json, GithubRequestError, get_github_user
from .resume import (
    generate_document,
    RESUME_DIRECTORY_LOCATION,
    RESUME_FILENAME,
    RESUME_LOCATION)
from flask import (
    Flask,
    render_template,
    redirect,
    escape,
    send_from_directory,
    abort
)
from jinja2.exceptions import TemplateNotFound
from os.path import exists


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    app.logger.info("Creating the resume.")
    generate_document(RESUME_LOCATION)
    assert exists(RESUME_LOCATION)
    app.logger.info("Resume Created.")

    @app.route('/', methods=["GET"])
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

    @app.route('/resume', methods=["GET"])
    def resume():
        """This route returns a download of my resume."""

        try:
            # return send_from_directory(RESUME_DIRECTORY_LOCATION, path=RESUME_FILENAME, filename=RESUME_FILENAME, as_attachment=True)
            return send_from_directory(RESUME_DIRECTORY_LOCATION, path=RESUME_FILENAME, as_attachment=True)
        except FileNotFoundError:
            abort(404)

    @app.route('/project/<string:project>', methods=["GET"])
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

    @app.route('/github', methods=["GET"])
    def github():
        """This route redirects to my github"""
        return redirect('https://github.com/santosderek')

    @app.route('/linkedin', methods=["GET"])
    def linkedin():
        """This route redirects to my linkedin"""
        return redirect('https://www.linkedin.com/in/santosderek/')

    @app.errorhandler(404)
    def page_not_found(e):
        """HTTP Error 404: Not found."""
        return render_template("error/404.html"), 404

    app.logger.info("Application Created.")
    return app
