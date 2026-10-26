import unittest

from src.alternator import Alternator
from src.game import Game
from src.match import Match
from src.strategy import Decision
from src.tit_for_tat import TitForTat

game = Game([[(10, 10), (1, 8)], [(8, 1), (5, 5)]])

class TestTitForTat(unittest.TestCase):
    def test_creation(self):
        strategy = TitForTat(1)
        self.assertEqual(strategy.id, "tit-for-tat#1")

    def test_chooses_a_at_first(self):
        strategy_a = TitForTat(1)
        strategy_b = Alternator(1)
        match = Match(game, strategy_a, strategy_b)

        match.run_round()
        strategy_a_result = match.strategy_a_history

        self.assertListEqual(strategy_a_result, [(Decision.CHOICE_A, 10)])

    def test_responds_to_opponent(self):
        strategy_a = TitForTat(1)
        strategy_b = Alternator(1)
        match = Match(game, strategy_a, strategy_b)

        for _ in range(3):
            match.run_round()

        expected = [
            (Decision.CHOICE_A, 10),
            (Decision.CHOICE_A, 1),
            (Decision.CHOICE_B, 8)
        ]
        self.assertListEqual(match.strategy_a_history, expected)

    def test_forgives_opponent(self):
        strategy_a = TitForTat(1)
        strategy_b = Alternator(1)
        match = Match(game, strategy_a, strategy_b)

        for _ in range(10):
            match.run_round()

        expected = [
            (Decision.CHOICE_A, 10),
            (Decision.CHOICE_A, 1),
            (Decision.CHOICE_B, 8),
            (Decision.CHOICE_A, 1),
            (Decision.CHOICE_B, 8),
            (Decision.CHOICE_A, 1),
            (Decision.CHOICE_B, 8),
            (Decision.CHOICE_A, 1),
            (Decision.CHOICE_B, 8),
            (Decision.CHOICE_A, 1),
        ]
        self.assertListEqual(match.strategy_a_history, expected)

if __name__ == "__main__":
    unittest.main()
