
def recommend_topics(subject, level):
    topics = {
        "Python": {
            "Beginner": ["Variables", "Data Types", "Loops"],
            "Intermediate": ["Functions", "Lists", "Dictionaries"],
            "Advanced": ["OOP", "File Handling", "Decorators"]
        },
        "Machine Learning": {
            "Beginner": ["Introduction to ML", "Types of ML", "Basic Python"],
            "Intermediate": ["Data Preprocessing", "Linear Regression", "Decision Trees"],
            "Advanced": ["Neural Networks", "Deep Learning", "Model Optimization"]
        },
        "Data Structures": {
            "Beginner": ["Arrays", "Strings", "Stacks"],
            "Intermediate": ["Queues", "Linked Lists", "Trees"],
            "Advanced": ["Graphs", "Dynamic Programming", "Hashing"]
        }
    }

    return topics.get(subject, {}).get(level, [])
