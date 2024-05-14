import pokesearch as pklib

from random import randint as rand
from sys import argv

if len(argv) == 2:
    score = 0
    prev = []
    num = int(argv[1])
    for _ in range(num):
        pkmn = rand(1, 386)
        while pkmn in prev:
            pkmn = rand(1, 386)
        pklib.pksearch(str(pkmn))
        guess = input("Who's that Pokemon: ")
        if guess.title() == pklib.pklist[pkmn - 1]:
            print("Yes")
            score += 1
        else:
            print("No")
    print("Final Score is", score, "out of", num)
