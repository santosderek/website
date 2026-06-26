from pathlib import Path

from website import create_app
from website.resume import RESUME_FILENAME, RESUME_LOCATION, generate_document


def test_generate_document_writes_requested_location(tmp_path):
    output_path = tmp_path / 'nested' / RESUME_FILENAME

    returned_path = generate_document(output_path)

    assert returned_path == output_path
    assert output_path.exists()
    assert output_path.stat().st_size > 0


def test_generate_document_does_not_write_default_when_custom_location_used(tmp_path, monkeypatch):
    default_path = tmp_path / 'default' / RESUME_FILENAME
    custom_path = tmp_path / 'custom' / RESUME_FILENAME
    monkeypatch.setattr('website.resume.RESUME_LOCATION', str(default_path))

    generate_document(custom_path)

    assert custom_path.exists()
    assert not default_path.exists()


def test_create_app_generates_resume_on_startup_when_enabled(tmp_path, monkeypatch):
    monkeypatch.setattr('website.connectors.github.requests.get', lambda **kwargs: None)
    resume_location = tmp_path / 'startup' / RESUME_FILENAME

    create_app({
        'TESTING': True,
        'GENERATE_RESUME_ON_STARTUP': True,
        'RESUME_LOCATION': str(resume_location),
    })

    assert resume_location.exists()


def test_create_app_does_not_generate_resume_on_startup_when_disabled(tmp_path):
    resume_location = tmp_path / 'startup-disabled' / RESUME_FILENAME

    create_app({
        'TESTING': True,
        'GENERATE_RESUME_ON_STARTUP': False,
        'RESUME_LOCATION': str(resume_location),
    })

    assert not resume_location.exists()


def test_create_app_normalizes_resume_location_from_environment(tmp_path, monkeypatch):
    resume_location = tmp_path / 'env' / 'custom-resume.docx'
    monkeypatch.setenv('RESUME_LOCATION', str(resume_location))

    app = create_app({
        'TESTING': True,
        'GENERATE_RESUME_ON_STARTUP': False,
    })

    assert Path(app.config['RESUME_LOCATION']) == resume_location
    assert Path(app.config['RESUME_DIRECTORY_LOCATION']) == resume_location.parent
    assert app.config['RESUME_FILENAME'] == resume_location.name


def test_default_resume_location_is_still_defined():
    assert Path(RESUME_LOCATION).name == RESUME_FILENAME
