import random

def dead_state(board_width, board_height):
    board_state = [[0 for x in range(board_width)] for y in range(board_height)]
    return board_state

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

board = random_state(5,5)
print(board)