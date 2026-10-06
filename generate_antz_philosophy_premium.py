from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak

BASE_DIR = Path("/Users/Eugin/Documents/Claude File/Antz Logo Philosophy Document")
ICON_DIR = BASE_DIR / "reference" / "icon_elements"
OUTPUT = BASE_DIR / "Antz_Logo_Philosophy_Document_Premium.pdf"

styles = getSampleStyleSheet()

styles.add(ParagraphStyle(
    name='PremiumTitle',
    parent=styles['Title'],
    fontName='Times-Bold',
    fontSize=26,
    leading=30,
    textColor=colors.black,
    alignment=1,
    spaceAfter=4,
))

styles.add(ParagraphStyle(
    name='PremiumSubtitle',
    parent=styles['BodyText'],
    fontName='Times-Italic',
    fontSize=11,
    leading=14,
    textColor=colors.black,
    alignment=1,
    spaceAfter=12,
))

styles.add(ParagraphStyle(
    name='SectionTitle',
    parent=styles['Heading2'],
    fontName='Times-Bold',
    fontSize=15,
    leading=18,
    textColor=colors.black,
    alignment=1,
    spaceBefore=14,
    spaceAfter=10,
))

styles.add(ParagraphStyle(
    name='BodyLeft',
    parent=styles['BodyText'],
    fontName='Times-Roman',
    fontSize=10.7,
    leading=16,
    textColor=colors.black,
    alignment=1,
    spaceAfter=10,
))

styles.add(ParagraphStyle(
    name='CardTitle',
    parent=styles['Heading2'],
    fontName='Times-Bold',
    fontSize=11,
    leading=14,
    textColor=colors.black,
    alignment=1,
    spaceAfter=3,
))

styles.add(ParagraphStyle(
    name='CardBody',
    parent=styles['BodyText'],
    fontName='Times-Roman',
    fontSize=10,
    leading=14,
    textColor=colors.black,
    alignment=1,
    wordWrap='CJK',
))


def p(text, style='BodyLeft'):
    return Paragraph(text, styles[style])


def make_card(filename, title, text):
    image_path = ICON_DIR / filename
    if not image_path.exists():
        raise FileNotFoundError(f"Missing icon asset: {image_path}")

    icon = Image(str(image_path), width=25 * mm, height=25 * mm)
    text_block = Paragraph(f'<b>{title}</b><br/>{text}', styles['CardBody'])
    table = Table([[icon, text_block]], colWidths=[35 * mm, 120 * mm], style=[
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('BACKGROUND', (0, 0), (-1, -1), colors.Color(0.983, 0.983, 0.983)),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ])
    return table


story = []

story.append(p('<b>ANTZ</b>', 'PremiumTitle'))
story.append(p('Logo Philosophy and Symbol Interpretation', 'PremiumSubtitle'))
story.append(Spacer(1, 3))
story.append(p(
    'The ANTZ identity is a living system of meaning. Each symbol, animal, and graphic element contributes to a wider narrative of biodiversity, animal care, research, education, and international cooperation. Taken together, the logo expresses a global network of zoological institutions working in shared purpose and mutual stewardship.',
    'BodyLeft',
))

story.append(Spacer(1, 6))
story.append(p('<b>Central emblem</b>', 'SectionTitle'))
story.append(p(
    'At the centre of the mark sits a composed, balanced form that suggests an eye, a bird in elevation, and a living organism all at once. This core image conveys perception, memory, freedom, and intelligence. It represents a zoo that does not simply exhibit animals, but studies them, understands them, and protects them with care and long-term vision.',
    'BodyLeft',
))

story.append(Spacer(1, 8))
story.append(p('<b>Animal and symbol meaning</b>', 'SectionTitle'))

cards = [
    ('lionhead.png', 'Lion', 'Leadership, confidence, and authority. It suggests the strength of a trusted institution and the protective role of conservation.'),
    ('swan.png', 'Swan', 'Elegance, grace, and measured stewardship. It reflects beauty, care, and an elevated standard of welfare.'),
    ('feather.png', 'Feather', 'Communication, lightness, and knowledge-sharing. It conveys refinement and the idea of learning through observation.'),
    ('monkey.png', 'Primate', 'Curiosity, intelligence, and social behaviour. It captures the complexity of animals and the importance of understanding them deeply.'),
    ('giraffe.png', 'Giraffe', 'Perspective, uniqueness, and species diversity. It expresses the breadth of wildlife represented across habitats and regions.'),
    ('deer.png', 'Deer', 'Sensitivity, agility, and environmental harmony. It signals movement, balance, and a respectful relationship with nature.'),
    ('fish.png', 'Fish / Marine Life', 'Aquatic biodiversity and the wider ecological system. It recognizes that conservation is planetary, not isolated.'),
    ('turtle.png', 'Turtle', 'Resilience, longevity, and continuity. It reflects long-term guardianship and a sustained responsibility to life.'),
    ('tree.png', 'Tree', 'Growth, habitat, and ecological stability. It grounds the identity in the natural environment and sustainable care.'),
    ('flower.png', 'Flower', 'Renewal, beauty, and nurturing life. It represents the living world in all of its fragility and richness.'),
    ('water.png', 'Water', 'Purity, circulation, and the shared systems that connect every living organism across the planet.'),
    ('maginfying_glass.png', 'Research / Magnifier', 'Discovery, evidence, and scientific expertise. It expresses the analytical and educational foundation of the institution.'),
    ('heart.png', 'Heart', 'Compassion, welfare, and ethical care. It captures the emotional intelligence at the heart of the organisation.'),
    ('speech_bubbles.png', 'Speech Bubble', 'Education, engagement, and public communication. It reinforces the role of the zoo as a place of learning and dialogue.'),
    ('plus.png', 'Plus / Care', 'Medical support, welfare intervention, and specialist attention. It reflects a professional, thorough approach to animal wellbeing.'),
    ('tick.png', 'Check / Assurance', 'Verification, accountability, and standards. It signals trust, discipline, and responsible practice.'),
]

for i in range(0, len(cards), 2):
    row = []
    for filename, title, desc in cards[i:i + 2]:
        row.append(make_card(filename, title, desc))
    story.append(Table([row], colWidths=[140 * mm, 140 * mm], style=[
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(Spacer(1, 6))

story.append(Spacer(1, 8))
story.append(p('<b>The networking heart of ANTZ</b>', 'SectionTitle'))
story.append(p(
    'This is the most important philosophical idea behind the brand: ANTZ is not a single zoo, but a connected network of institutions across the world. Each animal and symbol can be understood as a specialist field—primates, marine life, birds, research, veterinary care, public education, habitat preservation, and more. Together, they form a living ecosystem of expertise and responsibility.',
    'BodyLeft',
))
story.append(p(
    'The logo therefore stands for collaboration, not isolation. It expresses a community of zoos, sanctuaries, research centres, aquariums, and conservation organisations working across borders to exchange knowledge, strengthen care standards, protect biodiversity, and create a more informed global public. The network is the real meaning of the mark—a shared mission carried by many institutions united under one vision.',
    'BodyLeft',
))

story.append(Spacer(1, 10))
story.append(p('<b>Conclusion</b>', 'SectionTitle'))
story.append(p(
    'ANTZ is a symbol of biodiversity, care, intelligence, and international collaboration. Each element adds a distinct layer of meaning, yet all belong to one unified philosophy: the idea that animal welfare, education, conservation, and research are strongest when they are connected. In that sense, the logo is not only an identity—it is an expression of a global network of institutions moving forward together.',
    'BodyLeft',
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
print(f"Created premium version: {OUTPUT}")
