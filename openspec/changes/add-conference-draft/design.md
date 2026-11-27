## Context
The existing README.md and DESIGN.md describe a proposal-stage nutrition agent and a deterministic calculator. The manuscript must preserve that distinction.

## Goals / Non-Goals
**Goals:** IEEE conference formatting, traceable sources, explicit equations, architecture figure, honest evaluation plan, reproducible compilation.
**Non-Goals:** Implement live nutrition APIs, claim completed RAG/MCP integration, publish a paper, or fabricate results.

## Decisions
1. Use IEEEtran in conference mode with pdfLaTeX and a self-contained TikZ diagram.
2. Keep references within main.tex to simplify Overleaf import.
3. Describe proposed MCP tools separately from authoring workflow; neither is represented as executed.
4. Retain the existing code and data unchanged. Use an additive GitHub update.
5. Require actual MCP authoring evidence and author metadata before final submission.

## Risks / Trade-offs
Synthetic records do not establish nutritional accuracy. Proposed evaluation requires labelled meals and appropriate privacy safeguards. MCP connectivity and GitHub write permission must be established in the user's environment.
