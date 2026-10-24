from game import Game
from strategy import Strategy


class Round:
    def __init__(self, game: Game, strategy_a: Strategy, strategy_b: Strategy) -> None:
        self.game = game
        self.strategy_a = strategy_a
        self.strategy_b = strategy_b
        self.winner: Strategy | None = None
