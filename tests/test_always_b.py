import unittest

from src.always_b import AlwaysB
from src.game import Game
from src.round import Round
from src.strategy import Decision

# common element among all tests
game = Game([[(-1, -1), (-3, 0)], [(0, -3), (-2, -2)]])

class TestAlwaysB(unittest.TestCase):
    def test_creation(self):
        strategy_a = AlwaysB(1)
        self.assertEqual(strategy_a.id, "always-b#1")

    def test_decide_no_history(self):
        strategy_a = AlwaysB(1)
        decision = strategy_a.decide(game, [])
        self.assertEqual(decision, Decision.CHOICE_B)

    def test_decide_is_consistent(self):
        strategy_a = AlwaysB(1)
        decision = strategy_a.decide(game, [])
        self.assertEqual(decision, Decision.CHOICE_B)
        second_decision = strategy_a.decide(game, [])
        self.assertEqual(second_decision, Decision.CHOICE_B)

    def test_decide_with_history(self):
        strategy_a = AlwaysB(1)
        strategy_b = AlwaysB(2)
        round = Round(game, strategy_a, strategy_b)

        decision = strategy_a.decide(game, [round])
        self.assertEqual(decision, Decision.CHOICE_B)

    def test_decide_consistent_between_games(self):
        strategy_a = AlwaysB(1)
        game_1_decision = strategy_a.decide(game, [])
        new_game = Game([[(0, 0), (0, 1)], [(1, 0), (0, 0)]])
        game_2_decision = strategy_a.decide(new_game, [])
        self.assertEqual(game_1_decision, Decision.CHOICE_B)
        self.assertEqual(game_2_decision, Decision.CHOICE_B)

if __name__ == "__main__":
    unittest.main()
