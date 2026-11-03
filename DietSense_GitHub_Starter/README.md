# DietSense

**A Conversational Domain AI Agent for Daily Calorie Intake Analysis**  
**Status: Proposal / early prototype — NOT a completed nutrition AI agent**

DietSense is a proposed nutrition-focused AI agent that accepts natural-language food descriptions, retrieves evidence from nutrition databases, estimates energy and macronutrient intake with uncertainty, tracks daily consumption and offers contextual summaries. Taiwan-specific foods and transparent source attribution are important design goals.

## Proposal scope
- Input: Taiwanese Mandarin/English food descriptions (text first; optional speech later)
- Planned AI: LLM planner, food/portion extraction, tool calling, retrieval-augmented generation (RAG)
- Planned sources: USDA FoodData Central, Taiwan food composition database, curated local-food records
- Analytics: per-food energy and macronutrients; BMR/TDEE; uncertainty ranges and follow-up questions
- Output: daily log, evidence/provenance, summary, recommendations with safety checks

## Repository map
- [`DESIGN.md`](DESIGN.md): authoritative living design document (deliverable ④)
- [`docs/`](docs/): proposal documents, presentation, architecture and flowchart
- [`src/dietsense/`](src/dietsense/): minimal deterministic analytics prototype
- [`data/`](data/): small *synthetic* demonstration data, not validated nutrient values
- [`tests/`](tests/): executable unit tests

## Quick start (Python 3.10+)
```bash
python -m unittest discover -s tests -v
python -m src.dietsense.cli --food demo_rice --grams 150 --weight 70 --height 170 --age 25 --sex male --activity 1.4
```
The CLI is a **calculation-only demonstration**. It does not call an LLM, authenticate to USDA, extract foods from free text or generate medical advice. `demo_rice` is a fictional teaching record.

## Proposal deliverables and planned validation
- Literature review: AI methods + nutrition domain knowledge
- Design artifacts: system architecture, decision loop/exception flow and pseudocode
- Planned evaluation: reference-labelled calorie estimation, tolerance accuracy (±10%, ±20%), logging time, task completion and SUS; prospective case-study protocol subject to recruitment/ethics and feasibility
- Planned target values in original proposal are **hypotheses**, not measured outcomes.

## Safety and privacy
Educational wellness prototype only, not clinical or individualized medical advice. No credentials, participant logs or personal health data should be committed. Store API tokens in environment variables. A single-day intake below a numeric threshold is not sufficient to diagnose an eating disorder or establish an individual's safe intake.

## What comes next
1. Curate legally usable verified nutrition records with source IDs and units.
2. Implement food extraction, database adapters, ranking and evidence logging.
3. Add an LLM controller with bounded tool calls and clarification logic.
4. Evaluate against labelled meals and compare with a manual-entry baseline.
5. Build web UI and user study only after consent/privacy design.

See [DESIGN.md](DESIGN.md) for details. Research statements in the original proposal require independent verification before formal citation.
