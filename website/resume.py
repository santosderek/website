"""Generating a DOCX and converting it to .pdf through python"""
from docx import Document
from os.path import expanduser, join
from . import get_resource_json

DOWNLOAD_LOCATION = join(expanduser('~'), 'Derek Santos - Resume.docx')


def generate_document(location=DOWNLOAD_LOCATION):

    document = Document()

    document.add_heading('Derek Santos', 0)

    subtitle = document.add_heading(
        'santosderek.com | Raleigh, NC | santos.jon.derek@gmail.com')

    # Technical Skills Section
    document.add_heading('Technical Skills', level=1)
    technologies = document.add_paragraph('')
    technologies.add_run('Technologies').bold = True
    skills_json = get_resource_json('skills.json')
    technology_list = skills_json['technologies']
    technology_list.sort(key=lambda x: x[1], reverse=True)
    for pos, item in enumerate(technology_list):
        if pos == 0:
            technologies.add_run(': ').bold = True
        else:
            technologies.add_run(', ')
        technologies.add_run('{}'.format(item[0]))
    tools = document.add_paragraph('')
    tools.add_run('Tools').bold = True
    tools_list = skills_json['tools']
    tools_list.sort(key=lambda x: x[1], reverse=True)
    for pos, item in enumerate(tools_list):
        if pos == 0:
            tools.add_run(': ').bold = True
        else:
            tools.add_run(', ')
        tools.add_run('{}'.format(item[0]))

    # Experiences Section
    document.add_heading('Experience', level=1)
    experiences = get_resource_json("career.json")

    for experience in experiences:
        experience_paragraph = document.add_paragraph('')
        experience_paragraph.add_run('{}'.format(experience['title'])).bold = True
        for pos, tech in enumerate(experience['technologies']):
            if pos == 0:
                experience_paragraph.add_run(',')
            experience_paragraph.add_run(' {}'.format(tech))

        experience_paragraph.add_run(
            ' {}\n'.format(experience['date'])).italic = True

        # experience bullet points - Has to be on its own paragraph
        for bullet in experience['descriptions']:
            document.add_paragraph(bullet, style='List Continue')

    # Leadership

    document.add_heading('Leadership', level=1)
    for item in get_resource_json('leadership.json'):
        leadership_paragraph = document.add_paragraph('')
        leadership_paragraph.add_run(item['title']).bold = True
        leadership_paragraph.add_run(' ' + item['date']).italic = True
        document.add_paragraph(item['location'])
        for line in item['description']:
            document.add_paragraph(line, style='List Continue')

    # Education
    document.add_heading('Education', level=1)
    for item in get_resource_json('education.json'):
        title_line = document.add_paragraph('')
        title_line.add_run(item['title']).bold = True
        title_line.add_run(' ' + item['date']).italic = True
        document.add_paragraph(item['degree'])

    document.save(DOWNLOAD_LOCATION)


if __name__ == "__main__":
    generate_document()
