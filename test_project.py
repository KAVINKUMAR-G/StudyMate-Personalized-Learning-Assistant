import tempfile
import unittest
from pathlib import Path
from memory import StudyMemory
from recommender import StudyEngine

class StudyMateTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = str(Path(self.temp_dir.name) / "test.db")
        self.memory = StudyMemory(self.db_path)
        self.engine = StudyEngine("knowledge_base.csv")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_profile_save_and_read(self):
        self.memory.save_profile("goal", "Prepare for exams")
        self.assertEqual(self.memory.get_profile("goal"), "Prepare for exams")

    def test_activity_is_saved(self):
        self.memory.add_activity("question", "supervised-learning", "test question", 0.8)
        self.assertEqual(len(self.memory.get_activities()), 1)

    def test_retrieval_finds_supervised_learning(self):
        result = self.engine.answer("What is supervised learning?")
        self.assertEqual(result["topic"], "supervised-learning")

    def test_empty_question_is_rejected(self):
        with self.assertRaises(ValueError):
            self.engine.answer(" ")

    def test_clear_memory(self):
        self.memory.save_profile("name", "Test")
        self.memory.add_activity("studied", "python-lists", "done", 1.0)
        self.memory.clear_all()
        self.assertEqual(self.memory.get_profile("name", ""), "")
        self.assertEqual(self.memory.get_activities(), [])

if __name__ == "__main__":
    unittest.main(verbosity=2)
