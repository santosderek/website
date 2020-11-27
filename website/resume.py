"""Generating a DOCX and converting it to .pdf through python"""
from docx import Document
from os.path import join
DOWNLOAD_LOCATION = r'C:\Users\derek\Desktop\Derek Santos - Resume.docx'


def generate_document():

    document = Document()

    document.add_heading('Derek Santos', 0)

    subtitle = document.add_heading(
        'santosderek.com | Raleigh NC, 27603 | santos.jon.derek@gmail.com')

    document.add_heading('Technical Skills', level=1)

    document.save(DOWNLOAD_LOCATION)


if __name__ == "__main__":
    generate_document()
