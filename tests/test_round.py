import unittest

from src.game import Game
from src.round import DecisionAlreadyMadeError, Round
from src.strategy import Decision, Strategy

# common elements among all tests to save on code
game = Game([[(-1, -1), (-3, 0)], [(0, -3), (-2, -2)]])
strategy_a = Strategy("strategy", 1)
strategy_b = Strategy("strategy", 2)

class TestRound(unittest.TestCase):
    def test_get_decisions_has_decisions(self):
        round = Round(game, strategy_a, strategy_b)
        round.strategy_a_decision = Decision.CHOICE_A
        round.strategy_b_decision = Decision.CHOICE_A
        self.assertEqual(round.result, (-1, -1))

    def test_get_decisions_one_decision(self):
        round = Round(game, strategy_a, strategy_b)
        round.strategy_a_decision = Decision.CHOICE_A
        self.assertIsNone(round.result)

    def test_get_decisions_no_decision(self):
        round = Round(game, strategy_a, strategy_b)
        self.assertIsNone(round.result)

    def test_overwrite_decision_raises_error(self):
        round = Round(game, strategy_a, strategy_b)
        round.strategy_a_decision = Decision.CHOICE_A
        with self.assertRaises(DecisionAlreadyMadeError):
            round.strategy_a_decision = Decision.CHOICE_B

    def test_get_results_twice(self):
        round = Round(game, strategy_a, strategy_b)
        round.strategy_a_decision = Decision.CHOICE_B
        round.strategy_b_decision = Decision.CHOICE_B

        res = round.result
        self.assertEqual(round.result, res)


if __name__ == "__main__":
    unittest.main()
