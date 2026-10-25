from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.strategy import Strategy

from src.game import Game


class Round:
    def __init__(self, game: Game,
                       strategy_a: Strategy,
                       strategy_b: Strategy,) -> None:
        self._game = game
        self.strategy_a = strategy_a
        self._strategy_a_decision: int | None = None
        self.strategy_b = strategy_b
        self._strategy_b_decision: int | None = None
        self._result: tuple[int, int] | None = None

    @property
    def result(self) -> tuple[int, int] | None:
        if self._result is not None:
            return self._result

        if self._strategy_a_decision is None or self._strategy_b_decision is None:
            return None

        moves = (self._strategy_a_decision, self._strategy_b_decision)
        a_score = self._game.get_a_payoff(*moves)
        b_score = self._game.get_b_payoff(*moves)

        self._result = (a_score, b_score)
        return self._result

    @property
    def strategy_a_decision(self) -> int | None:
        return self._strategy_a_decision

    @strategy_a_decision.setter
    def strategy_a_decision(self, decision: int) -> None:
        if self._strategy_a_decision is not None:
            raise DecisionAlreadyMadeError
        if decision not in [0, 1]:
            raise ValueError("invalid decision: must be 0 or 1")
        self._strategy_a_decision = decision

    @property
    def strategy_b_decision(self) -> int | None:
        return self._strategy_b_decision

    @strategy_b_decision.setter
    def strategy_b_decision(self, decision: int) -> None:
        if self.strategy_b_decision is not None:
            raise DecisionAlreadyMadeError
        if decision not in [0, 1]:
            raise ValueError("invalid decision: must be 0 or 1")
        self._strategy_b_decision = decision

class DecisionAlreadyMadeError(Exception):
    def __init__(self, message: str | None = None):
        super().__init__(message)
