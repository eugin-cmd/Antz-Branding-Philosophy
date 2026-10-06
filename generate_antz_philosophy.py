from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak

BASE_DIR = Path("/Users/Eugin/Documents/Claude File/Antz Logo Philosophy Document")
OUTPUT = BASE_DIR / "Antz_Logo_Philosophy_Document.pdf"
IMAGE = next(BASE_DIR.glob("Screenshot*png"), None)
if IMAGE is None:
    raise FileNotFoundError(f"No screenshot PNG found in {BASE_DIR}")

styles = getSampleStyleSheet()


def p(text, style_name='AntzBodyText', **kwargs):
    s = styles[style_name]
    for k, v in kwargs.items():
        setattr(s, k, v)
    return Paragraph(text, s)


styles.add(ParagraphStyle(
    name='TitleBlack',
    parent=styles['Title'],
    fontName='Times-Bold',
    fontSize=28,
    leading=32,
    textColor=colors.black,
    alignment=1,
    spaceAfter=10,
))
styles.add(ParagraphStyle(
    name='SectionTitle',
    parent=styles['Heading2'],
    fontName='Times-Bold',
    fontSize=18,
    leading=22,
    textColor=colors.black,
    spaceBefore=18,
    spaceAfter=10,
))
styles.add(ParagraphStyle(
    name='AntzBodyText',
    parent=styles['BodyText'],
    fontName='Times-Roman',
    fontSize=11,
    leading=16,
    textColor=colors.black,
    spaceAfter=8,
))
styles.add(ParagraphStyle(
    name='AntzSmallBody',
    parent=styles['BodyText'],
    fontName='Times-Roman',
    fontSize=10.5,
    leading=15,
    textColor=colors.black,
    spaceAfter=6,
))

story = []


def add_title_block():
    story.append(p('<b>ANTZ</b><br/><font size=11>Logo Philosophy</font>', 'TitleBlack'))
    story.append(p(
        'A living network of knowledge, care, and conservation — where every animal speaks to the character of a zoo institution and every institution contributes to a wider global ecosystem.',
        'AntzBodyText',
        fontName='Times-Italic',
        fontSize=11,
        alignment=1,
        spaceAfter=16,
    ))


add_title_block()

logo_img = Image(str(IMAGE), width=240 * 1.2, height=210 * 1.2)
intro_text = Paragraph(
    "<b>Logo visual expression</b><br/><br/>"
    "Naturally, the letter 'a' of our logo stands for antz. But look a little closer and you will see there is much more to it. "
    "The emblem does not simply represent a word; it tells a story of biodiversity, care, learning, and shared stewardship. "
    "Each form within the logo has a rich meaning, representing an aspect of our business, our mission, and our purpose.<br/><br/>"
    "At the centre, the mark is intentionally calm and complete: a living organism at the heart of the brand, while the surrounding animal forms suggest motion, intelligence, adaptation, and the diversity of environments that modern zoos and conservation institutions serve.",
    styles['AntzBodyText'],
)
story.append(Table([[logo_img, intro_text]], colWidths=[280, 240], style=[('VALIGN', (0, 0), (-1, -1), 'TOP')]))
story.append(Spacer(1, 10))
story.append(p('<b>At the centre</b>', 'SectionTitle', alignment=1))
story.append(p('<b>Flying bird in symmetry<br/>Also eye of the Elephant</b>', 'AntzBodyText', alignment=1, fontSize=13, leading=18, spaceAfter=10))
story.append(p(
    'The central composition signals balance and perception. The bird form implies elevation, freedom, and forward movement; the elephant-like eye suggests memory, intelligence, and the watchful perspective required in conservation and education. Together, the centre expresses a confident, observant institution—one that sees beyond immediate appearances and values long-term stewardship.',
    'AntzBodyText',
))

story.append(Spacer(1, 10))
story.append(p('<b>Starting from the stroke of the letter “a”</b>', 'SectionTitle'))

