"""Generating a DOCX and converting it to .pdf through python"""
from docx import Document
from os.path import expanduser, join

from .website import get_resource_json

DOWNLOAD_LOCATION = join(expanduser('~'), 'Derek Santos - Resume.docx')


def generate_document():

    document = Document()

    document.add_heading('Derek Santos', 0)

    subtitle = document.add_heading(
        'santosderek.com | Raleigh NC, 27603 | santos.jon.derek@gmail.com')

    document.add_heading('Technical Skills', level=1)

    technologies = document.add_paragraph('')
    technologies.add_run('Technologies').bold = True

    for item in get_resource_json():
        technologies.add_run('{}, '.format(item))

    document.save(DOWNLOAD_LOCATION)


if __name__ == "__main__":
    generate_document()
