import numpy as np
from IPython.display import clear_output
import time
import seaborn as sns
import matplotlib.pyplot as plt


def update_board(current_board):
    # your code here ...
    rows = len(current_board)
    cols = len(current_board[0])
    updated_board = [[0 for _ in range(cols)] for _ in range(rows)] # Initialize a new empty grid

    for r in range(rows):
        for c in range(cols):
            live_neighbors = 0
            # Loop through the 8 neighbors of the cell (r, c)
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (i == 0 and j == 0): # Skip the cell itself
                        continue
                    # Check if the neighbor is within the grid boundaries
                    if (0 <= r + i < rows and 0 <= c + j < cols):
                        # Add the neighbor's state to the count
                        live_neighbors += current_board[r + i][c + j]

            # Apply the rules to determine the state of the cell in the new grid
            if current_board[r][c] == 1: # If the cell is alive
                if live_neighbors < 2 or live_neighbors > 3:
                    updated_board[r][c] = 0 # Dies by underpopulation or overpopulation
                else:
                    updated_board[r][c] = 1 # Lives on
            else: # If the cell is dead
                if live_neighbors == 3:
                    updated_board[r][c] = 1 # Becomes alive by reproduction
                else:
                    updated_board[r][c] = 0 # Remains dead

    # updated_board = current_board

    return updated_board




def show_game(game_board, n_steps=10, pause=0.5):
    """
    Show `n_steps` of Conway's Game of Life, given the `update_board` function.

    Parameters
    ----------
    game_board : numpy.ndarray
        A binary array representing the initial starting conditions for Conway's Game of Life. In this array, ` represents a "living" cell and 0 represents a "dead" cell.
    n_steps : int, optional
        Number of game steps to run through, by default 10
    pause : float, optional
        Number of seconds to wait between steps, by default 0.5
    """
    for step in range(n_steps):
        clear_output(wait=True)

        # update board
        game_board = update_board(game_board)

        # show board
        sns.heatmap(game_board, cmap='plasma', cbar=False, square=True)
        plt.title(f'Board State at Step {step + 1}')
        plt.show()

        # wait for the next step
        if step + 1 < n_steps:
            time.sleep(pause)