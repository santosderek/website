"""Generating a DOCX and converting it to .pdf through python"""
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.shared import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor, Cm, Inches

from os.path import expanduser, join
from . import get_resource_json

DOWNLOAD_LOCATION = join(expanduser('~'), 'Derek Santos - Resume.docx')
DEFAULT_SPACING = Cm(0.01)
DEFAULT_FONT_NAME = "Crimson Text"
DEFAULT_FONT_SIZE_TITLE = Pt(20)
DEFAULT_FONT_SIZE_SUBTITLE = Pt(10)
DEFAULT_FONT_SIZE_HEADING = Pt(12)
DEFAULT_FONT_SIZE_TEXT = Pt(9)
DEFAULT_TOP_MARGIN_LENGTH = Cm(1)
DEFAULT_BOTTOM_MARGIN_LENGTH = Cm(1)
DEFAULT_LEFT_MARGIN_LENGTH = Inches(.75)
DEFAULT_RIGHT_MARGIN_LENGTH = Inches(.75)


def insertHR(paragraph):
    p = paragraph._p  # p is the <w:p> XML element
    pPr = p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    pPr.insert_element_before(pBdr,
                              'w:shd', 'w:tabs', 'w:suppressAutoHyphens', 'w:kinsoku', 'w:wordWrap',
                              'w:overflowPunct', 'w:topLinePunct', 'w:autoSpaceDE', 'w:autoSpaceDN',
                              'w:bidi', 'w:adjustRightInd', 'w:snapToGrid', 'w:spacing', 'w:ind',
                              'w:contextualSpacing', 'w:mirrorIndents', 'w:suppressOverlap', 'w:jc',
                              'w:textDirection', 'w:textAlignment', 'w:textboxTightWrap',
                              'w:outlineLvl', 'w:divId', 'w:cnfStyle', 'w:rPr', 'w:sectPr',
                              'w:pPrChange'
                              )
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '6')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), 'auto')
    pBdr.append(bottom)


