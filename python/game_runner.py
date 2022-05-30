import math
from numpy import random

from game import Game


def main():
    not_a_winner = False
    game = Game()
    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    game.roll(math.floor(random.uniform(0, 1) * 6 + 1))
    if math.floor(random.uniform(0, 1) * 10 == 7):
        not_a_winner = game.wrong_answer()
    else:
        not_a_winner = game.was_correctly_answered()

    while (not_a_winner):
        game.roll(math.floor(random.uniform(0, 1) * 6 + 1))
        if math.floor(random.uniform(0, 1) * 10 == 7):
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()


if __name__ == '__main__':
    main()
