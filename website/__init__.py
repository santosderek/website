from flask import (
    Flask,
    render_template
)


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    @app.route('/', methods=["GET"])
    def home():
        """The index / home route of the website"""
        return render_template('home.html')

    return app
