import unittest

from src.game import Game
from src.match import Match
from src.strategies.randomstrategy import RandomStrategy
from src.strategy import Decision

game = Game([[(-1, -1), (-3, 0)], [(0, -3), (-2, -2)]])

class TestRandomStrategy(unittest.TestCase):
    def test_creation(self):
        strategy = RandomStrategy(1)
        self.assertEqual(strategy.id, "random#1")

    def test_makes_a_decision(self):
        strategy = RandomStrategy(1)
        decision = strategy.decide(game, [])
        self.assertIn(decision, [Decision.CHOICE_A, Decision.CHOICE_B])

    def test_makes_both_decisions_eventually(self):
        strategy_a = RandomStrategy(1)
        strategy_b = RandomStrategy(2)
        match = Match(game, strategy_a, strategy_b)

        for _ in range(100):
            match.run_round()

        decisions = [decision for decision, _ in match.strategy_a_history]

        self.assertTrue(Decision.CHOICE_A in decisions)
        self.assertTrue(Decision.CHOICE_B in decisions)

    def test_seeded_randomness(self):
        strategy_a = RandomStrategy(1, seed=4)
        strategy_b = RandomStrategy(2)

        match = Match(game, strategy_a, strategy_b)

        for _ in range(10):
            match.run_round()

        expected = [
            Decision.CHOICE_A,
            Decision.CHOICE_B,
            Decision.CHOICE_A,
            Decision.CHOICE_B,
            Decision.CHOICE_B,
            Decision.CHOICE_A,
            Decision.CHOICE_A,
            Decision.CHOICE_A,
            Decision.CHOICE_A,
            Decision.CHOICE_B
        ]
        actual = [decision for decision, _ in match.strategy_a_history]

        self.assertListEqual(actual, expected)
