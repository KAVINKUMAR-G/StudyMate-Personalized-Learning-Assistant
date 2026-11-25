# StudyMate – Personalized Learning Assistant

## About the Project
StudyMate is a personalized learning assistant prototype built using Python and Machine Learning. It helps students understand topics, track learning activities, and discover relevant topics to study next.

## Key Features
- **Student Profile:** Save the learner's name and learning goal.
- **Question Answering:** Retrieve relevant notes and provide simple explanations.
- **Personalized Recommendations:** Suggest topics based on learning goals and previous activities.
- **Progress Tracking:** Record questions and completed topics.
- **Local Memory:** Store learner profile and activity data using SQLite.
- **Retrieval Evaluation:** Test how effectively the system retrieves relevant learning notes.

## Technologies Used
- Python
- Streamlit
- SQLite
- Pandas
- Scikit-learn
- TF-IDF
- Cosine Similarity

## How It Works
1. The student enters a learning question.
2. StudyMate searches its built-in knowledge base.
3. It retrieves the most relevant notes using TF-IDF and cosine similarity.
4. It displays a simple explanation and related notes.
5. Learning activities are saved locally.
6. The system uses the learning goal and activity history to recommend topics.

## Installation

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python -m streamlit run app.py
```

## Project Scope
This is an educational prototype that uses a curated local knowledge base and retrieval-based explanations. It does not currently use an external LLM or live internet search.

## Author
Kavinkumar G.
## Live Demo

Try StudyMate here:

[Launch StudyMate](https://studymate-personalized-learning-assistant-mxchnqm5aesxcnhdm5mr.streamlit.app)

## Developer

**Kavinkumar G.**

Personalized Learning Assistant built using Python, Streamlit, SQLite and Machine Learning.
