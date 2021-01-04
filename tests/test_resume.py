from website.resume import generate_document, RESUME_LOCATION
from os.path import exists
import pytest


def test_generate_document(): 
    generate_document(RESUME_LOCATION)
    assert exists(RESUME_LOCATION)
