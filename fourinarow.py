import pygame
import sys
from time import sleep

"""All the time complexity, best, worst and average case scenarios for
the functions and algorithms all provided in the comments.py file"""

# Initializing Pygame
pygame.init()

#Bounds of our grid
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)

WIDTH = COLUMN_COUNT * SQUARESIZE
HEIGHT = (ROW_COUNT + 1) * SQUARESIZE
SIZE = (WIDTH, HEIGHT)

BLUE = (30, 144, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0,128,0)

# Setting up screen
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Connect 4")

# Fonts for our game
small_font = pygame.font.SysFont("monospace", 30)
medium_font = pygame.font.SysFont("monospace", 40)
large_font = pygame.font.SysFont("monospace", 50)

# Our variables for the game
player_scores = [0, 0]  # Scores for Player 1 and Bot/Player 2
score_record = []  # Tracker to record the scores
game_mode = "bot"  # Establish the gamemode
leaderboard = []  # We use this to track the number of moves for each game

#Drawing the grid and scores
def draw_grid(grid, blink_positions=None):
    screen.fill(WHITE)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, (r + 1) * SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c * SQUARESIZE + SQUARESIZE / 2), int((r + 1) * SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if grid[r][c] == 1:
                color = WHITE if blink_positions and (r, c) in blink_positions else RED
                pygame.draw.circle(screen, color, (int(c * SQUARESIZE + SQUARESIZE / 2), HEIGHT - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif grid[r][c] == 2:
                color = WHITE if blink_positions and (r, c) in blink_positions else YELLOW
                pygame.draw.circle(screen, color, (int(c * SQUARESIZE + SQUARESIZE / 2), HEIGHT - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    # Drawing the score
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
    score_text = medium_font.render(f"P1: {player_scores[0]}  P2/Bot: {player_scores[1]}", True, WHITE)
    screen.blit(score_text, (20, 10))

    pygame.display.update()

def binary_search_least(arr):
    #finding round with least moves, which means the player who won the fastest
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        high = mid
    return arr[low] if arr else None


def binary_search_most(arr):
    #finding round with the most moves, which means the player who took the longest moves to win a game
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high) // 2 + 1
        low = mid
    if arr:
        return arr[high]
    else:
        None


def show_scores(): #function for displaying the top scorer and lowest scorer
    running = True
    screen.fill(BLACK)

    # Creating the title
    title = large_font.render("Scores", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))

    if leaderboard: # Here we are ensuring that the leaderboard is already sorted and mantains this order during insertion
        least_entry = binary_search_least(leaderboard)
        most_entry = binary_search_most(leaderboard)

        # Displaying top scorer
        top_text = small_font.render(f"Top Scorer: {least_entry[0]} with {least_entry[1]} moves", True, GREEN)
        screen.blit(top_text, (WIDTH // 2 - top_text.get_width() // 2, 150))

        # Displaying lowest scorer
        low_text = small_font.render(f"Lowest Scorer: {most_entry[0]} with {most_entry[1]} moves", True, YELLOW)
        screen.blit(low_text, (WIDTH // 2 - low_text.get_width() // 2, 250))

    else:
        # If no scores are available
        no_scores_text = small_font.render("No scores available yet!", True, RED)
        screen.blit(no_scores_text, (WIDTH // 2 - no_scores_text.get_width() // 2, 200))

    # We give the user the option to go back by pressing B
    back_option = small_font.render("Press B to go back", True, RED)
    screen.blit(back_option, (WIDTH // 2 - back_option.get_width() // 2, HEIGHT - 100))

    pygame.display.update()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:  # You have to press 'B' to go back
                    return

def show_restart_popup():
    #Shows a pop-up asking the player what they wanna do next (main menu, leaderboard, play again)
    while True:  # WHILE: Keep showing the popup until a valid option is chosen
        screen.fill(BLACK)
        title = medium_font.render("Do you want to continue?", True, WHITE)
        yes_option = small_font.render("1. Yes", True, RED)
        exit_option = small_font.render("2. Exit", True, YELLOW)
        scores_option = small_font.render("3. Scores", True, BLUE)
        mainmenu_option = small_font.render("4. Main Menu", True, GREEN)

        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
        screen.blit(yes_option, (WIDTH // 2 - yes_option.get_width() // 2, 200))
        screen.blit(exit_option, (WIDTH // 2 - exit_option.get_width() // 2, 300))
        screen.blit(scores_option, (WIDTH // 2 - scores_option.get_width() // 2, 400))
        screen.blit(mainmenu_option, (WIDTH // 2 - mainmenu_option.get_width() // 2, 500))
        pygame.display.update()

        for event in pygame.event.get(): #Menuing options
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # Yes
                    return "restart"
                elif event.key == pygame.K_2:  # Exit
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_3:  # Leaderboard
                    result = show_scores()
                    if result == "back":  # Re-display the restart popup after viewing the leaderboard
                        break  # Exit this loop and re-display the popup
                elif event.key == pygame.K_4:  # Main menu
                    return "main_menu"


def bot_move(grid): #This is the whole bot logic navigating the best move for the bot using Multidimensional arrays
    # MOST IMPORTANTLY: Check if bot has a winning move
    for col in range(COLUMN_COUNT):
        if grid[ROW_COUNT - 1][col] == 0:
            for r in range(ROW_COUNT):
                if grid[r][col] == 0:
                    row = r
                    break
            grid[row][col] = 2
            if check_win(grid, 2):
                grid[row][col] = 0
                return col
            grid[row][col] = 0

    # SECOND: Check if player has a winning move (to block)
    for col in range(COLUMN_COUNT):
        if grid[ROW_COUNT - 1][col] == 0:
            for r in range(ROW_COUNT):
                if grid[r][col] == 0:
                    row = r
                    break
            grid[row][col] = 1
            if check_win(grid, 1):
                grid[row][col] = 0
                return col
            grid[row][col] = 0

    # Arrays that we created to help the bot make a decision
    bot_decisionmaking_1 = []
    bot_decisionmaking_2 = []
    final_bot_decision = []
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)
    ]

    for col in range(COLUMN_COUNT):
        # Check if a column is playable (basically not full)
        if grid[ROW_COUNT - 1][col] == 0:
            # Finds the row where the piece would fall into if it was put in that column
            for r in range(ROW_COUNT):
                if grid[r][col] == 0:
                    row = r
                    break

            """ Calculate counter_1 (This is a counter that will keep track of all the playable positions
            and how much of a threat they are if Player puts a piece here"""
            counter_1 = 0
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < ROW_COUNT and 0 <= new_col < COLUMN_COUNT and grid[new_row][new_col] == 1:
                    counter_1 += 1

            for r in range(row + 1, ROW_COUNT):
                if grid[r][col] == 1:
                    counter_1 += 1

            #Add the place and the threat level into the array as a tupple
            bot_decisionmaking_1.append(((row, col), counter_1))

            """ Calculate counter_2 (This is a counter that will keep track of all the playable positions
                        and how much of an advantage they are if Bot puts a piece here"""
            counter_2 = 0
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < ROW_COUNT and 0 <= new_col < COLUMN_COUNT and grid[new_row][new_col] == 2:
                    counter_2 += 1

            for r in range(row + 1, ROW_COUNT):
                if grid[r][col] == 2:
                    counter_2 += 1

            # Add the place and the benefit level into the array as a tupple
            bot_decisionmaking_2.append(((row, col), counter_2))

    # Sorts the decision arrays using Quick Sort by their respective levels
    bot_decisionmaking_1 = quick_sort(bot_decisionmaking_1)
    bot_decisionmaking_2 = quick_sort(bot_decisionmaking_2)

    # Append the best decisions to the final decision list (The "best" move to block player and "best" move for bot)
    if bot_decisionmaking_1:
        final_bot_decision.append(bot_decisionmaking_1[-1])
    if bot_decisionmaking_2:
        final_bot_decision.append(bot_decisionmaking_2[-1])

    # Sort the final decisions using Quick Sort by the leve of benefit or theat
    final_bot_decision = quick_sort(final_bot_decision)

    # Determine the best move, the one with the highest level
    if final_bot_decision:
        best_move = final_bot_decision[-1][0]
    else:
        best_move = (0, 0)

    return best_move[1]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # We choose the pivot as the middle element as on average its a faster way
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []
    for x in arr:
        if x[1] < pivot[1]:
            left.append(x)
        elif x[1] == pivot[1]:
            middle.append(x)
        else:
            right.append(x)
    return quick_sort(left) + middle + quick_sort(right)

def show_main_menu():
    #Showing the main menu so the user can select a mode
    global game_mode
    running = True
    screen.fill(BLACK)
    title = large_font.render("Connect 4", True, WHITE)
    option1 = medium_font.render("1. Play vs Bot", True, RED)
    option2 = medium_font.render("2. Play 1v1", True, YELLOW)

    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
    screen.blit(option1, (WIDTH // 2 - option1.get_width() // 2, 200))
    screen.blit(option2, (WIDTH // 2 - option2.get_width() // 2, 300))
    pygame.display.update()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_mode = "bot"
                    running = False
                elif event.key == pygame.K_2:
                    game_mode = "1v1"
                    running = False

def show_winner_popup(winner):
    #Showing a pop-up that announces the winner
    popup_running = True
    screen.fill(BLACK)

    if winner == 1:
        title = medium_font.render("Player 1 Wins!", True, RED)
    elif winner == 2:
        title = medium_font.render("Player 2/Bot Wins!", True, YELLOW)
    else:
        title = medium_font.render("It's a Tie!", True, WHITE)

    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - title.get_height() // 2))
    pygame.display.update()
    sleep(2)  # Pause for 2 seconds so user can actually see what it says


def start_game():
    """Start the Connect 4 game."""
    global player_scores, leaderboard, score_record

    # Initializing the game variables
    grid = []
    for _ in range(ROW_COUNT):
        row = [0] * COLUMN_COUNT
        grid.append(row)
    current_player = 1
    moves_stack = []  # Stack to store moves for our added undo functionality
    game_over = False
    move_count = 0  # Track the number of moves in the current game

    draw_grid(grid)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_over:
                if current_player == 1 and event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, SQUARESIZE))
                    posx = event.pos[0]
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
                    pygame.display.update()
                elif current_player == 2 and event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, SQUARESIZE))
                    posx = event.pos[0]
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
                    pygame.display.update()

                if event.type == pygame.KEYDOWN:
                    # Undo functionality with the Keyboard Letter U
                    if event.key == pygame.K_u:
                        # Pops the last two moves from the top of the stack to take those pieces away
                        if len(moves_stack) >= 2:
                            for _ in range(2):
                                row, col, player = moves_stack.pop()
                                grid[row][col] = 0
                            # This is a simple check to not have any player skip turns and have a game bug
                            if moves_stack:
                                current_player = 3 - moves_stack[-1][2]
                            else:
                                1
                            draw_grid(grid)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    posx = event.pos[0]
                    col = int(posx // SQUARESIZE)

                    if col >= 0 and col < COLUMN_COUNT and grid[ROW_COUNT - 1][col] == 0:
                        row = None
                        for r in range(ROW_COUNT):
                            if grid[r][col] == 0:
                                row = r
                                break
                        grid[row][col] = current_player
                        moves_stack.append((row, col, current_player))  # Pushes the moves into the stack
                        move_count += 1  # Increment move count
                        draw_grid(grid)  # Update the grid display
                        pygame.time.wait(500)

                        winning_positions = check_win(grid, current_player)  # Assign winning positions
                        if winning_positions:
                            player_scores[current_player - 1] += 1
                            draw_grid(grid)
                            blink_winning_tokens(grid, winning_positions, current_player)  # Blink tokens for the aesthetics
                            show_winner_popup(current_player)  # Show winner announcement
                            # Add game result to the leaderboard
                            leaderboard.append((f"Player {current_player}", move_count))
                            leaderboard = quick_sort(leaderboard)
                            game_over = True
                        elif check_tie(grid):
                            draw_grid(grid)
                            show_winner_popup(0)  # Tie announcement
                            # Add tie result to the leaderboard
                            leaderboard.append(("Tie", move_count))
                            leaderboard = quick_sort(leaderboard)
                            game_over = True
                        else:
                            draw_grid(grid)
                            current_player = 3 - current_player  # Switch between 1 and 2

            #Overall game logic for connect 4
            if game_mode == "bot" and current_player == 2 and not game_over:
                col = bot_move(grid)
                row = None
                for r in range(ROW_COUNT):
                    if grid[r][col] == 0:
                        row = r
                        break
                grid[row][col] = 2
                moves_stack.append((row, col, 2))  # Push bot's move onto the stack
                move_count += 1  # Increment move count
                draw_grid(grid)  # Update the grid display
                pygame.time.wait(500)
                winning_positions = check_win(grid, current_player)  # Assign winning positions
                if winning_positions:
                    player_scores[1] += 1
                    blink_winning_tokens(grid, winning_positions, current_player)  # Blink tokens
                    show_winner_popup(current_player)
                    leaderboard.append((f"Player {current_player}", move_count))
                    leaderboard = quick_sort(leaderboard)
                    game_over = True
                elif check_tie(grid):
                    draw_grid(grid)
                    show_winner_popup(0)  # Tie announcement
                    # Add tie result to the leaderboard
                    leaderboard.append(("Tie", move_count))
                    leaderboard = quick_sort(leaderboard)
                    game_over = True
                else:
                    draw_grid(grid)
                    current_player = 1

        if game_over:
            restart_option = show_restart_popup()
            if restart_option == "restart":
                start_game()
            elif restart_option == "main_menu":
                show_main_menu()
                start_game()
            else:
                pygame.quit()
                sys.exit()

def blink_winning_tokens(grid, winning_positions, piece):
    #The 4 connected rows will blink to indicate victory
    for _ in range(5):  # Blink 5 times
        draw_grid(grid, blink_positions=winning_positions)  # Highlighting tokens
        pygame.time.wait(300)  # Pause for 300ms
        draw_grid(grid)
        pygame.time.wait(300)  # Pause for 300ms

def check_win(grid, piece):
    # Checking if the given piece has won and returns the winning positions
    # This for loop checks horizontal locations
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            winning_sequence = True
            positions = []
            for i in range(4):
                if grid[r][c + i] != piece:
                    winning_sequence = False
                    break
                positions.append((r, c + i))
            if winning_sequence:
                return positions

    # This for loop checks vertical locations
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT):
            winning_sequence = True
            positions = []
            for i in range(4):
                if grid[r + i][c] != piece:
                    winning_sequence = False
                    break
                positions.append((r + i, c))
            if winning_sequence:
                return positions

    # This for loop checks up sloped diagonal locations
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            winning_sequence = True
            positions = []
            for i in range(4):
                if grid[r + i][c + i] != piece:
                    winning_sequence = False
                    break
                positions.append((r + i, c + i))
            if winning_sequence:
                return positions

    # This for loop checks down sloped diagonal locations
    for r in range(3, ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            winning_sequence = True
            positions = []
            for i in range(4):
                if grid[r - i][c + i] != piece:
                    winning_sequence = False
                    break
                positions.append((r - i, c + i))
            if winning_sequence:
                return positions
    return None

def check_tie(grid):
    # Check if the game ended in a tie by seeing if the grid is full
    for col in range(COLUMN_COUNT):
        if grid[ROW_COUNT - 1][col] == 0:
            return False
    return True

#Runs the game
show_main_menu()
start_game()
