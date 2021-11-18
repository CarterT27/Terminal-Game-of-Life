import random
import curses
from time import sleep
import sys

file = "./Boards/gosper_glider_gun.txt"

# Creates an array with the given dimensions that is filled with zeros
def dead_state(board_height = 3 , board_width = 3):
    board_state = [[0 for x in range(board_width)] for y in range(board_height)]
    return board_state

# Fills the zeros of a dead_state board with 0s and 1s
def random_state(board_height = 3, board_width = 3):
    board_state = dead_state(board_height, board_width)
    for row in range(board_height):
        for column in range(board_width):
            random_number = random.random()
            if random_number >= 0.5:
                cell_state = 0
            else:
                cell_state = 1
            board_state[row][column] = cell_state
    return board_state

# Formats the board state and prints it to the terminal
def render(board_state, stdscr):
    dead = " "
    live = "O"
    stdscr.clear()
    for column in range(len(board_state[0]) + 1):
        stdscr.addstr("--")
    stdscr.addstr("-\n")

    for row in range(len(board_state)):
        stdscr.addstr("| ")
        for column in range(len(board_state[row])):
            if board_state[row][column] == 0:
                stdscr.addstr(dead + " ")
            else:
                stdscr.addstr(live + " ")
        try:
            stdscr.addstr("|\n")
        except curses.error:
            sys.exit("The board is too big for the terminal. Please resize the terminal and rerun the program or choose a smaller board.")

    for column in range(len(board_state[0]) + 1):
        stdscr.addstr("--")
    stdscr.addstr("-\n")
    stdscr.refresh()

# Calculates and returns the next board state according to the rules of life
def next_board_state(initial_board_state):
    next_board_state = dead_state(len(initial_board_state), len(initial_board_state[0]))

    for row in range(len(initial_board_state)):
        for column in range(len(initial_board_state[row])):
            next_board_state[row][column] = get_next_cell_state(initial_board_state[row][column], get_number_of_live_neighbors(initial_board_state, row, column))
    return next_board_state

# Returns the number of live neighbors given board state, row, and column
def get_number_of_live_neighbors(board_state, row, column):
    number_of_live_neighbors = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            rowi = row + i
            columnj = column + j
            if rowi < 0:
                continue
            if rowi > len(board_state) - 1:
                continue
            if columnj < 0:
                continue
            if columnj > len(board_state[0]) - 1:
                continue
            if board_state[rowi][columnj] == 1:
                number_of_live_neighbors += 1
    number_of_live_neighbors -= board_state[row][column]
    return number_of_live_neighbors

# Returns next cell state based on initial cell state and the number of live neighbors
def get_next_cell_state(initial_cell_state, number_of_live_neighbors):
    next_cell_state = 0
    if initial_cell_state == 1:
        if number_of_live_neighbors in [0, 1]: #Underpopulation
            next_cell_state = 0
        elif number_of_live_neighbors in [2, 3]: #Neighborhood is just right
            next_cell_state = 1
        elif number_of_live_neighbors > 3: #Overpopulation
            next_cell_state = 0
        else:
            next_cell_state = 0
    if initial_cell_state == 0:
        if number_of_live_neighbors == 3: #Reproduction
            next_cell_state = 1
        else:
            next_cell_state = 0

    return next_cell_state

# Loads a board state from the given text file and returns it as an array board state
def load_board_state(file):
    board_state = []
    current_row = []
    lines = []
    with open(file, "r") as f:
        while True:
            c = f.read(1)
            if not c: # End of file
                board_state.append(current_row)
                break
            if c in ["0", "1"]:
                current_row.append(int(c))
            else:
                board_state.append(current_row[:]) # Stupid list references
                current_row.clear()
    return board_state

# Runs the Game of Life in a loop
def run_game(initial_board_state, stdscr):
    render(initial_board_state, stdscr)
    while True:
        following_board_state = next_board_state(initial_board_state)
        initial_board_state = following_board_state
        render(following_board_state, stdscr)
        sleep(0.3)

def main(stdscr):
    if __name__ == "__main__":
        # init_state = random_state(20, 50)
        init_state = load_board_state(file)
        run_game(init_state, stdscr)

curses.wrapper(main)