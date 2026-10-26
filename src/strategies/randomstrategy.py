import random

from src.game import Game
from src.round import Round
from src.strategy import Decision, Strategy


class RandomStrategy(Strategy):
    def __init__(self,
                 id: int,
                 starting_score: int = 0,
                 allow_elimination: bool = False,
                 seed: int | None = None) -> None:
        self._rng = random.Random(seed)
        super().__init__("random", id, starting_score, allow_elimination)


    def decide(self, game: Game | None, history: list[Round] | None) -> Decision:
        if game is None or history is None:
            raise ValueError("decision needs a game and history")

        if self._rng.randint(0, 1) == 0:
            return Decision.CHOICE_A
        else:
            return Decision.CHOICE_B