animal_entries = [
    ('Lion', 'Leader/Majestic'),
    ('Swan', 'Elegance/Beauty'),
    ('Fruits', 'Diet/Nutrition'),
    ('Squirrel', 'Active/Small animal'),
    ('Flying on top', 'Aim high/freedom'),
    ('Tree', 'Forest/Tall'),
    ('Tiger/Panther', 'Agile/Strong'),
    ('Feather', 'Light/Write'),
    ('Primate', 'Active/Alert'),
    ('Humming bird', 'Speed/Efficient'),
    ('Snail', 'Wisdom/Perseverance'),
    ('Giraffe', 'Wild/Unique'),
    ('Plus', 'Medical'),
    ('Magnifier', 'Searchable/data'),
    ('Feeder', 'Medicine/Care'),
    ('Egg', 'Egg management'),
    ('Heart', 'Love/compassion'),
    ('Iguana', 'Reptile world'),
    ('Speech bubble', 'Communication/Share knowledge'),
    ('Flower plant', 'Horticulture'),
    ('Deer', 'Speed/Spiritual/Regenerative'),
    ('School of fishes', 'Groups/Harmony'),
    ('Turtle', 'Seaworld/Robust'),
    ('Fish/Whale', 'Aquatic life'),
    ('Crocodile', 'Amphibian/Guardians'),
    ('Water/Sparkle', 'Clean/Water management'),
    ('Research', 'Share/Connected'),
    ('Tick', 'Task/Checklist'),
]

rows = []
for i in range(0, len(animal_entries), 3):
    row = []
    for label, value in animal_entries[i:i + 3]:
        row.append(Paragraph(f'<b>{label}</b><br/><font size=8>{value}</font>', styles['AntzSmallBody']))
    rows.append(row)

animal_table = Table(rows, colWidths=[150, 150, 150], rowHeights=40)
animal_table.setStyle(TableStyle([
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
]))
story.append(animal_table)

story.append(PageBreak())
story.append(p('<b>What the animals represent</b>', 'SectionTitle'))


def bullet_block(text):
    return p(f'<bullet>&bull;</bullet> {text}', 'AntzBodyText')

story.append(bullet_block('The lion anchors the identity with leadership, confidence, and natural majesty; it suggests authority without arrogance.'))
story.append(bullet_block('The swan and feather add elegance, lightness, and communication; they speak to refinement and the idea of a graceful, high-quality experience.'))
story.append(bullet_block('The primate, bird, and deer energy signals agility, alertness, and vitality—qualities essential in dynamic animal care and modern educational engagement.'))
story.append(bullet_block('The oceanic life, turtle, fish, and whale all connect the brand to aquatic ecosystems and to the broader global environment in which biodiversity is interconnected.'))
story.append(bullet_block('The flower, tree, fruit, and water imagery reflect growth, nourishment, habitat, and sustainability, reinforcing the ecological dimension of the institution.'))
story.append(bullet_block('The magnifier, tick, and research symbols show knowledge, discovery, verification, and a professional, evidence-led culture.'))

story.append(Spacer(1, 10))
story.append(p('<b>The networking heart of ANTZ</b>', 'SectionTitle'))
story.append(p(
    'The most important philosophical idea in this logo is not simply the list of animals. It is the network. ANTZ is imagined as a living alliance of zoos, aquariums, wildlife centres, research institutions, educational bodies, and conservation partners across the world. The emblem brings together different species and different institutional roles into one shared visual language, reflecting a collaborative model in which knowledge, animal care, conservation strategy, and public education are exchanged across borders.<br/><br/>'
    'This is the deeper meaning of the interconnected shapes: every institution has its own expertise, but all are connected by a common purpose. One zoo may specialise in primates, another in marine life, another in habitat restoration, and another in exotic bird care. The network is what transforms individual excellence into collective impact. Through shared knowledge, coordinated breeding, habitat stewardship, education, and public engagement, the global zoo community becomes a single living system.<br/><br/>'
    'In this sense, the logo is both an identity mark and a map of collaboration. It argues that the future of animal conservation is not isolated—it is networked, interdisciplinary, and globally connected. ANTZ represents a world in which institutions do not compete in isolation but learn from one another, support one another, and build a stronger, more resilient future for wildlife and humanity alike.',
    'AntzBodyText',
))

story.append(Spacer(1, 14))
story.append(p('<b>Summary</b>', 'SectionTitle'))
story.append(p(
    'The ANTZ logo is a visual expression of biodiversity, care, intelligence, and shared purpose. It brings together many animals, many functions, and many forms of expertise into an elegant monogram that remains easy to recognise while holding extraordinary depth. Above all, it embodies the idea that zoos and conservation institutions are not standalone entities: they are part of a global network of learning, stewardship, and responsibility.',
    'AntzBodyText',
))

pdf = SimpleDocTemplate(
    str(OUTPUT),
    pagesize=A4,
    rightMargin=25 * mm,
    leftMargin=25 * mm,
    topMargin=18 * mm,
    bottomMargin=18 * mm,
)
pdf.build(story)
print(f"Created PDF: {OUTPUT}")
