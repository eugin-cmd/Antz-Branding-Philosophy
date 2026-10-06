from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak

BASE_DIR = Path("/Users/Eugin/Documents/Claude File/Antz Logo Philosophy Document")
ICON_DIR = BASE_DIR / "reference" / "icon_elements"
OUTPUT = BASE_DIR / "Antz_Logo_Philosophy_Document_Luxury.pdf"

styles = getSampleStyleSheet()

styles.add(ParagraphStyle(
    name='LuxuryTitle',
    parent=styles['Title'],
    fontName='Times-Bold',
    fontSize=30,
    leading=34,
    textColor=colors.black,
    alignment=1,
    spaceAfter=4,
))

styles.add(ParagraphStyle(
    name='LuxurySubtitle',
    parent=styles['BodyText'],
    fontName='Times-Italic',
    fontSize=11,
    leading=14,
    textColor=colors.black,
    alignment=1,
    spaceAfter=18,
))

styles.add(ParagraphStyle(
    name='LuxuryIntro',
    parent=styles['BodyText'],
    fontName='Times-Roman',
    fontSize=11,
    leading=17,
    textColor=colors.black,
    alignment=1,
    spaceAfter=16,
))

styles.add(ParagraphStyle(
    name='LuxurySection',
    parent=styles['Heading2'],
    fontName='Times-Bold',
    fontSize=15,
    leading=18,
    textColor=colors.black,
    alignment=1,
    spaceBefore=16,
    spaceAfter=10,
))

styles.add(ParagraphStyle(
    name='LuxuryBody',
    parent=styles['BodyText'],
    fontName='Times-Roman',
    fontSize=10.5,
    leading=15.5,
    textColor=colors.black,
    spaceAfter=8,
))

styles.add(ParagraphStyle(
    name='LuxuryCardTitle',
    parent=styles['Heading2'],
    fontName='Times-Bold',
    fontSize=11,
    leading=14,
    textColor=colors.black,
    spaceAfter=2,
))

styles.add(ParagraphStyle(
    name='LuxuryCardBody',
    parent=styles['BodyText'],
    fontName='Times-Roman',
    fontSize=9.4,
    leading=13,
    textColor=colors.black,
    spaceAfter=0,
))


def p(text, style='LuxuryBody'):
    return Paragraph(text, styles[style])


def make_card(filename, title, desc):
    path = ICON_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Missing icon: {path}")

    icon = Image(str(path), width=22 * mm, height=22 * mm)
    title_para = Paragraph(f'<b>{title}</b>', styles['LuxuryCardTitle'])
    desc_para = Paragraph(desc, styles['LuxuryCardBody'])
    table = Table([[icon, title_para, desc_para]], colWidths=[26 * mm, 30 * mm, 92 * mm], style=[
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('BACKGROUND', (0, 0), (-1, -1), colors.Color(0.985, 0.985, 0.985)),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ])
    return table


def cover_page():
    story = []
    story.append(Spacer(1, 18))
    story.append(p('<b>ANTZ</b>', 'LuxuryTitle'))
    story.append(p('Logo Philosophy and Brand Symbolism', 'LuxurySubtitle'))
    story.append(Spacer(1, 18))
    story.append(p(
        'A global identity shaped by biodiversity, care, intelligence, and international collaboration.',
        'LuxuryIntro',
    ))
    story.append(Spacer(1, 10))
    story.append(p('The ANTZ logo is more than a mark. It is a living system of meaning—an ecosystem of symbols, institutions, and shared purpose designed to represent a worldwide network of zoological expertise.', 'LuxuryIntro'))
    return story


story = []
story.extend(cover_page())
story.append(PageBreak())

story.append(p('<b>Brand philosophy</b>', 'LuxurySection'))
story.append(p(
    'The ANTZ identity is built on a single idea: that conservation, education, animal welfare, and scientific understanding are strongest when they are connected. Every symbol in the mark contributes to this broader narrative. The result is a visual system that feels elegant, intelligent, and deeply rooted in the mission of safeguarding life on Earth.',
    'LuxuryBody',
))
story.append(p(
    'The central form of the logo suggests observation, memory, and freedom. It is both a bird in motion and an eye-like symbol of vigilance. This balance creates the emotional language of the brand: calm, purposeful, perceptive, and deeply humane.',
    'LuxuryBody',
))

story.append(Spacer(1, 10))
story.append(p('<b>Symbol interpretation</b>', 'LuxurySection'))

