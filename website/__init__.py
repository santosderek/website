from os.path import exists

from flask import Flask, render_template

from .api.v1 import api
from .resume import RESUME_LOCATION, generate_document
from .routes.website import website_blueprint
from .sitemap import sitemap


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

    app.logger.info("Creating the resume.")
    generate_document(RESUME_LOCATION)
    assert exists(RESUME_LOCATION)
    app.logger.info("Resume Created.")

    app.register_blueprint(website_blueprint)
    app.register_blueprint(api)

    sitemap.init_app(app)

    @app.errorhandler(404)
    def page_not_found(e):
        """HTTP Error 404: Not found."""
        return render_template("error/404.html"), 404

    app.logger.info("Application Created.")
    return app
