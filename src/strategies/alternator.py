from src.game import Game
from src.round import Round
from src.strategy import Decision, Position, Strategy


class Alternator(Strategy):
    def __init__(self,
                 id: int,
                 starting_score: int = 0,
                 allow_elimination: bool = False) -> None:
        super().__init__("alternator", id, starting_score, allow_elimination)

    def decide(self, game: Game | None, history: list[Round] | None) -> Decision:
        if game is None or history is None:
            raise ValueError("decision needs a game and history")

        if len(history) == 0:
            return Decision.CHOICE_A

        last_round = history[-1]

        if self.position == Position.POSITION_A:
            if last_round.strategy_a_decision is None:
                return Decision.CHOICE_A
            else:
                if last_round.strategy_a_decision == Decision.CHOICE_A:
                    return Decision.CHOICE_B
                else:
                    return Decision.CHOICE_A
        else:
            if last_round.strategy_b_decision is None:
                return Decision.CHOICE_A
            else:
                if last_round.strategy_b_decision == Decision.CHOICE_A:
                    return Decision.CHOICE_B
                else:
                    return Decision.CHOICE_A
