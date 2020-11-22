from flask import (
    Flask,
    render_template,
    redirect
)


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    @app.route('/', methods=["GET"])
    def home():
        """The index / home route of the website"""
        return render_template('home.html')

    @app.route('/github', methods=["GET"])
    def github():
        """This route redirects to my github"""
        return redirect('https://github.com/santosderek')

    @app.route('/linkedin', methods=["GET"])
    def linkedin():
        """This route redirects to my linkedin"""
        return redirect('https://www.linkedin.com/in/santosderek/')

    return app
