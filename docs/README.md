# Writing a learning note

Work through one question at a time. Start with an example, explain the modeling
choices, and connect the Lean definitions to the behavior being studied. Include
enough reasoning for a reader to follow the result. Prefer revising an unclear
note to adding another topic. [One paid call](../GiveAndTake/PaidCall/Note.mdx)
is the first example.

## Preview locally

With Node.js 22.12 or newer:

```sh
npm ci
npm run dev
```

Open the URL printed by Astro. Before committing, run `npm run build` and inspect
the changed pages, including at phone width. `npm run preview` serves the built site.

## Keep the note beside its code

Write `GiveAndTake/<Case>/Note.mdx`. Its metadata supplies the navigation:

```yaml
---
title: "Your question"
description: "What the reader will learn."
slug: your-question
order: 2
---
```

Use a unique slug and choose an order for the reading sequence. Add `draft: true`
while a note is unfinished; drafts stay out of the site. The reading lists in
`topics/` are drafts until we develop them into useful explanations.

The page supplies its own title, so start the body with prose. Use ordinary
Markdown for the explanation and `$...$` for inline math. There is no required
section template or minimum number of definitions, theorems, or examples.

## Show the actual Lean source

An empty fence imports a declaration and its proof from a path relative to the note:

````mdx
```lean4 file="./Verification.lean" declaration="execute_preservesFunds"
```
````

Omit `declaration` to include the whole file. The excerpt updates with the code;
a missing declaration fails the build. Use ordinary fences for commands or
small expressions. A long excerpt can be folded:

````mdx
<CodePreview title="Conservation for one action">

```lean4 file="./Verification.lean" declaration="execute_preservesFunds"
```

</CodePreview>
````

Link between published notes using relative source paths. Use GitHub links for
repository files that are not notebook pages. Explain assumptions and what a
result means beside the relevant code.

## Shared documentation format

`clok.json` selects pages; [Overview.mdx](Overview.mdx) is the entry point. The
renderer and styling follow
[`same-but-better`](https://github.com/CloK-Lab/same-but-better/tree/6891ef09fa04860573561909c02841e156bf852c),
adapted under Apache-2.0. The notebook builds independently of other repositories.

Read the notebook on [CloK](https://www.clok.tech/docs/give-and-take), where the
main website supplies the navbar. The local Astro preview shows the document body.

The shared `Sync project documentation` workflow checks registered projects hourly
and proposes updates after their CI passes. Website checks and the deployment
preview must pass before the publication PR is merged. See the
[CloK documentation protocol](CLOK_PROTOCOL.md) for the full contract.
