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

if __name__ == "__main__":
    unittest.main()
