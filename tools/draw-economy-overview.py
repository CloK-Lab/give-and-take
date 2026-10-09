"""Energy supports a human-agent network with allocation and renewal mechanisms."""
from pathlib import Path
from base64 import b64encode
from html import escape
from math import atan2, degrees, hypot
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
BLUE, PURPLE, GOLD = '#86b9d5', '#b6a4c9', '#c6ad79'
INK, MUTED, RULE = '#dfebf4', '#9fa6b2', '#303b47'
parts = ['''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="630" viewBox="0 0 1080 630" role="img" aria-labelledby="title description">
<title id="title">DSI on Chain and mathematically verified infrastructure</title>
<desc id="description">A conceptual network of six human-agent pairs: each outer cube carries a human and an agent icon and connects by a short chain to its nearest wallet in a smaller gold hexagon. A blue flame represents energy at the center. The interior has no arrows or labels. To the right, Mathematically verified infra groups four illustrations in a two-by-two grid: Hardware, a chip and circuit board; Compute, a server cluster; Software, a code editor; and Science, an experiment and observation sheet. Two arrows labeled Improve connect the network and infrastructure as whole groups in opposite directions. Superintelligence and mathematical verification describe the research goals, not achieved capabilities. Feedback represents maintenance and upgrades, not the recovery of consumed energy or proof of empirical truth.</desc>
''']
fonts, licenses = [], []
for package, family in [('jost', 'Jost'), ('ibm-plex-mono', 'Plex')]:
    folder = ROOT / 'node_modules/@fontsource' / package
    data = b64encode((folder / 'files' / f'{package}-latin-400-normal.woff2').read_bytes()).decode()
    fonts.append(f"@font-face{{font-family:{family};src:url(data:font/woff2;base64,{data}) format('woff2')}}")
    licenses.append((folder / 'LICENSE').read_text())
licenses.append((ROOT / 'tools/assets/lucide-LICENSE').read_text())
parts += ['<metadata>' + escape('\n\n'.join(licenses)) + '</metadata>', '<style>', *fonts, '''
text{font-family:Jost,sans-serif;font-weight:400}
.mono{font-family:Plex,monospace;letter-spacing:1.2px}
.compact{display:none}
@media(max-width:620px){.wide{display:none}.compact{display:inline}}
</style><defs>
''']
for name, color in [('blue', BLUE), ('purple', PURPLE), ('gold', GOLD), ('ink', INK)]:
    parts.append(f'<marker id="{name}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M2 1 L8 5 L2 9" fill="none" stroke="{color}" stroke-width="1.4"/></marker>')
parts.append('</defs><rect width="1080" height="630" fill="#0a0a0f"/>')


def text(x, y, label, size=24, color=INK, anchor='middle', mono=False):
    parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" class="{"mono" if mono else ""}">{escape(label)}</text>')


