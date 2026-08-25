# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: SkillMap
import unittest

class TestSkillMap(unittest.TestCase):
    def test_add_skill(self):
        skillmap = SkillMap()
        skillmap.add_skill("Python", "Advanced")
        self.assertIn("Python", skillmap.skills)
        self.assertEqual(skillmap.skills["Python"].level, "Advanced")

    def test_add_exercise(self):
        skillmap = SkillMap()
        skillmap.add_skill("Python", "Advanced")
        skillmap.add_exercise("Python", "Advanced", "Data Structures")
        self.assertIn("Data Structures", skillmap.exercises["Python"]["Advanced"])

    def test_add_schedule(self):
        skillmap = SkillMap()
        skillmap.add_skill("Python", "Advanced")
        skillmap.add_schedule("Python", "Advanced", "Monday", 10)
        schedule = skillmap.schedule["Python"]["Advanced"]
        self.assertEqual(schedule["Monday"], 10)

    def test_add_progress(self):
        skillmap = SkillMap()
        skillmap.add_skill("Python", "Advanced")
        skillmap.add_exercise("Python", "Advanced", "Data Structures")
        skillmap.add_progress("Python", "Advanced", "Data Structures", 0.7)
        progress = skillmap.progress["Python"]["Advanced"]["Data Structures"]
        self.assertEqual(progress["completed"], 1)
        self.assertEqual(progress["total"], 1)
        self.assertAlmostEqual(progress["score"], 0.7)

if __name__ == "__main__":
    unittest.main()
