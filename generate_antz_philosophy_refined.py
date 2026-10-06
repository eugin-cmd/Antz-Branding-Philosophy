from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle

BASE_DIR = Path("/Users/Eugin/Documents/Claude File/Antz Logo Philosophy Document")
ICON_DIR = BASE_DIR / "reference" / "icon_elements"
OUTPUT = BASE_DIR / "Antz_Logo_Philosophy_Document_Refined.pdf"

styles = getSampleStyleSheet()

styles.add(ParagraphStyle(
    name='TitleLeft',
    parent=styles['Title'],
    fontName='Times-Bold',
    fontSize=26,
    leading=30,
    textColor=colors.black,
    alignment=1,
    spaceAfter=8,
))

styles.add(ParagraphStyle(
    name='SubtitleLeft',
    parent=styles['BodyText'],
    fontName='Times-Italic',
    fontSize=11,
    leading=15,
    textColor=colors.black,
    alignment=1,
    spaceAfter=18,
))

styles.add(ParagraphStyle(
    name='SectionLeft',
    parent=styles['Heading2'],
    fontName='Times-Bold',
    fontSize=15,
    leading=18,
    textColor=colors.black,
    alignment=1,
    spaceBefore=12,
    spaceAfter=10,
))

styles.add(ParagraphStyle(
    name='IntroText',
    parent=styles['BodyText'],
    fontName='Times-Roman',
    fontSize=10.8,
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
    spaceAfter=4,
))

styles.add(ParagraphStyle(
    name='CardBody',
    parent=styles['BodyText'],
    fontName='Times-Roman',
    fontSize=10,
    leading=14,
    textColor=colors.black,
    alignment=1,
    spaceAfter=4,
))


def para(text, style='IntroText'):
    return Paragraph(text, styles[style])


def make_card(filename: str, title: str, description: str):
    image_path = ICON_DIR / filename
    if not image_path.exists():
        raise FileNotFoundError(f"Missing icon asset: {image_path}")

    img = Image(str(image_path), width=26 * mm, height=23 * mm)
    text = Paragraph(
        f'<b>{title}</b><br/>{description}',
        styles['CardBody'],
    )
    table = Table([[img, text]], colWidths=[36 * mm, 120 * mm], style=[
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('BACKGROUND', (0, 0), (-1, -1), colors.Color(0.98, 0.98, 0.98)),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ])
    return table


story = []

story.append(para('<b>ANTZ</b>', 'TitleLeft'))
story.append(para('Logo Philosophy and Brand Symbolism', 'SubtitleLeft'))
story.append(Spacer(1, 4))

story.append(para(
    'The ANTZ logo is built as a living ecosystem of meaning. Each animal and symbol represents a distinct dimension of the zoo mission: leadership, biodiversity, intelligence, care, conservation, education, and cross-institution collaboration. More than a single emblem, it expresses a global network of organisations working together to protect life on Earth.',
    'IntroText',
))

story.append(para('<b>Core interpretation</b>', 'SectionLeft'))
story.append(make_card('lionhead.png', 'Lion', 'Leadership, authority, and natural majesty. The lion embodies confidence and protection, expressing the strength of a trusted zoological institution.'))
story.append(Spacer(1, 7))
story.append(make_card('swan.png', 'Swan', 'Elegance, refinement, and careful stewardship. The swan suggests grace, beauty, and a calm but highly considered approach to animal care.'))
story.append(Spacer(1, 7))
story.append(make_card('feather.png', 'Feather', 'Communication, lightness, and knowledge transfer. It reinforces the idea of learning, beauty, and the importance of shared understanding.'))
story.append(Spacer(1, 7))
story.append(make_card('monkey.png', 'Primate', 'Intelligence, curiosity, and social connection. This symbol reflects behavioural understanding, awareness, and the living complexity of animal life.'))
story.append(Spacer(1, 7))
story.append(make_card('giraffe.png', 'Giraffe', 'Perspective, uniqueness, and wild identity. The giraffe stands for species differentiation and the breadth of life represented across global habitats.'))
story.append(Spacer(1, 7))
story.append(make_card('deer.png', 'Deer', 'Sensitivity, agility, and regenerative nature. It speaks to movement, balance, and a respectful relationship with the natural world.'))

