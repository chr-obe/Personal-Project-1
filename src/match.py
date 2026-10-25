from src.game import Game
from src.round import Round
from src.strategy import Position, Strategy


class Match:
    def __init__(self, game: Game, strategy_a: Strategy, strategy_b: Strategy) -> None:
        self.game = game
        self.strategy_a = strategy_a
        self.strategy_b = strategy_b
        self._history: list[Round] = []

        # set strategy positions
        strategy_a.position = Position.POSITION_A
        strategy_a.position = Position.POSITION_B

    def run_round(self) -> None:
        # create the round
        round = Round(self.game, self.strategy_a, self.strategy_b)

        # get the strategy decisions and set them in the round
        decision_a = self.strategy_a.decide(self.game, self._history)
        decision_b = self.strategy_b.decide(self.game, self._history)
        round.strategy_a_decision = decision_a
        round.strategy_b_decision = decision_b

        # add the round to history
        self._history.append(round)

        # get the round result
        result = round.result

        if result is None:
            return # this shouldn't happen!

        # adjust scores appropriately
        self.strategy_a.update_score(result[0])
        self.strategy_b.update_score(result[1])


    @property
    def history(self) -> list[Round]:
        return self._history
