from flask import (
    Flask,
    render_template
    )


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

    @app.route('/', methods=["GET"])
    def home():
        return render_template('home.html')

    @app.route('/projects', methods=["GET"])
    def projects():
        return render_template('projects.html')

    @app.route('/experience', methods=["GET"])
    def experience():
        return render_template('experience.html')

    @app.route('/contact', methods=["GET"])
    def contact():
        return render_template('contact.html')

    return app
