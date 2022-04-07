from .resume import generate_document, RESUME_LOCATION
from flask import Flask, render_template
from os.path import exists
from .routes.website import website_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    app.logger.info("Creating the resume.")
    generate_document(RESUME_LOCATION)
    assert exists(RESUME_LOCATION)
    app.logger.info("Resume Created.")

    app.register_blueprint(website_blueprint)

    @app.errorhandler(404)
    def page_not_found(e):
        """HTTP Error 404: Not found."""
        return render_template("error/404.html"), 404

    app.logger.info("Application Created.")
    return app
