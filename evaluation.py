from recommender import StudyEngine

TEST_CASES = [
    ("What is supervised learning?", "supervised-learning"),
    ("Explain a decision tree", "decision-tree"),
    ("What does Python list mean?", "python-lists"),
    ("How does linear regression work?", "linear-regression"),
    ("What is model overfitting?", "overfitting"),
]

def run_evaluation():
    engine = StudyEngine("knowledge_base.csv")
    correct = 0
    rows = []
    for question, expected_topic in TEST_CASES:
        result = engine.answer(question)
        passed = result["topic"] == expected_topic
        correct += int(passed)
        rows.append((question, expected_topic, result["topic"], passed, round(result["score"], 3)))
    accuracy = correct / len(TEST_CASES)
    print("StudyMate retrieval evaluation")
    print("-" * 72)
    for question, expected, predicted, passed, score in rows:
        print(f"Q: {question}")
        print(f"Expected: {expected} | Predicted: {predicted} | Score: {score:.3f} | {'PASS' if passed else 'FAIL'}")
    print("-" * 72)
    print(f"Top-1 accuracy: {correct}/{len(TEST_CASES)} = {accuracy:.1%}")
    return accuracy

if __name__ == "__main__":
    run_evaluation()
