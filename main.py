import random as rd
import numpy as np

class Game:
    def __init__(self, size: int):
        self.size: int = size
    
    def start(self) -> None:
        # Valores a serem mostrado no jogo
        self.values: np.ndarray = np.reshape((rd.choices(range(1, 10), k=self.size**2)), (self.size, self.size))

        # Matriz booleana de resposta
        self.answers: np.ndarray = np.reshape(((self.size**2)*[False]), (self.size, self.size))
        for row in range(self.size):
            self.answers[row][rd.randint(0, self.size-1)] = True
        for col in range(self.size):
            self.answers[rd.randint(0, self.size-1)][col] = True

        # Matriz de resposta
        self.answers_values: np.ndarray = self.values * self.answers

        # Soma lateral e superior
        self.side_sums: list[int] = [int(sum(row)) for row in self.answers_values]
        self.top_sums: list[int] = [int(sum([self.answers_values[i][col] for i in range(self.size)])) for col in range(self.size)]

    def change_size_to(self, new_size: int):
        self.size: int = new_size

def test() -> None:
    x: Game = Game(5)
    x.start()
    print(f': {x.top_sums}')
    for i, line in enumerate(x.values):
        print(f'{x.side_sums[i]}: {line}')
        

def main() -> None:
    test()

if __name__=='__main__':
    main()