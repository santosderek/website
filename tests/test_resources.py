import json
from pathlib import Path

import pytest

from website.resources import get_resource_json


def test_get_resource_json_loads_from_package_when_cwd_changes(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)

    returned_value = get_resource_json('career.json')

    assert isinstance(returned_value, list)
    assert len(returned_value) > 0


def test_get_resource_json_can_use_explicit_directory(tmp_path):
    resource_file = tmp_path / 'custom.json'
    resource_file.write_text(json.dumps({'hello': 'world'}), encoding='utf-8')

    assert get_resource_json('custom.json', resource_directory=tmp_path) == {'hello': 'world'}


def test_get_resource_json_rejects_path_traversal(tmp_path):
    with pytest.raises(ValueError, match='Invalid resource filename'):
        get_resource_json('../settings.py', resource_directory=tmp_path)


@pytest.mark.parametrize('filename', ['/tmp/example.json', 'nested/example.json', 'not-json.txt'])
def test_get_resource_json_rejects_non_simple_json_filenames(filename, tmp_path):
    with pytest.raises(ValueError, match='Invalid resource filename'):
        get_resource_json(filename, resource_directory=tmp_path)


def test_get_resource_json_raises_clear_missing_file_error(tmp_path):
    with pytest.raises(FileNotFoundError, match='Resource JSON file not found'):
        get_resource_json('missing.json', resource_directory=tmp_path)


def test_get_resource_json_raises_clear_invalid_json_error(tmp_path):
    resource_file = tmp_path / 'invalid.json'
    resource_file.write_text('{not valid json', encoding='utf-8')

    with pytest.raises(ValueError, match='Invalid JSON in resource file'):
        get_resource_json(resource_file.name, resource_directory=tmp_path)
