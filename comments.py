def draw_grid(grid, blink_positions=None):
    """
    Draws the Connect 4 grid on the screen, including pieces and optional blinking.
    Time Complexity:
        Best Case: O(ROW_COUNT * COLUMN_COUNT) - Traverse the grid once.
        Average Case: O(ROW_COUNT * COLUMN_COUNT) - Always traverses the entire grid.
        Worst Case: O(ROW_COUNT * COLUMN_COUNT) - Always traverses the entire grid.
    """
    ...

def binary_search_least(arr):
    """
    Finds the round with the least moves using binary search.
    Time Complexity:
        Best Case: O(1) - Array has one element.
        Average Case: O(log n) - Halves the array repeatedly for a typical sorted array.
        Worst Case: O(log n) - Halves the array repeatedly.
    """
    ...

def binary_search_most(arr):
    """
    Finds the round with the most moves using binary search.
    Time Complexity:
        Best Case: O(1) - Array has one element.
        Average Case: O(log n) - Halves the array repeatedly for a typical sorted array.
        Worst Case: O(log n) - Halves the array repeatedly.
    """
    ...

def show_scores():
    """
    Displays the top scorer and lowest scorer from the leaderboard.
    Time Complexity:
        Best Case: O(1) - If no scores are available.
        Average Case: O(1) - Accessing binary search results (precomputed).
        Worst Case: O(1) - Displaying precomputed binary search results.
    """
    ...

def show_restart_popup():
    """
    Displays a pop-up to let the user choose an action after a game ends.
    Time Complexity:
        Best Case: O(1) - Minimal input to choose an option.
        Average Case: O(1) - Typically constant interaction time.
        Worst Case: O(1) - Waiting for valid input.
    """
    ...

def bot_move(grid):
    """
    Determines the bot's move using various heuristics and checks.
    Time Complexity:
        Best Case: O(ROW_COUNT * COLUMN_COUNT) - Minimum checks to find a valid move.
        Average Case: O(ROW_COUNT * COLUMN_COUNT) - Evaluates heuristics for a moderate number of columns.
        Worst Case: O(ROW_COUNT * COLUMN_COUNT * DIRECTIONS) - Evaluates danger heuristics for all positions.
    """
    ...

def quick_sort(arr):
    """
    Sorts an array using the quicksort algorithm.
    Time Complexity:
        Best Case: O(n log n) - Balanced partitioning.
        Average Case: O(n log n) - Random pivot results in near-balanced partitions.
        Worst Case: O(n^2) - Highly unbalanced partitions.
    """
    ...

def show_main_menu():
    """
    Displays the main menu to let the user choose the game mode.
    Time Complexity:
        Best Case: O(1) - Minimal input to select a mode.
        Average Case: O(1) - Typically constant interaction time.
        Worst Case: O(1) - Waiting for valid input.
    """
    ...

def show_winner_popup(winner):
    """
    Displays a pop-up announcing the winner of the game.
    Time Complexity:
        Best Case: O(1) - Fixed number of operations.
        Average Case: O(1) - Always executes the same steps.
        Worst Case: O(1) - Always executes the same steps.
    """
    ...

def start_game():
    """
    Starts the Connect 4 game loop, handles gameplay, and manages game states.
    Time Complexity:
        Best Case: O(ROW_COUNT * COLUMN_COUNT) - A minimal number of moves to finish.
        Average Case: O(ROW_COUNT * COLUMN_COUNT) - Moderate gameplay with average moves.
        Worst Case: O(ROW_COUNT * COLUMN_COUNT) - All grid positions are filled.
    """
    ...

def blink_winning_tokens(grid, winning_positions, piece):
    """
    Blinks the winning tokens to highlight the victory.
    Time Complexity:
        Best Case: O(ROW_COUNT * COLUMN_COUNT) - Minimal iterations for grid updates.
        Average Case: O(ROW_COUNT * COLUMN_COUNT) - Moderate gameplay with average moves.
        Worst Case: O(ROW_COUNT * COLUMN_COUNT) - Updates the entire grid multiple times for blinking.
    """
    ...

def check_win(grid, piece):
    """
    Checks if the given piece has achieved a Connect 4 and returns the winning positions.
    Time Complexity:
        Best Case: O(ROW_COUNT * COLUMN_COUNT) - Early win detection.
        Average Case: O(ROW_COUNT * COLUMN_COUNT) - Scans a moderate number of positions before a win.
        Worst Case: O(ROW_COUNT * COLUMN_COUNT) - Scans all potential win conditions.
    """
    ...

def check_tie(grid):
    """
    Checks if the game is a tie (all positions are filled).
    Time Complexity:
        Best Case: O(COLUMN_COUNT) - Minimal columns to verify.
        Average Case: O(COLUMN_COUNT) - Moderately filled columns.
        Worst Case: O(COLUMN_COUNT) - Always checks the top row of columns.
    """
    ...