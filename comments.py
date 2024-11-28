def draw_grid(grid, blink_positions=None):
    """
    Draws the Connect 4 grid on the screen
    Time Complexity:
        Best Case: O(ROW_COUNT * COLUMN_COUNT) - Traverse the grid to make it.
        Average Case: O(ROW_COUNT * COLUMN_COUNT) - Traverse the grid to make it.
        Worst Case: O(ROW_COUNT * COLUMN_COUNT) - Traverse the grid to make it.
    """

def binary_search_least(arr):
    """
    Finds the round with the least moves using binary search to put in the Scores section
    Time Complexity:
        Best Case: O(1) - A singular game has been played.
        Average Case: O(log n) - Halves the array repeatedly for a typical sorted array binary search.
        Worst Case: O(log n) - Halves the array repeatedly
    """


def binary_search_most(arr):
    """
    Finds the round with the most moves using binary search to put in the Scores section
    Time Complexity:
        Best Case: O(1) - A singular game has been played.
        Average Case: O(log n) - Halves the array repeatedly for a typical sorted array binary search.
        Worst Case: O(log n) - Halves the array repeatedly
    """

def show_scores():
    """
    Displays the top scorer and lowest scorer from the leaderboard.
    Time Complexity:
        Best Case: O(1) - If no scores are available.
        Average Case: O(1) - Accessing binary search results, so the result is already computed.
        Worst Case: O(1) - Accessing binary search results, so the result is already computed.
    """

def show_restart_popup():
    """
    Displays a pop-up to let the user choose an action after a game ends.
    Time Complexity:
        Best Case: O(1) - Input to choose a unique key option.
        Average Case: O(1) - Input to choose a unique key option.
        Worst Case: O(1) - Input to choose a unique key option.
    """

def bot_move(grid):
    """
    Determines the bot's move using various heuristics and checks.
    Time Complexity:
        Best Case: O(ROW_COUNT * COLUMN_COUNT) - Needs to check the possible available and valid moves.
        Average Case: O(ROW_COUNT * COLUMN_COUNT) - Needs to check the possible available and valid moves.
        Worst Case: O(ROW_COUNT * COLUMN_COUNT * DIRECTIONS) - Will have to evaluate the danger and direction for all the valid positions.
    """

def quick_sort(arr):
    """
    Sorts an array using the quicksort algorithm.
    Time Complexity:
        Best Case: O(n log n) - Balanced partitioning.
        Average Case: O(n log n) - Random pivot gives results in near-balanced partitions.
        Worst Case: O(n^2) - Highly unbalanced partitions, and very unlucky scenario.
    """

def show_main_menu():
    """
    Displays the main menu to let the user choose the game mode.
    Time Complexity:
        Best Case: O(1) - Minimal input to select a mode.
        Average Case: O(1) - Typically constant interaction time.
        Worst Case: O(1) - Waiting for valid input.
    """

def show_winner_popup(winner):
    """
    Displays a pop-up announcing the winner of the game.
    Time Complexity:
        Best Case: O(1) - Fixed number of operations.
        Average Case: O(1) - Always executes the same steps.
        Worst Case: O(1) - Always executes the same steps.
    """

def start_game():
    """
    Starts the Connect 4 game loop, handles gameplay, and manages game states.
    Time Complexity:
        Best Case: O(7) - A minimal number of moves to finish, in connect 4 the fastest a game can be is 4 moves by player 1 and 3 moves by player 2.
        Average Case: O((ROW_COUNT * COLUMN_COUNT)/2) - Moderate gameplay with average moves will take about half of the board.
        Worst Case: O(ROW_COUNT * COLUMN_COUNT) - All grid positions are filled and ends in a Tie.
    """


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
