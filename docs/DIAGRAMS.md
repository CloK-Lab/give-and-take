# Diagram style

Use the approved [system diagram](assets/native-system.svg) as the visual reference
for ν-DSI. Keep this guide in contributor documentation, not in the
learning notes.

## Visual language

- Dark background, lightly tinted surfaces, outlined shapes, and small line
  icons. Use the reference cube geometry for actors and infrastructure; use the
  diagram forms below when the subject is a quantity, a state, or a sequence.
- Group modules by responsibility. Leave space between groups for labeled arrows.
  Prefer a few meaningful nodes over decorative detail.
- Jost for module names and explanations; IBM Plex Mono for section labels.
  Use short English labels matching the Lean definitions. Keep implementation
  language and project positioning in the introduction, not in diagram headings.
- Thin connectors with open arrowheads. Solid lines show primary requests and
  actions; dashed lines show returned status, results, or execution-ready signals.
  Label each interaction. Do not mix runtime interactions with import dependencies.

| Role | Color |
| --- | --- |
| Canvas | `#0a0a0f` |
| Main text | `#dfebf4` |
| Secondary text | `#9fa6b2` |
| Agents, tasks, physical resources, and service interaction | `#86b9d5` |
| Wallets and spending authority | `#b6a4c9` |
| Ledger and settlement | `#c6ad79` |

Keep these color meanings consistent across diagrams. Pair colors with labels;
color alone must not carry the meaning. Avoid gradients, glow, heavy shadows,
new accent colors, and unrelated project logos.

## Choose a form for the subject

| Subject | Form | What the reader should see |
| --- | --- | --- |
| System responsibilities | Isometric module diagram | Actors, boundaries, and labeled interactions |
| Resource allocation | Proportional flow bands | A stated total, disjoint components, and their units |
| Balance changes | Before/after ledger | The same holders, the transferred amount, and the conserved total |
| Alternatives and lifecycle | State graph | State contents, labeled actions, and separate terminal outcomes |
| Messages over time | Sequence lanes | Sender, recipient, order, and responses |
| Dimensional relations | Annotated equations | Inputs, units, operation, and result |

Give each form the visual weight of the system diagram: a clear group boundary,
a readable heading, prominent values, and supporting details inside the relevant
state or ledger. Use filled bands to show quantities and small glyphs to identify
roles. Avoid adding cubes where a balance row or a formula explains more.

The resource example uses one blue family throughout: tint separates components
without assigning new semantic meanings to purple or gold. Flow widths use the
same scale at both ends. Never join joules, tokens, gas, and money as if they were
one conserved flow; label a tariff or exchange rate when a calculation relates
quantities with different units. Distinguish illustrative inputs from measurements.

[`tools/draw-learning-figures.py`](../tools/draw-learning-figures.py) generates:

- `energy-allocation.svg`: 200 J split across separate GPU, CPU, and network
  devices over the same two-second interval, checked in `Quantities/Checks.lean`.
- `token-transfer.svg`: the 100/0 to 70/30 fixture in `ERC20/Checks.lean`.
- `paid-call-paths.svg`: the two alternative paths in `PaidCall`; the terminal
  double circles and explicit names identify finished states. Arrows are actions,
  not simultaneous flows, and the example has no fees.

The homepage uses [`economy-overview.svg`](assets/economy-overview.svg), generated
by [`tools/draw-economy-overview.py`](../tools/draw-economy-overview.py), for the
project's conceptual scope. Energy belongs inside a connected human–agent
network, with wallets supporting resource allocation. Use the heading
"DSI Network" for this proposed system. Expand DSI as decentralized
superintelligence in the preceding paragraph and explain the project's intended
human–agent collaboration, on-chain allocation, and improvement loop.

The current local layout places four infrastructure areas around two concentric
hexagons. Hardware and Compute sit above; Software and Science sit below. The
outer purple hexagon has six human–agent cubes, each carrying a human glyph and
an agent glyph on its visible faces. The inner gold hexagon has six wallet cubes
connected by plain edges. Link each wallet to its nearest human–agent pair with
two short chain links, leaving space before both cube faces. Place the blue
energy flame at the shared center and "DSI Network" above the rings.

Title the surrounding areas "Verified Infrastructure". Replace floating
external connectors with short blue fabrication benches: shallow isometric beds,
a small workpiece, and a jointed tool arm. These attach the four infrastructure
stations to the network as a whole and suggest building, verifying, and improving
its infrastructure. They are a conceptual production scene, not literal physical
assembly lines for software or science. Draw the benches behind the panels and
network, with no arrows or crossing routes.

Gold remains inside the wallet ring and denotes on-chain tokenomics. Keep all six wallets
connected in a smaller hexagon and linked to their nearest human–agent pair.
The two keys distinguish "Tokenomics on Chain" from "Build · verify · improve".
Wallets represent payment and spending capabilities within an allocation
mechanism; they do not specify a particular chain or a complete allocation rule.

Keep the four infrastructure panels equal and their illustrations distinct:
Hardware is a chip and circuit board, Compute a server cluster, Software a code
window, and Science an experiment. Align label baselines and padding. Compact
rendering widens the panels and enlarges their artwork and labels.

