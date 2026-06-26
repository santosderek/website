"""Helpers for loading JSON resources bundled with the website."""
import json
from pathlib import Path
from typing import Any, Optional, Union

from flask import current_app, has_app_context

from .settings import DEFAULT_RESOURCE_DIRECTORY


PathLike = Union[str, Path]


def _resource_directory(resource_directory: Optional[PathLike] = None) -> Path:
    if resource_directory is not None:
        return Path(resource_directory)

    if has_app_context():
        configured_directory = current_app.config.get('RESOURCE_DIRECTORY')
        if configured_directory:
            return Path(configured_directory)

    return DEFAULT_RESOURCE_DIRECTORY


def _safe_resource_path(filename: str, resource_directory: Optional[PathLike] = None) -> Path:
    requested = Path(filename)
    if requested.is_absolute() or requested.name != filename or requested.suffix != '.json':
        raise ValueError(f"Invalid resource filename: {filename!r}")

    base_directory = _resource_directory(resource_directory).resolve()
    resource_path = (base_directory / requested).resolve()

    if resource_path.parent != base_directory:
        raise ValueError(f"Invalid resource filename: {filename!r}")

    return resource_path


def get_resource_json(filename: str, resource_directory: Optional[PathLike] = None) -> Any:
    """Return the contents of a resource JSON file.

    Resource files are loaded from the configured resource directory using UTF-8
    encoding. Only simple JSON filenames are accepted so callers cannot traverse
    outside the resource directory.
    """
    resource_path = _safe_resource_path(filename, resource_directory)

    try:
        with resource_path.open('r', encoding='utf-8') as current_file:
            return json.load(current_file)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Resource JSON file not found: {resource_path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in resource file: {resource_path}") from exc
