from website.resume import generate_document, DOWNLOAD_LOCATION
from os.path import exists
import pytest


def test_generate_document(): 
    generate_document(DOWNLOAD_LOCATION)

    assert exists(DOWNLOAD_LOCATION)
