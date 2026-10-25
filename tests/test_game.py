import unittest

from src.game import Game

payoffs: list[list[tuple[int, int]]] = [[(-1, -1), (-3, 0)], [(0, -3), (-2, -2)]]

class TestGame(unittest.TestCase):
    def test_get_strategy_a_payoffs(self):
        game = Game(payoffs)
        expected = [[-1, -3], [0, -2]]
        self.assertListEqual(game.strategy_a_payoffs, expected)

    def test_get_strategy_b_payoffs(self):
        game = Game(payoffs)
        expected = [[-1, 0], [-3, -2]]
        self.assertListEqual(game.strategy_b_payoffs, expected)

    def test_get_correct_payoff(self):
        game = Game(payoffs)
        moves = (0, 1)
        self.assertEqual(game.get_a_payoff(*moves), -3)
        self.assertEqual(game.get_b_payoff(*moves), 0)

    def test_get_name_has_name(self):
        game = Game(payoffs, "Prisoner's Dilemma")
        self.assertEqual(game.name, "Prisoner's Dilemma")

    def test_get_name_no_name(self):
        game = Game(payoffs)
        self.assertEqual(game.name, "")

    def test_game_no_payoffs_raises_error(self):
        with self.assertRaises(ValueError):
            _ = Game([])

    def test_game_too_many_payoffs_raises_error(self):
        with self.assertRaises(ValueError):
            _ = Game([[(0, 0), (-1, 1), (1, -1)],
                         [(1, -1), (0, 0), (-1, 1)],
                         [(-1, 1), (1, -1), (0, 0)]])

if __name__ == "__main__":
    unittest.main()
