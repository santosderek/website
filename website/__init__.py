from pathlib import Path

from flask import Flask

from .api.v1 import api
from .resume import generate_document
from .routes.website import website_blueprint
from .sitemap import sitemap


def create_app(config_overrides=None):
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')
    if config_overrides:
        app.config.update(config_overrides)

    directory_or_filename_overridden = bool(
        config_overrides
        and 'RESUME_LOCATION' not in config_overrides
        and (
            'RESUME_DIRECTORY_LOCATION' in config_overrides
            or 'RESUME_FILENAME' in config_overrides
        )
    )
    if directory_or_filename_overridden:
        resume_location = Path(app.config['RESUME_DIRECTORY_LOCATION']) / app.config['RESUME_FILENAME']
        app.config['RESUME_LOCATION'] = str(resume_location)
    else:
        resume_location = Path(app.config['RESUME_LOCATION'])
        app.config['RESUME_DIRECTORY_LOCATION'] = str(resume_location.parent)
        app.config['RESUME_FILENAME'] = resume_location.name

    if app.config.get('GENERATE_RESUME_ON_STARTUP', True):
        app.logger.info("Creating the resume.")
        try:
            with app.app_context():
                generated_location = generate_document(resume_location)
        except Exception as exc:  # pragma: no cover - exact logging path is runtime-only
            raise RuntimeError(f"Unable to generate resume at {resume_location}") from exc

        if not Path(generated_location).exists():
            raise RuntimeError(f"Resume was not created at {generated_location}")
        app.logger.info("Resume Created.")

    app.register_blueprint(website_blueprint)
    app.register_blueprint(api)

    sitemap.init_app(app)

    @app.errorhandler(404)
    def page_not_found(e):
        """HTTP Error 404: Not found."""
        return '<p class="text-center">Sorry! Could not find page!</p>', 404

    app.logger.info("Application Created.")
    return app
