# Working on Give and take

This is a CloK learning and research project. Its purpose is to build formal
models, specifications, and executable code in Lean for studying agent protocols,
payments, tokenized assets, incentives, and safety.

- Prioritize learning: explain one small question clearly before adding topics.
  Start notes with a worked example and explain why each modeling choice matters.
  Keep reader navigation small, leave undeveloped topics as drafts, and avoid
  unnecessary frameworks, checklists, and duplicate explanations.
- Published notes should state what is being studied and explain the subject
  directly. Keep writing advice, learning methods, project positioning, and
  promises about future work in contributor documentation, not reader-facing prose.
- Use English for repository documentation and code comments; converse with the
  user in their preferred language.
- Read README.md, CONTRIBUTING.md, and the guide for the case being changed.
- Keep definitions, specifications, execution, and verification separate.
  The demo and proofs must refer to the same executable Lean definitions.
- Add concrete cases before introducing general frameworks. Do not create empty
  modules for planned features or describe reading notes as implementations.
- Preserve explicit units, assumptions, source versions, and proof boundaries.
  Do not conflate protocol execution, service quality, economic incentives,
  external asset backing, or chain settlement.
- Do not introduce admitted proofs, custom axioms, or native evaluation axioms.
  Audit new public theorems in scripts/Audit.lean.
- Run lake build, lake exe demo, and lake env lean scripts/Audit.lean.
- Keep case notes beside their Lean source as Note.mdx and use source excerpts
  instead of copying definitions or proofs. Follow docs/README.md and clok.json.
- For documentation changes, run npm run build and inspect the affected pages.
  Preserve the shared CloK documentation format and notebook visual conventions.
- Keep generated build files, credentials, and local runtime data out of Git.
