"""Write an editable, responsive SVG architecture drawing in CloK's type and colors."""
from pathlib import Path
from base64 import b64encode
from html import escape

root = Path(__file__).resolve().parents[1]
fonts, licenses = [], []
for package, family in [('jost', 'Jost'), ('ibm-plex-mono', 'Plex')]:
    directory = root / 'node_modules/@fontsource' / package
    font = b64encode((directory / 'files' / f'{package}-latin-400-normal.woff2').read_bytes()).decode()
    fonts.append(f"@font-face{{font-family:{family};src:url(data:font/woff2;base64,{font}) format('woff2');font-weight:400}}")
    licenses.append((directory / 'LICENSE').read_text())

blue, purple, gold = '#86b9d5', '#b6a4c9', '#c6ad79'
parts = ['''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="700" viewBox="0 0 1000 700" role="img" aria-labelledby="title description">
<title id="title">Give and take — system modules</title>
<desc id="description">Agent A requests a task from Agent B and submits a spending request to Wallet. Payment combines the provider's terms with wallet authorization and settles the transfer in Ledger. The paid task can then execute and return its result. ETH is the asset. Wallet limits, payment amounts, and ledger balances are measured in wei. The ledger is local Lean state.</desc>
''', '<metadata>' + escape('\n\n'.join(licenses)) + '</metadata>', '<style>', *fonts, '''
text{font-family:Jost,sans-serif;font-weight:400;fill:#dfebf4}
.mono{font-family:Plex,monospace;letter-spacing:1.5px}
.muted{fill:#9fa6b2}.blue{fill:#86b9d5}.purple{fill:#b6a4c9}.gold{fill:#c6ad79}
.compact{display:none}.wire{fill:none;stroke-width:2;stroke-linejoin:round;stroke-linecap:round}
@media(max-width:620px){.wide{display:none}.compact{display:inline}}
</style><defs>
''']
for name, color in [('blue', blue), ('purple', purple), ('gold', gold)]:
    parts.append(f'<marker id="{name}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M2 1 L8 5 L2 9" fill="none" stroke="{color}" stroke-width="1.4"/></marker>')
parts.append('</defs><rect width="1000" height="700" fill="#0a0a0f"/>')

def txt(x, y, value, size=22, css='', anchor='middle'):
    parts.append(f'<text x="{x}" y="{y}" font-size="{size}" class="{css}" text-anchor="{anchor}">{escape(value)}</text>')

def path(d, color='blue', dashed=False, arrow=True):
    col = dict(blue=blue, purple=purple, gold=gold)[color]
    attrs = f' marker-end="url(#{color})"' if arrow else ''
    if dashed:
        attrs += ' stroke-dasharray="5 7"'
    parts.append(f'<path d="{d}" class="wire" stroke="{col}"{attrs}/>')

def box(x,y,w,h,fill,stroke):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1"/>')

def cube(x, y, size, kind, color):
    """Three planar faces and a small line glyph; all geometry remains editable."""
    tones = {
        'blue': ('#172936','#111f2c','#0c1823',blue),
        'purple': ('#2c2237','#21192c','#18121f',purple),
        'gold': ('#3b3220','#2d2518','#211c13',gold)
    }
    top,left,right,edge = tones[color]
    parts.append(f'<g transform="translate({x} {y}) scale({size/50})">')
    parts.append(f'<path d="M0 -55 L50 -27 L0 1 L-50 -27 Z" fill="{top}" stroke="{edge}" stroke-width="1.5"/>')
    parts.append(f'<path d="M-50 -27 L0 1 L0 58 L-50 30 Z" fill="{left}" stroke="{edge}" stroke-width="1.5"/>')
    parts.append(f'<path d="M0 1 L50 -27 L50 30 L0 58 Z" fill="{right}" stroke="{edge}" stroke-width="1.5"/>')
    parts.append(f'<g transform="translate(10 6) skewY(-29)" fill="none" stroke="{edge}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">')
    if kind == 'agent':
        parts.append('<circle cx="15" cy="10" r="6"/><path d="M4 31 V27 C4 16 26 16 26 27 V31"/>')
    elif kind == 'wallet':
        parts.append('<rect x="1" y="3" width="28" height="27" rx="2"/><path d="M21 12 H30 V22 H21 Z"/><circle cx="25" cy="17" r="1"/>')
    elif kind == 'payment':
        parts.append('<path d="M1 10 H27 L22 5 M27 10 L22 15 M29 26 H3 L8 21 M3 26 L8 31"/>')
    else:
        parts.append('<path d="M1 4 H28 V32 H1 Z M7 11 H22 M7 18 H22 M7 25 H17"/>')
    parts.append('</g></g>')

