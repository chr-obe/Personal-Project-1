import unittest

from src.always_a import AlwaysA
from src.always_b import AlwaysB
from src.game import Game
from src.match import Match
from src.round import Round
from src.strategy import Decision

game = Game([[(-1, -1), (-3, 0)], [(0, -3), (-2, -2)]])

class TestMatch(unittest.TestCase):
    def test_create_match_empty_history(self):
        strategy_a = AlwaysA(1)
        strategy_b = AlwaysA(2)

        match = Match(game, strategy_a, strategy_b)
        self.assertListEqual(match.history, [])

    def test_create_match_adds_results(self):
        strategy_a = AlwaysA(1)
        strategy_b = AlwaysA(2)

        match = Match(game, strategy_a, strategy_b)

        expected_round = Round(game, strategy_a, strategy_b)
        expected_round.strategy_a_decision = Decision.CHOICE_A
        expected_round.strategy_b_decision = Decision.CHOICE_A
        _ = expected_round.result # needed since it doesn't have a setter

        match.run_round()

        self.assertListEqual(match.history, [expected_round])

    def test_get_strategy_a_results(self):
        strategy_a = AlwaysA(1)
        strategy_b = AlwaysB(1)

        match = Match(game, strategy_a, strategy_b)

        for _ in range(3):
            match.run_round()

        expected = [(Decision.CHOICE_A, -3), (Decision.CHOICE_A, -3), (Decision.CHOICE_A, -3)]
        self.assertListEqual(match.strategy_a_history, expected)

    def test_get_strategy_b_results(self):
        strategy_a = AlwaysA(1)
        strategy_b = AlwaysB(1)

        match = Match(game, strategy_a, strategy_b)

        for _ in range(3):
            match.run_round()

        expected = [(Decision.CHOICE_B, 0), (Decision.CHOICE_B, 0), (Decision.CHOICE_B, 0)]
        self.assertListEqual(match.strategy_b_history, expected)

if __name__ == "__main__":
    unittest.main()
