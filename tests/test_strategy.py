import unittest

from src.strategy import Strategy


class TestStrategy(unittest.TestCase):
    def test_strategy_decide_error(self):
        strategy = Strategy("strategy", 1)
        with self.assertRaises(NotImplementedError):
            strategy.decide(None, None)

    def test_get_score(self):
        strategy = Strategy("strategy", 1, 100)
        self.assertEqual(strategy.score, 100)

    def test_change_score(self):
        strategy = Strategy("strategy", 1)
        self.assertEqual(strategy.score, 0)
        strategy.update_score(50)
        self.assertEqual(strategy.score, 50)

    def test_eliminate_strategy(self):
        strategy = Strategy("strategy", 1, 50, True)
        self.assertFalse(strategy.is_eliminated)
        strategy.update_score(-100)
        self.assertEqual(strategy.score, -50)
        self.assertTrue(strategy.is_eliminated)

    def test_strategy_eliminated_at_zero(self):
        strategy = Strategy("strategy", 1, 1, True)
        strategy.update_score(-1)
        self.assertTrue(strategy.is_eliminated)

    def test_score_cannot_update_when_eliminated(self):
        strategy = Strategy("strategy", 1, 1, True)
        strategy.update_score(-1)
        self.assertTrue(strategy.is_eliminated)
        self.assertEqual(strategy.score, 0)
        strategy.update_score(-1)
        self.assertEqual(strategy.score, 0)

    def test_strategy_not_eliminated_unless_allowed(self):
        strategy = Strategy("strategy", 1, 1)
        strategy.update_score(-1)
        self.assertFalse(strategy.is_eliminated)

    def test_clone(self):
        strategy = Strategy("strategy", 1)
        clone = strategy.temp_clone()
        expected = Strategy("strategy", "temp")
        self.assertEqual(clone, expected)

    def test_strategy_id(self):
        strategy = Strategy("strategy", 1)
        self.assertEqual(strategy.id, "strategy#1")

    def test_clone_id(self):
        strategy = Strategy("strategy", 1)
        clone = strategy.temp_clone()
        self.assertEqual(clone.id, "strategy#temp")

if __name__ == "__main__":
    unittest.main()
