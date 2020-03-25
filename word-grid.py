# Jesse Pelletier
# Purpose: This program populates an N-sized grid with random letters.
# File Name: word-grid.py


import random

def print_grid(G):  # prints the previously generated grid

    for i in range(len(G)):
        for j in range(len(G)):
            print(G[i][j], end = '')
            if j == len(G) - 1:
                print()
            else:
                print(',', end = '')
                

    return 0 

def make_grid(N):  # creates a list of lists of random lower-case letters
                   # that acts as a grid
    outer = []
    num =1

    for i in range(N):
        inner = []
        for j in range(N):
            inner.append(chr(random.randint(97, 122)))
        outer.append(inner)

    return outer


def init():  # initializes the program by seeding the random function,
                # and taking in inputs for the size of the grid and the seed.
    N = int(input())
    S = input()

    random.seed(S)

    return N

def main():  # calls the functions that do the heavy lifting

    num = init()

    print_grid(make_grid(num))

    return 0
    

main()
