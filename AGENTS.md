# Working on Give and Take

This is a CloK learning and research project. Its purpose is to build formal
models, specifications, and executable code in Lean for studying agent protocols,
payments, tokenized assets, incentives, and safety.

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
- Keep generated build files, credentials, and local runtime data out of Git.
