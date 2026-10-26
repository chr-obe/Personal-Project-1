from src.game import Game
from src.round import Round
from src.strategy import Decision, Position, Strategy


class Match:
    def __init__(self, game: Game, strategy_a: Strategy, strategy_b: Strategy) -> None:
        self.game = game
        self.strategy_a = strategy_a
        self.strategy_b = strategy_b
        self._history: list[Round] = []

        # set strategy positions
        strategy_a.position = Position.POSITION_A
        strategy_b.position = Position.POSITION_B

    def run_round(self) -> None:
        # create the round
        current_round = Round(self.game, self.strategy_a, self.strategy_b)

        # get the strategy decisions and set them in the round
        decision_a = self.strategy_a.decide(self.game, self._history)
        decision_b = self.strategy_b.decide(self.game, self._history)
        current_round.strategy_a_decision = decision_a
        current_round.strategy_b_decision = decision_b

        # add the round to history
        self._history.append(current_round)

        # get the round result
        result = current_round.result

        if result is None: # this shouldn't happen!
            raise RuntimeError("at least one strategy has not made a decision somehow")

        # adjust scores appropriately
        self.strategy_a.update_score(result[Position.POSITION_A])
        self.strategy_b.update_score(result[Position.POSITION_B])


    @property
    def history(self) -> list[Round]:
        return self._history

    @property
    def strategy_a_history(self) -> list[tuple[Decision, int]]:
        strategy_history = []
        for match_round in self._history:
            if match_round.result is None:
                raise ValueError("round has no result")
            strategy_history.append((match_round.strategy_a_decision, match_round.result[Position.POSITION_A]))
        return strategy_history

    @property
    def strategy_b_history(self) -> list[tuple[Decision, int]]:
        strategy_history = []
        for match_round in self._history:
            if match_round.result is None:
                raise ValueError("round has no result")
            strategy_history.append((match_round.strategy_b_decision, match_round.result[Position.POSITION_B]))
        return strategy_history
