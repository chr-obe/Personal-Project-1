from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.strategy import Decision, Strategy

from src.game import Game
from src.strategy import Decision


@dataclass
class Round:
    _game: Game
    strategy_a: Strategy
    strategy_b: Strategy
    _strategy_a_decision: Decision | None = field(default=None, init=False)
    _strategy_b_decision: Decision | None = field(default=None, init=False)
    _result: tuple[int, int] | None = field(default=None, init=False)

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
    def strategy_a_decision(self, decision: Decision) -> None:
        if self._strategy_a_decision is not None:
            raise DecisionAlreadyMadeError
        self._strategy_a_decision = decision

    @property
    def strategy_b_decision(self) -> int | None:
        return self._strategy_b_decision

    @strategy_b_decision.setter
    def strategy_b_decision(self, decision: Decision) -> None:
        if self.strategy_b_decision is not None:
            raise DecisionAlreadyMadeError
        self._strategy_b_decision = decision

class DecisionAlreadyMadeError(Exception):
    def __init__(self, message: str | None = None):
        super().__init__(message)
