from docx import Document

# Iterate through a document and give back all headings
def iterate_headings(paragraphs):
    for paragraph in paragraphs:
        if paragraph.style.name.startswith('Heading 2'):
            yield paragraph

# Opening a document
document = Document('atbs.docx')

for heading in iterate_headings(document.paragraphs):
    print heading.text

document.save('test.docx')
