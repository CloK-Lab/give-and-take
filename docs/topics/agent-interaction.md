---
title: "Agent interaction"
description: "Reading A2A and identifying the meanings of tasks, delegation, and results."
slug: agent-interaction
order: 2
section: Study topics
draft: true
---

Status: reading notes and modeling questions; no A2A implementation yet.
Sources consulted on 2026-10-08.

A2A specifies communication between independent agents, including capability
discovery, messages, tasks, and artifacts. A protocol task's reported completion
and an application's acceptance of its result are distinct concepts.

## Sources

- [A2A introduction](https://a2a-protocol.org/latest/)
- [A2A v1.0.0 specification](https://a2a-protocol.org/v1.0.0/specification/)
- [Life of a task](https://a2a-protocol.org/latest/topics/life-of-a-task/)

## Questions to formalize

- What identifies a request, a task, a result, and an attempted retry?
- Which information does each participant observe?
- What is delegated when an agent calls another agent?
- How do task completion, result acceptance, and payment status relate?
- Can every local call follow its rules while the network fails to make progress?

Use a pinned specification when claiming conformance. Application-specific
acceptance or incentive rules should be labeled as additions.
