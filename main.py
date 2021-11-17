import random

# Creates an array with the given dimensions that is filled with zeros
def dead_state(board_width, board_height):
    board_state = [[0 for x in range(board_width)] for y in range(board_height)]
    return board_state

# Fills the zeros of a dead_state board with 0s and 1s
def random_state(board_width, board_height):
    board_state = dead_state(board_width, board_height)
    for y in range(board_height):
        for x in range(board_width):
            random_number = random.random()
            if random_number >= 0.5:
                cell_state = 0
            else:
                cell_state = 1
            board_state[x][y] = cell_state
    return board_state

# Formats the board state and prints it to the terminal
def render(board_state):
    for y in range(len(board_state) + 1):
        print("--", end = "")
    print()

    for y in range(len(board_state)):
        print("|", end = "")
        for x in range(len(board_state[y])):
            print(str(board_state[x][y]) + " ", end = "")
        print("|")

    for y in range(len(board_state) + 1):
        print("--", end = "")
    print()