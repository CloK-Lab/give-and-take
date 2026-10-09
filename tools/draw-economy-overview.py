"""A human-agent workshop builds and improves verified infrastructure."""
from pathlib import Path
from base64 import b64encode
from html import escape
from math import atan2, cos, degrees, hypot, pi, sin
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
BLUE, PURPLE, GOLD = '#86b9d5', '#b6a4c9', '#c6ad79'
INK, MUTED, RULE = '#dfebf4', '#9fa6b2', '#303b47'
parts = ['''<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="920" viewBox="0 0 1080 920" role="img" aria-labelledby="title description">
<title id="title">Verified Infrastructure and DSI Network</title>
<desc id="description">Verified Infrastructure surrounds a human-agent workshop. Hardware, Compute, Software, and Science occupy four workstations. Short production benches carry workpieces between the stations and the central network, with jointed tool arms suggesting fabrication, verification, and improvement. Six human-agent cubes form the outer hexagon, six connected wallet cubes form the inner hexagon, and a blue energy flame sits at the center. Each wallet links to its nearest human-agent pair. Gold denotes allocation inside the network; blue denotes production and infrastructure. The illustration describes research goals rather than achieved capabilities or a literal automated factory.</desc>
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
parts.append('</defs><rect width="1080" height="920" fill="#0a0a0f"/>')


def text(x, y, label, size=24, color=INK, anchor='middle', mono=False):
    parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" class="{"mono" if mono else ""}">{escape(label)}</text>')


def line(d, color=RULE, width=1, opacity=1, arrow=None, fill='none', dashed=False):
    attrs = f' marker-end="url(#{arrow})"' if arrow else ''
    if dashed:
        attrs += ' stroke-dasharray="6 7"'
    parts.append(f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{width}" opacity="{opacity}" stroke-linecap="round" stroke-linejoin="round"{attrs}/>')


def rect(x, y, w, h, fill='none', stroke=RULE, radius=4):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>')


def flame(x, y, scale=4):
    # Lucide's flame outline; see docs/DIAGRAMS.md for source and license.
    icon = ElementTree.parse(ROOT / 'tools/assets/lucide-flame.svg').getroot()
    parts.append(f'<g transform="translate({x - 12 * scale} {y - 12 * scale}) scale({scale})">')
    for shape in icon.findall('{http://www.w3.org/2000/svg}path'):
        line(shape.attrib['d'], BLUE, 1.8 / scale)
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


def wallet(x, y, scale=.65):
    # Reuse the system diagram's wallet geometry at a smaller scale.
    parts.append(f'<g transform="translate({x} {y}) scale({scale})">')
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


def hexagon(cx, cy, radius, color):
    points = [(cx + radius * cos(-pi / 2 + i * pi / 3),
               cy + radius * sin(-pi / 2 + i * pi / 3)) for i in range(6)]
    d = 'M' + ' L'.join(f'{x:.2f} {y:.2f}' for x, y in points) + ' Z'
    line(d, color, 1.8)
    return points


def workpiece(x, y, finished=False):
    # The same small workpiece appears in outline and then on the tooling bed.
    edge = BLUE if finished else '#658394'
    line(f'M{x} {y-10} L{x+11} {y-4} L{x} {y+2} L{x-11} {y-4} Z',
         edge, 1.2, fill='#274454' if finished else '#101820')
    line(f'M{x-11} {y-4} V{y+6} L{x} {y+12} V{y+2} M{x} {y+12} L{x+11} {y+6} V{y-4}',
         edge, 1.2, fill='#152936' if finished else '#101820')
    if finished:
        line(f'M{x+3} {y+4} l2 1 l4 -6', INK, 1.2)


def production_bench(x1, y1, x2, y2):
    # A shallow mechanical bed replaces the former floating connector curve.
    dx, dy = x2-x1, y2-y1
    length = hypot(dx, dy)
    ux, uy = dx/length, dy/length
    nx, ny = -uy*15, ux*15
    corners = [(x1+nx,y1+ny), (x2+nx,y2+ny),
               (x2-nx,y2-ny), (x1-nx,y1-ny)]
    d = 'M' + ' L'.join(f'{x:.2f} {y:.2f}' for x,y in corners) + ' Z'
    line(d, '#496575', 1.3, fill='#13212c')
    # The lower edge gives the workbench a visible thickness.
    low = sorted(corners, key=lambda p:p[1], reverse=True)[:2]
    (ax,ay),(bx,by) = low
    line(f'M{ax} {ay} L{ax} {ay+7} L{bx} {by+7} L{bx} {by}',
         '#3c5263', 1.1, fill='#0d161e')
    for fraction in [.12,.24,.36,.48,.60,.72,.84]:
        x,y=x1+dx*fraction,y1+dy*fraction
        line(f'M{x+nx*.65} {y+ny*.65} L{x-nx*.65} {y-ny*.65}',
             '#304958', .9)


def tooling(x1, y1, x2, y2):
    dx,dy=x2-x1,y2-y1
    bx,by=x1+dx*.27,y1+dy*.27
    jx,jy=x1+dx*.61,y1+dy*.61
    sign=1 if dx>0 else -1
    ex,ey=bx+sign*6,by-43
    wx,wy=jx-sign*22,jy-36
    tx,ty=jx,jy-16
    workpiece(x1+dx*.12,y1+dy*.12)
    workpiece(jx,jy,finished=True)
    # A compact jointed tool arm makes the construction relation visible.
    line(f'M{bx-9} {by} L{bx} {by-5} L{bx+9} {by} L{bx} {by+5} Z',
         BLUE,1.2,fill='#1a2c39')
    arm=f'M{bx} {by-3} L{ex} {ey} L{wx} {wy} L{tx} {ty}'
    line(arm,'#769db4',7)
    line(arm,'#1b2c38',3.5)
    for x,y in [(ex,ey),(wx,wy)]:
        parts.append(f'<circle cx="{x}" cy="{y}" r="4.5" fill="#111d27" stroke="{BLUE}" stroke-width="1.4"/>')
    line(f'M{tx} {ty} l-6 8 v6 M{tx} {ty} l6 8 v6',BLUE,1.6)


for compact in [False, True]:
    parts.append(f'<g class="{"compact" if compact else "wide"}">')
    text(540, 56, 'Verified Infrastructure', 44 if compact else 36)

    # One workshop, with four aligned output stations and short fabrication beds.
    routes=[(462.06,341,266,228), (617.94,341,814,228),
            (462.06,611,266,724), (617.94,611,814,724)]
    for route in routes:
        production_bench(*route)

    # The faint platform anchors the human-agent network in the workshop.
    line('M540 296 L695.88 386 V566 L540 656 L384.12 566 V386 Z',
         '#453d52',1.2,fill='#111017')
    line('M384.12 566 V574 L540 664 L695.88 574 V566 M540 656 V664',
         '#453d52',1.2,fill='#0e0d13')

    cell_width = 256 if compact else 236
    for cx in [162,918]:
        for y in [118,586]:
            rect(cx-cell_width/2,y,cell_width,248,'#0d1118','#263440',6)
    hardware(162,222)
    cluster_scale=.77 if compact else .71
    parts.append(f'<g transform="translate({918-147.5*cluster_scale} {226-496*cluster_scale}) scale({cluster_scale})">')
    cluster()
    parts.append('</g>')
    software(162,690,.94 if compact else .84)
    science(918,690,.96 if compact else .88)
    for x,y,label in [(162,338,'Hardware'),(918,338,'Compute'),
                       (162,806,'Software'),(918,806,'Science')]:
        text(x,y,label,44 if compact else 34)
    for route in routes:
        tooling(*route)

    peers=hexagon(540,476,180,'#675776')
    wallets=hexagon(540,476,103,'#806e4c')
    for (px,py),(wx,wy) in zip(peers,wallets):
        length=hypot(px-wx,py-wy)
        ux,uy=(px-wx)/length,(py-wy)/length
        chain(wx+ux*27,wy+uy*27,px-ux*37,py-uy*37)
    for x,y in wallets:
        wallet(x,y,.4)
    for x,y in peers:
        peer(x,y)
    text(540,225,'DSI Network',42 if compact else 34)
    flame(540,476,3)

    # Allocation stays in the wallet ring; the external benches show production.
    line('M192 877 H224',GOLD,2)
    text(238,885,'Allocation',30 if compact else 25,GOLD,anchor='start')
    line('M490 877 H522',BLUE,2)
    text(536,885,'Build · verify · improve',30 if compact else 25,BLUE,anchor='start')
    parts.append('</g>')
parts.append('</svg>\n')
(ROOT / 'docs/assets/economy-overview.svg').write_text(''.join(parts))
