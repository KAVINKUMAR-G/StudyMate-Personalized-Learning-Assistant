# Project notes

## Problem
Learners often struggle to decide what to study next and may need simple explanations of unfamiliar concepts.

## Proposed solution
StudyMate retrieves relevant notes from a curated knowledge base, remembers a learner's chosen goal and study activity locally, and recommends topics to revisit or explore.

## Core modules
- Human-computer interaction: Streamlit interface with question, plan, progress, and privacy sections.
- Applied ML: TF-IDF text representation and cosine-similarity retrieval.
- Learner memory: SQLite profile and activity records.
- Personalization: goal-aware recommendation ranking adjusted by prior activity.
- Evaluation: retrieval test cases and unit tests.

## Next research-grade improvements
- Expand the knowledge base using verified course materials.
- Collect consented feedback and evaluate recommendation usefulness.
- Compare TF-IDF with sentence embeddings.
- Add a knowledge graph connecting prerequisites and related topics.
- If an LLM is added later, use an optional provider, protect API keys with environment variables, and evaluate groundedness and hallucination rates.

## Demo script
1. Save a learning goal in the sidebar.
2. Ask: "What is supervised learning?"
3. Open the related notes to show retrieval evidence.
4. Mark a suggested topic as studied.
5. Open Progress to show the saved activity.
6. Clear local data to demonstrate user control.