def generate_document(location=DOWNLOAD_LOCATION):
    """Generate a word document based off the resource documents JSON"""
    # Document Wide Formatting
    document = Document()

    sections = document.sections
    for section in sections:
        section.top_margin = DEFAULT_TOP_MARGIN_LENGTH
        section.bottom_margin = DEFAULT_BOTTOM_MARGIN_LENGTH
        section.left_margin = DEFAULT_LEFT_MARGIN_LENGTH
        section.right_margin = DEFAULT_RIGHT_MARGIN_LENGTH

    # Style -> Title
    style = document.styles.add_style('ResumeTitle', WD_STYLE_TYPE.PARAGRAPH)
    font = style.font
    font.name = DEFAULT_FONT_NAME
    font.size = DEFAULT_FONT_SIZE_TITLE
    font.color.rgb = RGBColor(0, 0, 0)
    formatting = style.paragraph_format
    formatting.alignment = WD_ALIGN_PARAGRAPH.CENTER
    formatting.space_before = DEFAULT_SPACING
    formatting.space_after = DEFAULT_SPACING

    # Style -> Subtitle
    style = document.styles.add_style(
        'ResumeSubtitle', WD_STYLE_TYPE.PARAGRAPH)
    font = style.font
    font.name = DEFAULT_FONT_NAME
    font.size = DEFAULT_FONT_SIZE_SUBTITLE
    font.color.rgb = RGBColor(0, 0, 0)
    formatting = style.paragraph_format
    formatting.alignment = WD_ALIGN_PARAGRAPH.CENTER
    formatting.space_before = DEFAULT_SPACING
    formatting.space_after = DEFAULT_SPACING

    # Style -> Normal
    style = document.styles['Normal']
    font = style.font
    font.name = DEFAULT_FONT_NAME
    font.size = DEFAULT_FONT_SIZE_TEXT
    font.color.rgb = RGBColor(0, 0, 0)
    formatting = style.paragraph_format
    formatting.space_before = DEFAULT_SPACING
    formatting.space_after = DEFAULT_SPACING

    # Style -> Header
    style = document.styles.add_style(
        'ResumeHeader', WD_STYLE_TYPE.PARAGRAPH)
    font = style.font
    font.name = DEFAULT_FONT_NAME
    font.size = DEFAULT_FONT_SIZE_HEADING
    font.bold = True
    font.color.rgb = RGBColor(0, 0, 0)
    formatting = style.paragraph_format
    formatting.space_before = DEFAULT_SPACING
    formatting.space_after = DEFAULT_SPACING

    # Style -> List Bullet
    style = document.styles['List Bullet']
    font = style.font
    font.name = DEFAULT_FONT_NAME
    font.size = DEFAULT_FONT_SIZE_TEXT
    font.color.rgb = RGBColor(0, 0, 0)
    formatting = style.paragraph_format
    formatting.space_before = DEFAULT_SPACING
    formatting.space_after = DEFAULT_SPACING
    formatting.left_indent = Inches(0.5)

    # Style -> Emphasis
    style = document.styles['Emphasis']
    font = style.font
    font.name = DEFAULT_FONT_NAME
    font.size = DEFAULT_FONT_SIZE_TEXT
    font.color.rgb = RGBColor(84, 84, 84)

    # Title and sub-heading
    document.add_paragraph('Derek Santos', style='ResumeTitle')
    subtitle = document.add_paragraph('santosderek.com | Raleigh, NC | santos.jon.derek@gmail.com',
                                      style='ResumeSubtitle')

    # Technical Skills Section
    head = document.add_paragraph('Technical Skills',
                                  style='ResumeHeader')
    insertHR(head)
    # Technologies
    document.add_paragraph('').add_run('Technologies').bold = True
    technologies = document.add_paragraph('')
    skills_json = get_resource_json('skills.json')
    technology_list = skills_json['technologies']
    technology_list.sort(key=lambda x: x[1], reverse=True)
    for pos, item in enumerate(technology_list):
        if pos != 0:
            technologies.add_run(', ')
        technologies.add_run('{}'.format(item[0]))
    # Tools
    document.add_paragraph('').add_run('Tools:').bold = True
    tools = document.add_paragraph('')
    tools_list = skills_json['tools']
    tools_list.sort(key=lambda x: x[1], reverse=True)
    for pos, item in enumerate(tools_list):
        if pos != 0:
            tools.add_run(', ')
        tools.add_run('{}'.format(item[0]))

    # Experiences Section
    head = document.add_paragraph('Experience',
                                  style='ResumeHeader')
    insertHR(head)
    experiences = get_resource_json("career.json")
    for experience in experiences:
        experience_paragraph = document.add_paragraph('')
        experience_paragraph.add_run(
            '{}'.format(experience['title'])).bold = True
        for pos, tech in enumerate(experience['technologies']):
            if pos != 0:
                experience_paragraph.add_run(',', 'Emphasis')
            subtext = experience_paragraph.add_run(' {}'.format(tech),
                                                   'Emphasis')
        experience_paragraph.add_run(' {}'.format(experience['date']),
                                     'Emphasis').bold = True
        # experience bullet points - Has to be on its own paragraph
        for bullet in experience['descriptions']:
            document.add_paragraph(bullet, style='List Bullet')

    # Leadership
    head = document.add_paragraph('Leadership',
                                  style='ResumeHeader')
    insertHR(head)
    for item in get_resource_json('leadership.json'):
        leadership_paragraph = document.add_paragraph('')
        leadership_paragraph.add_run(item['title']).bold = True
        leadership_paragraph.add_run(' ' + item['location'],
                                     'Emphasis')
        date = leadership_paragraph.add_run(' ' + item['date'],
                                            'Emphasis')
        date.italic = True
        date.bold = True
        for line in item['description']:
            document.add_paragraph(line, style='List Bullet')

    # Education
    head = document.add_paragraph('Education',
                                  style='ResumeHeader')
    insertHR(head)
    for item in get_resource_json('education.json'):
        title_line = document.add_paragraph('')
        title_line.add_run(item['title']).bold = True
        date = title_line.add_run(' ' + item['date'],
                                  'Emphasis')
        date.italic = True
        date.bold = True
        document.add_paragraph(item['degree'])

    document.save(DOWNLOAD_LOCATION)


if __name__ == "__main__":
    generate_document()
