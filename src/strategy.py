from game import Game
from round import Round


class Strategy:
    def __init__(self, name: str,
                       id: int,
                       starting_score: int = 0,
                       allow_elimination: bool = False):
        self.id = f"{name}#{id}"
        self._score = starting_score
        self.allow_elimination = allow_elimination
        self._is_eliminated = False

    # This will be overridden by child classes
    # It should return either 0 or 1 (e.g. in the prisoner's dilemma, cooperate or defect)
    def decide(self, game: Game, history: list[Round]) -> int:
        raise NotImplementedError("method is meant to be overridden by its children")

    def update_score(self, change: int) -> None:
        if self._is_eliminated:
            return

        self._score += change
        if self.allow_elimination and self._score <= 0:
            self._is_eliminated = True

    @property
    def score(self) -> int:
        return self._score

    @property
    def is_eliminated(self) -> bool:
        return self._is_eliminated