story.append(Spacer(1, 10))
story.append(para('<b>Marine and habitat symbolism</b>', 'SectionLeft'))
story.append(make_card('fish.png', 'Fish / Marine Life', 'Aquatic ecosystems, biodiversity, and global environmental responsibility. It acknowledges the broader ecological system beyond land-based species.'))
story.append(Spacer(1, 7))
story.append(make_card('turtle.png', 'Turtle', 'Resilience, longevity, and continuity. The turtle signals a long-term commitment to stewardship and protected habitats.'))
story.append(Spacer(1, 7))
story.append(make_card('tree.png', 'Tree', 'Growth, habitat, and ecological balance. The tree anchors the brand in the natural world and reflects sustainable conservation.'))
story.append(Spacer(1, 7))
story.append(make_card('flower.png', 'Flower', 'Life, renewal, beauty, and nurturing care. It reinforces the botanical dimension of conservation and public learning.'))
story.append(Spacer(1, 7))
story.append(make_card('water.png', 'Water', 'Purity, environmental health, and the essential life systems that connect all species across the planet.'))

story.append(Spacer(1, 10))
story.append(para('<b>Knowledge, care, and communication</b>', 'SectionLeft'))
story.append(make_card('maginfying_glass.png', 'Research / Magnifier', 'Discovery, evidence, and professional conservation practice. It represents inquiry, monitoring, and scientific understanding.'))
story.append(Spacer(1, 7))
story.append(make_card('heart.png', 'Heart', 'Compassion, welfare, and ethical care. This symbol reflects the emotional and humane values at the centre of the organisation.'))
story.append(Spacer(1, 7))
story.append(make_card('speech_bubbles.png', 'Speech bubble', 'Education, public engagement, and shared learning. It communicates the zoo’s role as a place of understanding and connection.'))
story.append(Spacer(1, 7))
story.append(make_card('plus.png', 'Plus / Care', 'Medical support, wellness, and intervention when animal care requires specialised attention.'))
story.append(Spacer(1, 7))
story.append(make_card('tick.png', 'Checklist / Assurance', 'Verification, accountability, and care standards. It reflects a disciplined approach to welfare, records, and trust.'))

story.append(Spacer(1, 10))
story.append(para('<b>The greater meaning: a network of institutions</b>', 'SectionLeft'))
story.append(para(
    'This is the most important idea behind the logo. ANTZ stands for a global community of zoos, aquariums, sanctuaries, research centres, and conservation organisations working as one connected ecosystem. Each institution has its own specialism—primates, marine life, birds, habitat restoration, public education, veterinary care, research—but all are linked by a shared mission: to protect biodiversity, deepen knowledge, and create a better future for wildlife and people alike.',
    'IntroText',
))
story.append(para(
    'The logo therefore communicates collaboration rather than isolation. It reflects a world in which knowledge, care, and conservation are exchanged across borders. Every symbol in the mark belongs to a larger network of expertise, and every institution plays a role in a broader system of responsibility.',
    'IntroText',
))

story.append(Spacer(1, 8))
story.append(para('<b>Conclusion</b>', 'SectionLeft'))
story.append(para(
    'ANTZ is more than a brand symbol. It is a visual expression of biodiversity, compassion, intelligence, stewardship, and international collaboration. When the logo is understood as a set of distinct elements, each one becomes legible and meaningful; when viewed as a whole, the true message becomes clear: a connected global network of institutions committed to animal welfare, conservation, and shared learning.',
    'IntroText',
))

pdf = SimpleDocTemplate(
    str(OUTPUT),
    pagesize=A4,
    rightMargin=20 * mm,
    leftMargin=20 * mm,
    topMargin=18 * mm,
    bottomMargin=18 * mm,
)
pdf.build(story)
print(f"Created professional left-aligned PDF: {OUTPUT}")