parts.append('<g class="wide">')
txt(24, 34, 'GIVE AND TAKE', 19, 'mono blue', 'start')

box(0,68,294,492,'#0e151d','#263440')
box(326,68,320,492,'#14111b','#322a40')
box(678,68,322,492,'#17150f','#3b3325')
txt(24,105,'01  AGENTS',18,'mono blue','start')
txt(350,105,'02  PAYMENT',18,'mono purple','start')
txt(702,105,'03  SETTLEMENT',18,'mono gold','start')

# Wires are behind the nodes. Directions denote model operations, not imports.
path('M208 186 H429','purple')
txt(318,166,'spend request',19,'purple')
path('M480 281 V356','purple')
txt(492,321,'authorize',18,'purple','start')
path('M207 409 H429','blue')
txt(319,389,'terms',19,'blue')
path('M429 452 H207','blue',True)
txt(319,478,'execute',18,'blue')
path('M534 391 H616 V294 H762','gold')
txt(697,276,'transfer',19,'gold')
path('M762 332 H637 V433 H534','gold',True)
txt(702,359,'paid',19,'gold')
path('M101 409 H47 V186 H101','blue',True)
parts.append('<text transform="translate(32 302) rotate(-90)" font-size="18" class="blue" text-anchor="middle">result</text>')

cube(155,186,43,'agent','blue')
txt(155,262,'Agent A',25)
path('M155 279 V304','blue')
box(99,306,112,36,'#101f2c','#547c96')
txt(155,332,'Task',23,'blue')
path('M155 343 V360','blue')
cube(155,409,43,'agent','blue')
txt(155,488,'Agent B',25)
txt(155,520,'service + result',18,'muted')
cube(480,186,43,'wallet','purple')
txt(480,262,'Wallet',25)
cube(480,409,43,'payment','purple')
txt(480,488,'Payment',25)
txt(480,520,'terms + approval',18,'muted')
cube(840,306,61,'ledger','gold')
txt(840,407,'Ledger',29)
txt(840,439,'balances + nonces',20,'muted')
txt(840,522,'LOCAL STATE',15,'mono gold')

box(0,585,1000,57,'#0f1118','#2b303b')
txt(24,622,'Asset: ETH',24,'','start')
txt(266,622,'Unit: wei',21,'blue','start')
txt(976,621,'Wallet limit · Payment amount · Ledger balance',20,'muted','end')
for x,color,caption in [(24,blue,'Task interaction'),(365,purple,'Spending authority'),(720,gold,'Value transfer')]:
    parts.append(f'<path d="M{x} 676 H{x+26}" stroke="{color}" stroke-width="2"/>')
    txt(x+38,682,caption,18,'muted','start')
parts.append('</g><g class="compact">')

# At phone width, retain the modules and order with larger labels and fewer captions.
txt(34,46,'GIVE AND TAKE',34,'mono blue','start')
for y,fill,stroke in [(76,'#0e151d','#263440'),(227,'#14111b','#322a40'),(378,'#14111b','#322a40'),(529,'#17150f','#3b3325')]:
    box(25,y,950,132,fill,stroke)
cube(118,137,37,'agent','blue')
txt(215,122,'Agent + Task',43,'','start')
txt(215,175,'request → provider → result',33,'blue','start')
path('M118 209 V223','purple')
cube(118,288,37,'wallet','purple')
txt(215,273,'Wallet',43,'','start')
txt(215,326,'owner · asset · limit · recipient',33,'purple','start')
path('M118 360 V374','purple')
cube(118,439,37,'payment','purple')
txt(215,424,'Payment',43,'','start')
txt(215,477,'terms + approval → settle',33,'purple','start')
path('M118 511 V525','gold')
cube(118,590,37,'ledger','gold')
txt(215,575,'Ledger',43,'','start')
txt(215,628,'ETH / wei · balances · nonces',33,'gold','start')
parts.append('</g></svg>\n')

asset = root/'docs/assets/native-system.svg'
asset.write_text(''.join(parts))
