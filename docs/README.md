# The learning notebook

The notebook is an [Astro site with MDX](https://docs.astro.build/en/guides/integrations-guide/mdx/).
It builds to static HTML; no backend is needed. The site lives in `docs/`, while
the writing stays with its code in `GiveAndTake/<CaseName>/Note.mdx`.

Read the [project overview](Overview.mdx) and the
[paid-call note](../GiveAndTake/PaidCall/Note.mdx). Reading topics live in
`docs/topics/*.md`; `clok.json` selects those pages as well as the case notes.

The renderer, styles, and format tools were adapted from
[`same-but-better` at `6891ef0`](https://github.com/CloK-Lab/same-but-better/tree/6891ef09fa04860573561909c02841e156bf852c)
under Apache-2.0. They are kept local so this project builds independently while
following the same CloK documentation conventions.

## Local use

Use Node.js 22.12 or newer and npm:

```sh
npm ci
npm run dev
```

Open the URL printed by Astro, normally `http://localhost:4321`. If another
notebook uses that port, Astro selects an available one. To choose a port, use
`npm run dev -- --port 4322`. To check and build the site, run `npm run build`.
To inspect the generated site, run `npm run preview`. Static output is in `dist/`.
No deployment is configured. The site currently assumes it is served at the
domain root; subdirectory hosting requires configuring Astro's base and updating
root-relative links and assets together.

## Add a note

Create `GiveAndTake/<CaseName>/Note.mdx` beside the implementation. Use this
frontmatter, replacing the values:

```yaml
---
title: "Your note title"
description: "The question this note explores."
slug: your-note-title
order: 2
section: Models
draft: false
---
```

`slug` must be unique and use lowercase letters, numbers, and hyphens. `order`
is a positive integer controlling notebook order. `section` groups consecutive pages in the sidebar. `draft: true` excludes the note from both navigation and generated pages.
All other fields above are required. Invalid metadata fails the build.

The index, document sidebar, and note routes are generated from these files.
The page layout supplies the title; start the body with prose rather than another H1.

A useful note begins with code and a question, works through an example, then
records its reasoning, evidence, and open questions. There is no required section
template. Keep proved claims and measured observations distinct. Unfinished
ideas are welcome when identified as such.

## Show actual source

Use an empty Lean code fence with a source path relative to the note:

````mdx
## First implementation

```lean4 file="./VersionA.lean"
```
````

The path is relative to the note. Both the local preview and CloK's importer
expand the fence from the same source tree; missing files fail the build.
Use ordinary fenced code blocks for expressions, commands, and expected output.
Code blocks support syntax highlighting, line numbers, copy buttons, and metadata
such as `title="Example.lean" {2,4-6}` to name a file and emphasize lines.

## MDX features

Use Markdown tables, task lists, footnotes, links, images, and native `<details>`
for foldable content. For code with a visible preview, wrap a fenced code block
in `<CodePreview title="Formal specification">…</CodePreview>`. The first lines
remain visible with a fade; click the code area to expand and click again to
collapse. Enter and Space work when the area is focused. Selecting or copying
code does not toggle the preview. Write inline math as `$2n$` and display math between `$$`
on separate lines. Second- and third-level headings automatically populate the
page directory; note order supplies previous/next navigation.

These components are available without imports:

````mdx
<Callout type="tip" title="Observation">

Explain a useful detail here. Types: note, tip, warning, important.

</Callout>

<Tabs labels={["Version A", "Version B"]}>
<Tab>

```lean4 title="Example.lean" {1}
def answer := 42
```

</Tab>
<Tab>Compare with the other implementation.</Tab>
</Tabs>

<Steps>
<Step title="Build">Run `lake build`.</Step>
<Step title="Inspect">Read the checked theorem statements.</Step>
</Steps>

<Badge>Proved</Badge>
````

`Tabs` also accepts `defaultIndex={1}`; `Tab` accepts a `title` when the parent
has no `labels`. Tabs support arrow, Home, and End keys.

Link to another note with its source path, e.g. `[One paid call](../GiveAndTake/PaidCall/Note.mdx)`
from the overview. Heading fragments work too. Use relative Markdown images,
e.g. `![Diagram](./diagram.svg)`, to keep figures beside the note. CloK imports
referenced PNG, JPEG, WebP, GIF, AVIF, and SVG files up to 2 MiB each.

For compatibility with CloK, use the provided components and literal props
(strings, numbers, booleans, arrays, or objects). CloK rejects imports, exports,
event handlers, and executable JavaScript expressions. New interactive components
belong in the website and the matching local component map.

## Read on CloK

`clok.json` identifies this project, its overview, and the patterns selecting its pages.
The [CloK protocol v1](CLOK_PROTOCOL.md) defines the shared contract with the website.
Once published, CloK's importer reads these files from a pinned repository
commit, expands source references, and serves them under `/docs/give-and-take`. The main website owns
its navbar, theme, fonts, and home link. No navbar is copied into this repository.

The Astro site is a local writing preview. Publication uses CloK's existing
submission process; pushing these files alone does not publish the notebook.
The content must first be committed and meet the site's publication requirements.

## Visual conventions

`styles/site.css` follows the semantic colors and typography roles of the local
`Clok-Website/src/site/styles/theme.css` and `src/site/typography.css` reference:

- Jost for headings and navigation.
- STIX Two Text for prose.
- IBM Plex Mono for code and metadata.
- Dark surfaces and blue accents. The light palette is available through the
  host website's `html.light` class; this document has no separate theme control.

Fontsource packages serve the fonts locally, so builds never read another
repository. Only document navigation and content are rendered; branding and
site-wide navigation belong to the host website.

## Check a change

```sh
npm run build
git diff --check
```

Inspect the index and changed notes at desktop and phone widths. Check document
links and code overflow. For changes to implementations or
proofs, also run `lake build` from the repository root.

## Mathematical statements

Write paper-style environments on separate lines, outside `$$` and code fences:

```mdx
\begin{definition}[Output specification]
Define the predicate here, using prose and `$...$` or `$$...$$` for formulas.
\end{definition}

\begin{theorem}[Correctness]
State the claim here.
\end{theorem}

\begin{proof}
Give the argument here.
\end{proof}
```

`definition`, `theorem`, and `lemma` share a counter starting at 1 on each page.
Optional titles appear in parentheses. `proof` is unnumbered and ends with a
square. Blocks can contain Markdown, formulas, and document components. These
four environments are expanded by the document renderer; arbitrary LaTeX packages
and `\newtheorem` declarations are not supported. Unmatched blocks fail the build.


To show one declaration beside its mathematical statement, add its written Lean
name to the empty fence:

````mdx
```lean4 file="./Verification.lean" declaration="run_preservesFunds"
```
````

This includes the declaration and its proof directly from the source, with the
relative filename and original line range in the caption. Renaming or removing
the declaration fails the build instead of leaving a stale copy in the note.
The source reader supports declarations starting at column zero, indented bodies,
and `where`, `termination_by`, and `decreasing_by` clauses; it is not a Lean parser.
Use the name as written after `def`, `theorem`, etc. (for example
`Specification.unique`). Missing or ambiguous names fail the build. Use a
whole-file include for source that does not follow this layout. Short definitions
can remain fully visible; wrap longer proofs in `CodePreview`.
