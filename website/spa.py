"""Helpers for serving the built React single-page app."""
from pathlib import Path

from flask import abort, current_app, send_from_directory


def send_spa_index():
    """Serve the built React app shell.

    The frontend build is produced by Vite into ``website/static/spa`` by
    default. Tests can override ``SPA_DIST_DIR`` with a temporary fixture.
    """
    spa_dist_dir = Path(current_app.config['SPA_DIST_DIR'])
    index_file = spa_dist_dir / 'index.html'
    if not index_file.exists():
        current_app.logger.error("React app build not found at %s", index_file)
        abort(503)

    return send_from_directory(spa_dist_dir, 'index.html')