entries = [
    ('lionhead.png', 'Lion', 'Leadership, authority, and protection. It represents the strength and trust expected of a conservation institution.'),
    ('swan.png', 'Swan', 'Elegance, grace, and refined care. It expresses beauty, calm intelligence, and a considered approach to animal welfare.'),
    ('feather.png', 'Feather', 'Communication and lightness. It symbolizes the transfer of knowledge and the value of public understanding.'),
    ('monkey.png', 'Primate', 'Curiosity, intelligence, and social complexity. It reflects the importance of behavioural understanding.'),
    ('giraffe.png', 'Giraffe', 'Perspective, biodiversity, and uniqueness. It speaks to the breadth of species and global ecosystems.'),
    ('deer.png', 'Deer', 'Sensitivity, agility, and environmental harmony. It reflects movement, balance, and respect for nature.'),
    ('fish.png', 'Fish / Marine Life', 'Aquatic biodiversity and planetary stewardship. It extends the brand beyond land-based institutions to the wider living world.'),
    ('turtle.png', 'Turtle', 'Resilience and longevity. It represents long-term care, continuity, and the protection of vulnerable species.'),
    ('tree.png', 'Tree', 'Growth, habitat, and ecological stability. It grounds the identity in the environment and in sustainable stewardship.'),
    ('flower.png', 'Flower', 'Renewal and nurturing life. It signals care, beauty, and the delicate balance of natural systems.'),
    ('water.png', 'Water', 'Purity, shared life systems, and environmental health. It emphasizes the common resources that connect all life.'),
    ('maginfying_glass.png', 'Research', 'Discovery, science, and evidence-led understanding. It anchors the brand in rigorous, informed conservation practice.'),
    ('heart.png', 'Heart', 'Compassion and ethical welfare. It reflects the emotional and moral commitment at the centre of the organisation.'),
    ('speech_bubbles.png', 'Communication', 'Education and public engagement. It expresses the role of the institution as a place of exchange and trust.'),
    ('plus.png', 'Care', 'Medical expertise and specialised support. It reflects professional responsiveness and high standards of animal wellbeing.'),
    ('tick.png', 'Assurance', 'Accountability and quality. It signals trust, standards, and disciplined guardianship.'),
]

for i in range(0, len(entries), 2):
    row = []
    for filename, title, desc in entries[i:i+2]:
        row.append(make_card(filename, title, desc))
    story.append(Table([[row[0], row[1]]], colWidths=[140 * mm, 140 * mm], style=[
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(Spacer(1, 5))

story.append(Spacer(1, 10))
story.append(p('<b>The networking heart of ANTZ</b>', 'LuxurySection'))
story.append(p(
    'This is the most important idea behind the brand. ANTZ represents not a single institution, but a global network of zoos, aquariums, sanctuaries, research centres, conservation bodies, and educational organisations working in alliance. Each animal or symbol can be interpreted as a specialist discipline or institution within a larger system of expertise.',
    'LuxuryBody',
))
story.append(p(
    'In practice, that means one organisation may focus on primates, another on marine life, another on bird conservation, another on habitat restoration, and another on scientific publication and public education. What unites them is a shared mission: to protect biodiversity, improve animal welfare, and advance knowledge for the benefit of people and wildlife alike.',
    'LuxuryBody',
))
story.append(p(
    'The network is therefore the true philosophy of the mark. It expresses collaboration, exchange, and collective responsibility across borders. The ANTZ identity is a visual statement that the future of conservation is global, shared, and deeply interconnected.',
    'LuxuryBody',
))

story.append(Spacer(1, 10))
story.append(p('<b>Conclusion</b>', 'LuxurySection'))
story.append(p(
    'ANTZ is a symbol of biodiversity, compassion, intelligence, and international collaboration. Every element contributes to a distinct layer of meaning, yet all belong to one unified system of thought: that the most effective care for wildlife is collective, informed, and humane. The logo becomes a statement of identity, vision, and global responsibility—an elegant expression of what a connected world of conservation should look like.',
    'LuxuryBody',
))

pdf = SimpleDocTemplate(
    str(OUTPUT),
    pagesize=A4,
    rightMargin=18 * mm,
    leftMargin=18 * mm,
    topMargin=16 * mm,
    bottomMargin=16 * mm,
)
pdf.build(story)
print(f"Created luxury PDF: {OUTPUT}")
