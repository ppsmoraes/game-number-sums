import random as rd
import numpy as np

class Game:
    def __init__(self, size: int):
        self.size: int = size

    def start(self, prob: float) -> None:
        self.values: list[list[int]] = []
        self.answers: list[list[bool]] = []
        for row in range(self.size):
            self.values.append(rd.choices(range(1, 10), k=self.size))
            self.answers.append(rd.choices([True, False], k=self.size))
        # self.values[np.random.rand(self.size, self.size) < prob] = None
        # self.top_sums: list[int] = 
        self.side_sums: list[int] = [sum([number for number in line]) for line in self.values]

    def change_size_to(self, new_size: int):
        self.size: int = new_size

def test() -> None:
    x: Game = Game(5)
    x.change_size_to(3)
    x.start(0.2)
    for line in x.values:
        print(line)
    for line in x.answers:
        print(line)

    # print(f'sums: {x.side_sums}')

def main() -> None:
    test()

if __name__=='__main__':
    main()