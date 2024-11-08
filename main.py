import random as rd
import numpy as np

class Game:
    def __init__(self, size: int):
        self.size: int = size

    def set_size(self, new_size: int):
        self.size: int = new_size
    
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

    def play(self) -> None:
        row: int = int(input('Selecione uma linha: '))
        col: int = int(input('Selecione uma coluna: '))
        action: str = input('Deseja apagar ou selecionar? ')

        match action.lower():
            case 'apagar':
                print(f'O usuário deseja apagar o valor {self.values[row][col]}.')
                if not self.answers[row][col]:
                    print('Valor apagado com sucesso!')
                else :
                    print('Não foi dessa vez.')
            case 'selecionar':
                print(f'O usuário deseja selecionar o valor {self.values[row][col]}.')
                if self.answers[row][col]:
                    print('Valor selecionado com sucesso!')
                else :
                    print('Não foi dessa vez.')
            case _:
                pass



def test() -> None:
    x: Game = Game(5)
    x.start()
    print(f': {x.top_sums}')
    for i, line in enumerate(x.values):
        print(f'{x.side_sums[i]}: {line}')
    x.play()
        

def main() -> None:
    test()

if __name__=='__main__':
    main()