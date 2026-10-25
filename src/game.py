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
        self._strategy_a_payoffs: list[list[int]] = [
            [
                payoffs[0][0][0],
                payoffs[0][1][0],
            ],
            [
                payoffs[1][0][0],
                payoffs[1][1][0],
            ],
        ]
        self._strategy_b_payoffs: list[list[int]] = [
            [
                payoffs[0][0][1],
                payoffs[0][1][1],
            ],
            [
                payoffs[1][0][1],
                payoffs[1][1][1],
            ],
        ]

    def get_a_payoff(self, strategy_a_move: int, strategy_b_move: int) -> int:
        return self._strategy_a_payoffs[strategy_a_move][strategy_b_move]

    def get_b_payoff(self, strategy_a_move: int, strategy_b_move: int) -> int:
        return self._strategy_b_payoffs[strategy_a_move][strategy_b_move]

    @property
    def strategy_a_payoffs(self) -> list[list[int]]:
        return self._strategy_a_payoffs

    @property
    def strategy_b_payoffs(self) -> list[list[int]]:
        return self._strategy_b_payoffs

    @property
    def name(self) -> str:
        if self._name is not None:
            return self._name
        return ""
