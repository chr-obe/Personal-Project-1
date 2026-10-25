from __future__ import annotations

from enum import IntEnum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game import Game
    from src.round import Round


class Strategy:
    def __init__(self, name: str,
                       id: int,
                       starting_score: int = 0,
                       allow_elimination: bool = False):
        self._id = f"{name}#{id}"
        self._score = starting_score
        self._allow_elimination = allow_elimination
        self._is_eliminated = False

    # This will be overridden by child classes
    # It should return either 0 or 1 (e.g. in the prisoner's dilemma, cooperate or defect)
    def decide(self, game: Game | None, history: list[Round] | None) -> Decision:
        raise NotImplementedError("method is meant to be overridden by its children")

    def update_score(self, change: int) -> None:
        if self._is_eliminated:
            return

        self._score += change
        if self._allow_elimination and self._score <= 0:
            self._is_eliminated = True

    @property
    def score(self) -> int:
        return self._score

    @property
    def is_eliminated(self) -> bool:
        return self._is_eliminated

    @property
    def id(self) -> str:
        return self._id

    @property
    def position(self) -> Position:
        return self._position

    @position.setter
    def position(self, position: Position) -> None:
        self._position = position


class Position(IntEnum):
    POSITION_A = 0
    POSITION_B = 1

class Decision(IntEnum):
    CHOICE_A = 0
    CHOICE_B = 1
