class Game:
    def __init__(self, payoffs: list[list[tuple[int, int]]]) -> None:
        self.payoffs = payoffs
        self.strategy_a_payoffs: list[list[int]] = [
            [
                payoffs[0][0][0],
                payoffs[0][1][0],
            ],
            [
                payoffs[1][0][0],
                payoffs[1][1][0],
            ],
        ]
        self.strategy_b_payoffs: list[list[int]] = [
            [
                payoffs[0][0][1],
                payoffs[0][1][1],
            ],
            [
                payoffs[1][0][1],
                payoffs[1][1][1],
            ],
        ]
