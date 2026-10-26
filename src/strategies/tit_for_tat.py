from src.game import Game
from src.round import Round
from src.strategy import Decision, Position, Strategy


class TitForTat(Strategy):
    def __init__(self,
                 id: int,
                 starting_score: int = 0,
                 allow_elimination: bool = False) -> None:
        super().__init__("tit-for-tat", id, starting_score, allow_elimination)

    # plays whatever the opponent last played. if opponent didn't play anything, choose A
    def decide(self, game: Game | None, history: list[Round] | None) -> Decision:
        if game is None or history is None:
            raise ValueError("decision needs a game and history")

        if len(history) == 0:
            return Decision.CHOICE_A

        last_round = history[-1]
        if self.position == Position.POSITION_A:
            opponent_last_choice = last_round.strategy_b_decision
            if opponent_last_choice is None: # shouldn't be the case, but just in case
                return Decision.CHOICE_A
            else:
                return opponent_last_choice
        else:
            opponent_last_choice = last_round.strategy_a_decision
            if opponent_last_choice is None:
                return Decision.CHOICE_A
            else:
                return opponent_last_choice
