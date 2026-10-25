from src.game import Game
from src.round import Round
from src.strategy import Decision, Strategy


class AlwaysA(Strategy):
    def __init__(self,
                 id: int,
                 starting_score: int = 0,
                 allow_elimination: bool = False) -> None:
        super().__init__("always-a", id, starting_score, allow_elimination)

    def decide(self, game: Game | None, history: list[Round] | None) -> Decision:
        if game is None or history is None:
            raise ValueError("decision needs a game and history")

        return Decision.CHOICE_A
