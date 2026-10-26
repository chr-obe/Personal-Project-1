import unittest

from src.game import Game
from src.round import Round
from src.strategies.always_a import AlwaysA
from src.strategy import Decision

# common element among all tests
game = Game([[(-1, -1), (-3, 0)], [(0, -3), (-2, -2)]])

class TestAlwaysA(unittest.TestCase):
    def test_creation(self):
        strategy_a = AlwaysA(1)
        self.assertEqual(strategy_a.id, "always-a#1")

    def test_decide_no_history(self):
        strategy_a = AlwaysA(1)
        decision = strategy_a.decide(game, [])
        self.assertEqual(decision, Decision.CHOICE_A)

    def test_decide_is_consistent(self):
        strategy_a = AlwaysA(1)
        decision = strategy_a.decide(game, [])
        self.assertEqual(decision, Decision.CHOICE_A)
        second_decision = strategy_a.decide(game, [])
        self.assertEqual(second_decision, Decision.CHOICE_A)

    def test_decide_with_history(self):
        strategy_a = AlwaysA(1)
        strategy_b = AlwaysA(2)
        round = Round(game, strategy_a, strategy_b)

        decision = strategy_a.decide(game, [round])
        self.assertEqual(decision, Decision.CHOICE_A)

    def test_decide_consistent_between_games(self):
        strategy_a = AlwaysA(1)
        game_1_decision = strategy_a.decide(game, [])
        new_game = Game([[(0, 0), (0, 1)], [(1, 0), (0, 0)]])
        game_2_decision = strategy_a.decide(new_game, [])
        self.assertEqual(game_1_decision, Decision.CHOICE_A)
        self.assertEqual(game_2_decision, Decision.CHOICE_A)

if __name__ == "__main__":
    unittest.main()
