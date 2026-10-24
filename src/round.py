from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.strategy import Strategy

from src.game import Game


class Round:
    def __init__(self, game: Game, strategy_a: Strategy, strategy_b: Strategy) -> None:
        self.game = game
        self.strategy_a = strategy_a
        self.strategy_a_decision: int | None = None
        self.strategy_b = strategy_b
        self.strategy_b_decision: int | None = None
        self.winner: Strategy | None = None
