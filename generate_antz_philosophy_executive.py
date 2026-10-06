from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak

BASE_DIR = Path("/Users/Eugin/Documents/Claude File/Antz Logo Philosophy Document")
ICON_DIR = BASE_DIR / "reference" / "icon_elements"
OUTPUT = BASE_DIR / "Antz_Logo_Philosophy_Document_Executive.pdf"

styles = getSampleStyleSheet()

styles.add(ParagraphStyle(
    name='ExecTitle',
    parent=styles['Title'],
    fontName='Times-Bold',
    fontSize=28,
    leading=32,
    textColor=colors.black,
    alignment=1,
    spaceAfter=6,
))

styles.add(ParagraphStyle(
    name='ExecSubtitle',
    parent=styles['BodyText'],
    fontName='Times-Italic',
    fontSize=11,
    leading=14,
    textColor=colors.black,
    alignment=1,
    spaceAfter=14,
))

styles.add(ParagraphStyle(
    name='ExecIntro',
    parent=styles['BodyText'],
    fontName='Times-Roman',
    fontSize=10.8,
    leading=16,
    textColor=colors.black,
    alignment=1,
    spaceAfter=12,
))

styles.add(ParagraphStyle(
    name='ExecSection',
    parent=styles['Heading2'],
    fontName='Times-Bold',
    fontSize=14,
    leading=18,
    textColor=colors.black,
    alignment=1,
    spaceBefore=12,
    spaceAfter=8,
))

styles.add(ParagraphStyle(
    name='ExecBody',
    parent=styles['BodyText'],
    fontName='Times-Roman',
    fontSize=10.4,
    leading=15,
    textColor=colors.black,
    spaceAfter=8,
))

styles.add(ParagraphStyle(
    name='ExecCardTitle',
    parent=styles['Heading2'],
    fontName='Times-Bold',
    fontSize=11,
    leading=14,
    textColor=colors.black,
    spaceAfter=3,
))

styles.add(ParagraphStyle(
    name='ExecCardBody',
    parent=styles['BodyText'],
    fontName='Times-Roman',
    fontSize=9.6,
    leading=13,
    textColor=colors.black,
    spaceAfter=0,
))


def p(text, style='ExecBody'):
    return Paragraph(text, styles[style])


def card(filename, title, desc):
    path = ICON_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Missing icon: {path}")

    icon = Image(str(path), width=22 * mm, height=22 * mm)
    title_para = Paragraph(f'<b>{title}</b>', styles['ExecCardTitle'])
    body_para = Paragraph(desc, styles['ExecCardBody'])
    tbl = Table([[icon, title_para, body_para]], colWidths=[26 * mm, 28 * mm, 88 * mm], style=[
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LINEBELOW', (0, 0), (-1, 0), 0.5, colors.grey),
        ('BACKGROUND', (0, 0), (-1, -1), colors.Color(0.985, 0.985, 0.985)),
    ])
    return tbl

story = []

story.append(p('<b>ANTZ</b>', 'ExecTitle'))
story.append(p('Logo Philosophy | International Zoo Network', 'ExecSubtitle'))
story.append(Spacer(1, 2))
story.append(p(
    'The ANTZ mark is a visual expression of biodiversity, care, intelligence, and shared responsibility. Each individual element carries a distinct symbolic meaning, yet all belong to one larger story: a globally connected network of zoos, research institutions, conservation organisations, educational organisations, and animal welfare leaders working together for a common purpose.',
    'ExecIntro',
))

story.append(Spacer(1, 8))
story.append(p('<b>1. Core meaning of the emblem</b>', 'ExecSection'))
story.append(p(
    'At the centre of the mark sits a balanced and intelligent form that suggests both an eye and a bird in motion. This central composition communicates perception, memory, freedom, and foresight. It represents a modern zoological institution that observes carefully, understands deeply, and acts responsibly for the long-term welfare of animals and habitats.',
    'ExecBody',
))

story.append(Spacer(1, 8))
story.append(p('<b>2. Symbol interpretation</b>', 'ExecSection'))