def line(d, color=RULE, width=1, opacity=1, arrow=None, fill='none', dashed=False):
    attrs = f' marker-end="url(#{arrow})"' if arrow else ''
    if dashed:
        attrs += ' stroke-dasharray="6 7"'
    parts.append(f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{width}" opacity="{opacity}" stroke-linecap="round" stroke-linejoin="round"{attrs}/>')


def rect(x, y, w, h, fill='none', stroke=RULE, radius=4):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>')


def flame(x, y):
    # Lucide's flame outline; see docs/DIAGRAMS.md for source and license.
    icon = ElementTree.parse(ROOT / 'tools/assets/lucide-flame.svg').getroot()
    parts.append(f'<g transform="translate({x - 48} {y - 50}) scale(4)">')
    for shape in icon.findall('{http://www.w3.org/2000/svg}path'):
        line(shape.attrib['d'], BLUE, .5)
    parts.append('</g>')


def rack(x, y):
    # Tall enclosures, trays and indicators distinguish the cluster from cubes.
    parts.append(f'<g transform="translate({x} {y})">')
    line('M0 -40 L25 -27 L0 -14 L-25 -27 Z', BLUE, 1.3, fill='#203848')
    line('M-25 -27 L0 -14 V58 L-25 45 Z', '#648ba5', 1.3, fill='#101e29')
    line('M0 -14 L25 -27 V45 L0 58 Z', BLUE, 1.3, fill='#172c3b')
    parts.append('<g transform="translate(4 -5) skewY(-28)">')
    for yy in [0, 18, 36]:
        rect(0, yy, 17, 12, '#0c1720', '#678fa8', 1)
        line(f'M3 {yy+4} H11 M3 {yy+8} H9', '#8aaec4', .9)
        rect(13, yy + 5, 2, 2, '#c2dfec', 'none', 0)
    parts.append('</g></g>')


def cluster():
    line('M27 513 L125 462 L268 537 L167 593 Z', '#3f5c70', 1, fill='#0e1720')
    line('M27 513 V522 L167 602 L268 546 V537 M167 593 V602', '#3f5c70', 1)
    racks = [(95 + 47*c - 47*r, 429 + 24*c + 24*r) for r in range(2) for c in range(3)]
    for x, y in sorted(racks, key=lambda pos: pos[1]):
        rack(x, y)


def peer(x, y):
    # Human and agent share one cube, with one glyph on each visible face.
    parts.append(f'<g transform="translate({x} {y})">')
    line('M0 -31 L28 -15 L0 1 L-28 -15 Z', PURPLE, 1.3, fill='#2a2336')
    line('M-28 -15 L0 1 V35 L-28 19 Z', PURPLE, 1.3, fill='#171420')
    line('M0 1 L28 -15 V19 L0 35 Z', PURPLE, 1.3, fill='#211b2c')
    parts.append('<g transform="translate(-24 -5) skewY(29)">')
    parts.append(f'<circle cx="9" cy="5" r="3.5" fill="none" stroke="{INK}" stroke-width="1.2"/>')
    line('M2 21 V18 C2 10 16 10 16 18 V21', INK, 1.2)
    parts.append('</g><g transform="translate(5 6) skewY(-29)">')
    rect(0, 3, 18, 16, 'none', INK, 2)
    line('M9 3 V-1 M6 -1 H12 M-2 8 V14 M20 8 V14', INK, 1.2)
    for xx in [5, 13]:
        parts.append(f'<circle cx="{xx}" cy="10" r="1.1" fill="{INK}"/>')
    line('M5 15 H13', INK, 1.2)
    parts.append('</g></g>')


def chain(x1, y1, x2, y2):
    # Two small links fit the gap between a pair and its wallet; no direction.
    length = hypot(x2 - x1, y2 - y1)
    angle = degrees(atan2(y2 - y1, x2 - x1))
    parts.append(f'<g transform="translate({x1} {y1}) rotate({angle})">')
    for start in [0, length * .4]:
        parts.append(f'<rect x="{start}" y="-3" width="{length * .6}" height="6" rx="3" fill="none" stroke="{GOLD}" stroke-width="1.15"/>')
    parts.append('</g>')


def wallet(x, y):
    # Reuse the system diagram's wallet geometry at a smaller scale.
    parts.append(f'<g transform="translate({x} {y}) scale(.4)">')
    line('M0 -55 L50 -27 L0 1 L-50 -27 Z', GOLD, 3, fill='#3b3220')
    line('M-50 -27 L0 1 V58 L-50 30 Z', GOLD, 3, fill='#211c13')
    line('M0 1 L50 -27 V30 L0 58 Z', GOLD, 3, fill='#2d2518')
    parts.append('<g transform="translate(10 6) skewY(-29)">')
    parts.append(f'<rect x="1" y="3" width="28" height="27" rx="2" fill="none" stroke="{GOLD}" stroke-width="3"/>')
    line('M21 12 H30 V22 H21 Z', GOLD, 3)
    parts.append(f'<circle cx="25" cy="17" r="1.6" fill="{GOLD}"/>')
    parts.append('</g></g>')


def hardware(x, y):
    # A processor on a circuit board distinguishes physical design from compute.
    parts.append(f'<g transform="translate({x} {y}) scale(.85)">')
    line('M0 -55 L95 0 L0 55 L-95 0 Z', '#54798f', 1.6, fill='#142734')
    line('M-95 0 L0 55 V64 L-95 9 Z', BLUE, 1.4, fill='#101e29')
    line('M0 55 L95 0 V9 L0 64 Z', BLUE, 1.4, fill='#192e3d')
    for path in [
        'M-28 7 L-53 21 L-70 11',
        'M-16 15 L-38 28 L-51 20',
        'M28 7 L53 21 L70 11',
        'M16 15 L38 28 L51 20',
        'M-28 -29 L-49 -17 L-66 -27',
        'M28 -29 L49 -17 L66 -27',
    ]:
        line(path, '#6f99b1', 1.4)
    for xx, yy in [(-70,11), (70,11), (-66,-27), (66,-27)]:
        parts.append(f'<circle cx="{xx}" cy="{yy}" r="2.2" fill="{BLUE}"/>')
    line('M0 -43 L38 -21 L0 1 L-38 -21 Z', BLUE, 1.6, fill='#264455')
    line('M-38 -21 L0 1 V15 L-38 -7 Z', BLUE, 1.4, fill='#132330')
    line('M0 1 L38 -21 V-7 L0 15 Z', BLUE, 1.4, fill='#1c3342')
    line('M0 -34 L24 -20 L0 -6 L-24 -20 Z M-12 -27 L12 -13 M12 -27 L-12 -13', '#bdd6e5', 1.4)
    parts.append('</g>')


def science(x, y, scale=.82):
    # A flask beside an observation sheet: an illustration, not measured data.
    parts.append(f'<g transform="translate({x} {y}) scale({scale})">')
    line('M-72 -58 H-48 M-68 -57 V-22 L-95 39 Q-98 49 -85 49 H-33 Q-21 49 -25 39 L-52 -22 V-57', BLUE, 1.7, fill='#101d27')
    line('M-82 12 Q-60 6 -39 12 L-25 39 Q-21 49 -33 49 H-85 Q-98 49 -95 39 Z', '#486f88', 1.3, fill='#1e3647')
    for x, y, radius in [(-63, 26, 2.5), (-49, 38, 2), (-70, 40, 1.5)]:
        parts.append(f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{BLUE}"/>')
    line('M0 -64 H66 L84 -46 V52 H0 Z M66 -64 V-46 H84', BLUE, 1.6, fill='#101820')
    line('M13 -47 H46 M13 -36 H35', MUTED, 1.3)
    line('M14 -16 V35 H70', '#739ab3', 1.4)
    line('M19 27 C29 29 30 12 40 15 S55 -8 67 -6', BLUE, 2)
    line('M-103 63 H93', RULE, 1.4)
    parts.append('</g>')


def software(x, y, scale=.78):
    parts.append(f'<g transform="translate({x} {y}) scale({scale})">')
    rect(-100, -63, 200, 119, '#101820', '#54798f', 4)
    line('M-99 -39 H99', '#54798f', 1.3)
    for x in [-84, -74, -64]:
        parts.append(f'<circle cx="{x}" cy="-51" r="2" fill="{BLUE}"/>')
    # A recognizable code editor, with a short function rather than extra prose.
    line('M-80 -19 L-73 -12 L-80 -5 M-67 -5 H-54', BLUE, 1.8)
    line('M-35 -20 H5 M13 -20 H37 M-35 -4 H-4 M6 -4 H74 M-19 12 H27 M37 12 H59 M-35 29 H-6', '#86b9d5', 2)
    line('M-108 66 H108 L94 74 H-94 Z', BLUE, 1.4, fill='#152531')
    parts.append('</g>')


for compact in [False, True]:
    parts.append(f'<g class="{"compact" if compact else "wide"}">')
    # Move the unchanged network left to give both grid columns enough room.
    parts.append('<g transform="translate(-100 0)">')
    text(350, 75, 'DSI on Chain', 44 if compact else 36)

    # Two concentric networks, with only a flame at their shared center.
    line('M350 160 L520 255 V450 L350 550 L180 450 V255 Z', '#675776', 1.8)
    line('M350 242 L449 297 V410 L350 468 L251 410 V297 Z', '#806e4c', 1.5)
    for endpoints in [
        (350, 199, 350, 216),
        (489, 274, 472, 284),
        (489, 433, 472, 423),
        (350, 495, 350, 515),
        (211, 433, 228, 423),
        (211, 274, 228, 284),
    ]:
        chain(*endpoints)
    for x, y in [(350,242), (449,297), (449,410), (350,468), (251,410), (251,297)]:
        wallet(x, y)
    flame(350, 355)
    for x, y in [(350,160), (520,255), (520,450), (350,550), (180,450), (180,255)]:
        peer(x, y)
    parts.append('</g>')

    # Brackets attach the two relations to whole groups, never individual nodes.
    line('M463 128 H478 V592 H463', '#675776', 1.3)
    line('M613 128 H598 V592 H613', '#496171', 1.3)
    line('M490 327 H586', INK, 1.8, arrow='ink')
    text(538, 307, 'Improve', 30 if compact else 24)
    line('M586 402 H490', BLUE, 1.8, arrow='blue')
    text(538, 441, 'Improve', 30 if compact else 24, BLUE)

    # Four equal cells: physical designs, compute, software, and scientific work.
    text(835, 51, 'Mathematically', 40 if compact else 32)
    text(835, 95, 'verified infra', 40 if compact else 32)
    for cell_x in [625, 845]:
        for cell_y in [128, 378]:
            rect(cell_x, cell_y, 200, 210, '#0d1118', '#263440', 6)
    hardware(725, 225)
    parts.append('<g transform="translate(853.55 -95) scale(.62)">')
    cluster()
    parts.append('</g>')
    software(725, 459)
    science(945, 459)
    for x, y, label in [(725,318,'Hardware'), (945,318,'Compute'),
                        (725,568,'Software'), (945,568,'Science')]:
        text(x, y, label, 38 if compact else 30)

    parts.append('</g>')
parts.append('</svg>\n')
(ROOT / 'docs/assets/economy-overview.svg').write_text(''.join(parts))
