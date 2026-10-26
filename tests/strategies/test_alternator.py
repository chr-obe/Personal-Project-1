import unittest

from src.game import Game
from src.match import Match
from src.strategies.alternator import Alternator
from src.strategy import Decision

game = Game([[(10, 10), (1, 8)], [(8, 1), (5, 5)]])

class TestAlternator(unittest.TestCase):
    def test_creation(self):
        strategy_a = Alternator(1)
        self.assertEqual(strategy_a.id, "alternator#1")

    def test_decide_no_history(self):
        strategy_a = Alternator(1)
        decision = strategy_a.decide(game, [])
        self.assertEqual(decision, Decision.CHOICE_A)

    def test_decide_alternates(self):
        strategy_a = Alternator(1)
        strategy_b = Alternator(2)
        match = Match(game, strategy_a, strategy_b)

        match.run_round()
        match.run_round()
        match.run_round()

        self.assertEqual(len(match.history), 3)
        self.assertListEqual(
            match.strategy_a_history,
            [(Decision.CHOICE_A, 10),
             (Decision.CHOICE_B, 5),
             (Decision.CHOICE_A, 10)]
        )


if __name__ == "__main__":
    unittest.main()