"Superintelligence" describes the project's intended direction, not a claim of
achieved capability. "Verified Infrastructure" states the research goal: specified properties of
scientific models, hardware designs, computations, and software. It is not a certification of
existing outputs, a proof of empirical truth, or an SI-safety guarantee. Digital
records support an allocation mechanism; a record alone does not determine a
fair or correct allocation. The maintenance loop represents improvements, not
recovery of consumed energy. The flame, the experiment, and the server count
are conceptual illustrations, not measurements or a fixed conversion rate.

## Source and layout

Author diagrams as editable SVG. The current drawing is generated by
[`tools/draw-native-system.py`](../tools/draw-native-system.py); reuse its `cube`,
`box`, `path`, and `txt` geometry when adding related figures. Keep the generator
alongside the SVG so changes can be reproduced.
[`tools/draw-ethereum-mechanism.py`](../tools/draw-ethereum-mechanism.py) uses
the same geometry for the Ethereum infrastructure diagram.
[`tools/draw-bitcoin-double-spend.py`](../tools/draw-bitcoin-double-spend.py)
illustrates conflicting payments and competing Bitcoin branches.
[`tools/draw-bitcoin-proof-of-work.py`](../tools/draw-bitcoin-proof-of-work.py)
expands the mining loop and the work needed to rewrite a chain.
[`tools/draw-quantities.py`](../tools/draw-quantities.py) shows gas pricing and
constant-power energy consumption as independent calculations, followed by ETH
denominations. Its gas reference is the diagram in
[Ethereum's gas documentation](https://ethereum.org/developers/docs/gas/#what-is-gas),
credited there to [Ethereum EVM illustrated](https://takenobu-hs.github.io/downloads/ethereum_evm_illustrated.pdf).
The new drawing uses the notebook's geometry and numerical fixtures; no source
artwork is embedded. Keep the energy example separate from the gas example.

[`tools/draw-x402-payment.py`](../tools/draw-x402-payment.py) draws the successful
HTTP v2 `exact` / EIP-3009 `authorization` flow at x402 revision `7f2b2f1`.
Use sequence lanes for the agent, resource server, facilitator, and chain.
Keep the wallet's local policy decision, read-only verification, service
execution, and token settlement separate. Service execution precedes settlement
in this flow. The compact view preserves the same eight steps in vertical cards.
This figure describes the upstream protocol; the current Lean projection models
only payment requirements and integer amount decoding.

[`tools/draw-payment-infrastructure.py`](../tools/draw-payment-infrastructure.py)
generates three source-study figures with illustrative prices and balances:

- `ap2-authorization.svg`: the evidence relationships for an autonomous purchase
  in AP2 v0.2 at `e1ea56d`. Open mandates and the merchant's checkout are inputs
  to the agent's closed mandates. The diagram groups payment verification roles;
  it is not a complete message sequence.
- `gateway-batch-settlement.svg`: USDC balances before acceptance, while pending,
  and after batch confirmation. Three charges total 0.010 USDC. Fees are excluded;
  the service can respond while funds are pending.
- `nevermined-billing.svg`: one successful call under two example plans. A prepaid
  plan consumes three of 100 credits; a pay-as-you-go plan charges USD 0.03.
  Keep the units and the time of charging explicit.

The Circle and Nevermined references were consulted on 9 October 2026. Each
figure has a separate compact layout. The accompanying note states which
upstream behavior is studied and the narrower scope of the executable Lean model.

```sh
python3 tools/draw-native-system.py
python3 tools/draw-ethereum-mechanism.py
python3 tools/draw-bitcoin-double-spend.py
python3 tools/draw-bitcoin-proof-of-work.py
python3 tools/draw-quantities.py
python3 tools/draw-learning-figures.py
python3 tools/draw-economy-overview.py
python3 tools/draw-x402-payment.py
python3 tools/draw-payment-infrastructure.py
npm run build
```

The script uses the fonts already installed by `npm ci`. Embed font data and
its license metadata in the SVG so the figure renders consistently when exported.
Include an SVG title and description, plus meaningful Markdown alt text.

The reference uses a 1000 × 700 canvas, 2-unit connectors, 25–29-unit node titles,
and 18–22-unit annotations. At rendered widths of 620px or less, use a compact
layout with larger labels; do not simply shrink the desktop drawing. Preserve the
module roles and interaction order. Check both notebook and phone-width rendering.

Keep one canonical copy of each diagram in the learning notes. Other pages can
link to it. Every module and interaction shown must be explained by the accompanying
model; mark a proposed component explicitly if it is not implemented.

## Bitcoin mark

The Bitcoin diagram uses the classic orange-and-white mark at the user's request.
The SVG in `tools/assets/bitcoin-logo.svg` comes from
[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Bitcoin.svg), derived
from Bitboy's logo and listed there as public domain (retrieved 2026-10-08).
The generator embeds its original paths; orange is reserved for the mark.

## Energy icon

The homepage uses Lucide's single-outline [flame icon](https://github.com/lucide-icons/lucide/blob/a04f228cd01185e09c188b7227b9600c08c565ec/icons/flame.svg),
retrieved 2026-10-08. The original SVG is in `tools/assets/lucide-flame.svg`;
its ISC license is included in `tools/assets/lucide-LICENSE` and in the generated
SVG metadata. Only scale, stroke width, and color are adapted to the diagram.
Keep the silhouette unfilled and avoid adding inner flames or decorative layers.
