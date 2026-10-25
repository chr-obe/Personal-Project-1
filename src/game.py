from src.strategy import Decision, Position


class Game:
    """
        Payoffs format:
                   B0          B1
               -----------|-----------
            A0 | (A0, B0) | (A0, B1) |
               -----------|-----------
            A1 | (A1, B0) | (A1, B1) |
               -----------|-----------

        [[(A0, B0), (A0, B1)], [(A1, B0), (A1, B1)]]
    """
    def __init__(self, payoffs: list[list[tuple[int, int]]], name: str | None = None) -> None:
        if len(payoffs) != 2 or len(payoffs[0]) != 2 or len(payoffs[1]) != 2:
            raise ValueError("game should be a 2x2 matrix")

        self._name = name
        self._payoffs = payoffs

    def get_a_payoff(self, strategy_a_move: Decision, strategy_b_move: Decision) -> int:
        return self._payoffs[strategy_a_move][strategy_b_move][Position.POSITION_A]

    def get_b_payoff(self, strategy_a_move: Decision, strategy_b_move: Decision) -> int:
        return self._payoffs[strategy_a_move][strategy_b_move][Position.POSITION_B]

    @property
    def payoffs(self) -> list[list[tuple[int, int]]]:
        return self._payoffs

    @property
    def strategy_a_payoffs(self) -> list[list[int]]:
        return [
            [self._payoffs[Decision.CHOICE_A][Decision.CHOICE_A][Position.POSITION_A],
             self._payoffs[Decision.CHOICE_A][Decision.CHOICE_B][Position.POSITION_A]],
            [self._payoffs[Decision.CHOICE_B][Decision.CHOICE_A][Position.POSITION_A],
             self._payoffs[Decision.CHOICE_B][Decision.CHOICE_B][Position.POSITION_A]]
        ]

    @property
    def strategy_b_payoffs(self) -> list[list[int]]:
        return [
            [self._payoffs[Decision.CHOICE_A][Decision.CHOICE_A][Position.POSITION_B],
             self._payoffs[Decision.CHOICE_A][Decision.CHOICE_B][Position.POSITION_B]],
            [self._payoffs[Decision.CHOICE_B][Decision.CHOICE_A][Position.POSITION_B],
             self._payoffs[Decision.CHOICE_B][Decision.CHOICE_B][Position.POSITION_B]]
        ]

    @property
    def name(self) -> str:
        if self._name is not None:
            return self._name
        return ""