symbol_rows = [
    ('lionhead.png', 'Lion', 'Leadership, authority, and protection. The lion represents confidence, presence, and the strength of a trusted conservation institution.'),
    ('swan.png', 'Swan', 'Elegance, grace, and stewardship. The swan brings beauty and calm intelligence to the identity, reflecting careful care and refinement.'),
    ('feather.png', 'Feather', 'Communication, lightness, and knowledge sharing. It suggests the transmission of learning and the importance of public understanding.'),
    ('monkey.png', 'Primate', 'Curiosity, intelligence, and social life. It reflects the complexity of animal behaviour and the importance of observation.'),
    ('giraffe.png', 'Giraffe', 'Perspective, uniqueness, and biodiversity. It conveys the breadth of species and the many environments represented by the institution.'),
    ('deer.png', 'Deer', 'Sensitivity, agility, and harmony with nature. It suggests balance, movement, and respect for living ecosystems.'),
    ('fish.png', 'Fish / Marine Life', 'Aquatic ecosystems and planetary responsibility. It acknowledges that conservation reaches beyond land into oceans and global biodiversity.'),
    ('turtle.png', 'Turtle', 'Resilience, longevity, and endurance. It speaks to long-term stewardship and the protection of vulnerable species.'),
    ('tree.png', 'Tree', 'Growth, habitat, and environment. It grounds the brand in the natural world and reinforces sustainability as a core responsibility.'),
    ('flower.png', 'Flower', 'Renewal, beauty, and nurturing life. It adds a human-centred sense of care, tenderness, and ecological vitality.'),
    ('water.png', 'Water', 'Purity and interconnected life systems. It reflects the essential resources shared across all species and regions.'),
    ('maginfying_glass.png', 'Research', 'Discovery, investigation, and evidence-led conservation. It embodies science, analysis, and informed practice.'),
    ('heart.png', 'Heart', 'Compassion and welfare. It reflects the humane values at the centre of animal care and ethical treatment.'),
    ('speech_bubbles.png', 'Communication', 'Education and engagement. It represents public learning, dialogue, and the role of institutions in raising awareness.'),
    ('plus.png', 'Care', 'Medical support and specialist intervention. It symbolizes welfare expertise and attention to the needs of living animals.'),
    ('tick.png', 'Assurance', 'Accountability and standards. It reflects disciplined care, quality assurance, and trustworthiness.'),
]

for idx in range(0, len(symbol_rows), 2):
    cols = []
    for filename, title, desc in symbol_rows[idx:idx + 2]:
        cols.append(card(filename, title, desc))
    story.append(Table([[cols[0], cols[1]]], colWidths=[140 * mm, 140 * mm], style=[
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(Spacer(1, 5))

story.append(Spacer(1, 8))
story.append(p('<b>3. The global networking principle</b>', 'ExecSection'))
story.append(p(
    'The most important narrative behind ANTZ is the idea of connection. The logo is not only a symbol of a single institution; it represents a network of zoological organisations, sanctuaries, aquariums, wildlife centres, research bodies, and conservation partners across the world. Each element can be read as a different specialism or node within a wider ecosystem of expertise.',
    'ExecBody',
))
story.append(p(
    'This network model is essential to modern conservation. One institution may specialise in primates, another in marine life, another in bird welfare, another in habitat restoration, and another in scientific research. Through cooperation, the international zoo community can exchange knowledge, improve standards, protect biodiversity, and educate the public more effectively than any single organisation could alone.',
    'ExecBody',
))
story.append(p(
    'In this sense, the ANTZ mark functions as both a brand identity and a map of collaboration. It expresses a collective mission: to protect wildlife, improve understanding, and build a more informed and compassionate global movement for animal life.',
    'ExecBody',
))

story.append(Spacer(1, 8))
story.append(p('<b>4. Conclusion</b>', 'ExecSection'))
story.append(p(
    'ANTZ is not simply an emblem for a zoo. It is a symbolic system for a global network of care and conservation. Every element contributes to a larger narrative of biodiversity, responsibility, education, and international cooperation. The result is an identity that is elegant, intelligent, and deeply rooted in the shared mission of protecting life on Earth.',
    'ExecBody',
))

pdf = SimpleDocTemplate(
    str(OUTPUT),
    pagesize=A4,
    rightMargin=18 * mm,
    leftMargin=18 * mm,
    topMargin=18 * mm,
    bottomMargin=18 * mm,
)
pdf.build(story)
print(f"Created executive PDF: {OUTPUT}")
