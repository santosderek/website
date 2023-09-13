from os.path import exists

from website.resume import RESUME_LOCATION, generate_document


def test_generate_document():
    generate_document(RESUME_LOCATION)
    assert exists(RESUME_LOCATION)
