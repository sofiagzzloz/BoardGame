import pygame
import sys
from time import sleep

# Initializing Pygame
pygame.init()

# Deciding the bounds of the grid
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)

WIDTH = COLUMN_COUNT * SQUARESIZE
HEIGHT = (ROW_COUNT + 1) * SQUARESIZE  # Extra row for hovering pieces
SIZE = (WIDTH, HEIGHT)

BLUE = (30, 144, 255)  
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0,128,0)

# Setting up the screen 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Connect 4 with Leaderboard, Smarter Bot, and Undo")

# Choosing our fonts
small_font = pygame.font.SysFont("monospace", 30)
medium_font = pygame.font.SysFont("monospace", 40)
large_font = pygame.font.SysFont("monospace", 50)

# Our variables for the game
player_scores = [0, 0]  # Scores for Player 1 and Bot/Player 2
score_record = []  #  record of scores
game_mode = "bot"  # Default game mode: "bot" or "1v1"
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

# complexity
# Best case =(1)
# Worst/ Avergae case = O(log n)



def binary_search_least(arr): 
    #finding round with least moves
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        high = mid  
    return arr[low] if arr else None


def binary_search_most(arr):
    #finding round with the most moves 
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2 + 1
        low = mid  
    return arr[high] if arr else None

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

    # Giving the user the option to go back by pressing B
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
    #Show a pop-up asking the player if they want to continue or view leaderboard
    while True:  # Keep showing the popup until a valid option is chosen
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

        for event in pygame.event.get():
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


def bot_move(grid):
    # Complexity:
    # Best case: O(row count: 6)
    #Worst/Average: O(6 x 7 -> column count times row count)
 
    # Priority 1: Check for bot's winning move
    for col in range(COLUMN_COUNT):
        if grid[ROW_COUNT - 1][col] == 0:
            row = next(r for r in range(ROW_COUNT) if grid[r][col] == 0)
            grid[row][col] = 2
            if check_win(grid, 2):
                grid[row][col] = 0
                return col
            grid[row][col] = 0

    # Priority 2: Check for player's winning move to block
    for col in range(COLUMN_COUNT):
        if grid[ROW_COUNT - 1][col] == 0:
            row = next(r for r in range(ROW_COUNT) if grid[r][col] == 0)
            grid[row][col] = 1
            if check_win(grid, 1):
                grid[row][col] = 0
                return col
            grid[row][col] = 0

    # General Danger Evaluation
    bot_decisionmaking_1 = []
    bot_decisionmaking_2 = []
    final_bot_decision = []
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)
    ]

    for col in range(COLUMN_COUNT):
        if grid[ROW_COUNT - 1][col] == 0:
            row = next(r for r in range(ROW_COUNT) if grid[r][col] == 0)

            counter_1 = sum(1 for dr, dc in directions if 0 <= row + dr < ROW_COUNT and 0 <= col + dc < COLUMN_COUNT and grid[row + dr][col + dc] == 1)
            counter_1 += sum(1 for r in range(row + 1, ROW_COUNT) if grid[r][col] == 1)
            bot_decisionmaking_1.append(((row, col), counter_1))

            counter_2 = sum(1 for dr, dc in directions if 0 <= row + dr < ROW_COUNT and 0 <= col + dc < COLUMN_COUNT and grid[row + dr][col + dc] == 2)
            counter_2 += sum(1 for r in range(row + 1, ROW_COUNT) if grid[r][col] == 2)
            bot_decisionmaking_2.append(((row, col), counter_2))

    # Sort decision arrays using Quick Sort
    bot_decisionmaking_1 = quick_sort(bot_decisionmaking_1)
    bot_decisionmaking_2 = quick_sort(bot_decisionmaking_2)

    if bot_decisionmaking_1:
        final_bot_decision.append(bot_decisionmaking_1[-1])
    if bot_decisionmaking_2:
        final_bot_decision.append(bot_decisionmaking_2[-1])

    final_bot_decision = quick_sort(final_bot_decision)
    best_move = final_bot_decision[-1][0] if final_bot_decision else (0, 0)

    return best_move[1]

# Complexity: 
# Best/ Average :O(N * LOG(N))
# Worse case: O(n^2)
def quick_sort(arr): 
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x[1] < pivot[1]]
    middle = [x for x in arr if x[1] == pivot[1]]
    right = [x for x in arr if x[1] > pivot[1]]

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
    grid = [[0 for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
    current_player = 1
    moves_stack = []  # Stack to store moves for undo functionality
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
                    # Undo functionality
                    if event.key == pygame.K_u:
                        # Undo last two moves (player + opponent)
                        if len(moves_stack) >= 2:
                            for _ in range(2):
                                row, col, player = moves_stack.pop()
                                grid[row][col] = 0
                            # Ensure correct player is next
                            current_player = 3 - moves_stack[-1][2] if moves_stack else 1
                            draw_grid(grid)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    posx = event.pos[0]
                    col = int(posx // SQUARESIZE)

                    if col >= 0 and col < COLUMN_COUNT and grid[ROW_COUNT - 1][col] == 0:
                        row = next(r for r in range(ROW_COUNT) if grid[r][col] == 0)
                        grid[row][col] = current_player
                        moves_stack.append((row, col, current_player))  # Push move onto the stack
                        move_count += 1  # Increment move count
                        draw_grid(grid)  # Update the grid display
                        pygame.time.wait(500)

                        winning_positions = check_win(grid, current_player)  # Assign winning positions
                        if winning_positions:
                            player_scores[current_player - 1] += 1
                            draw_grid(grid)
                            blink_winning_tokens(grid, winning_positions, current_player)  # Blink tokens
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

            if game_mode == "bot" and current_player == 2 and not game_over:
                col = bot_move(grid)
                row = next(r for r in range(ROW_COUNT) if grid[r][col] == 0)
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
        draw_grid(grid)  # Draw grid without highlights
        pygame.time.wait(300)  # Pause for 300ms

def check_win(grid, piece):
    # Checking if the given piece has won and returns the winning positions
    # Checking horizontal locations
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if all(grid[r][c + i] == piece for i in range(4)):
                return [(r, c + i) for i in range(4)]

    # Check vertical locations
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT):
            if all(grid[r + i][c] == piece for i in range(4)):
                return [(r + i, c) for i in range(4)]

    # Check positively sloped diagonals
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            if all(grid[r + i][c + i] == piece for i in range(4)):
                return [(r + i, c + i) for i in range(4)]

    # Check negatively sloped diagonals
    for r in range(3, ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if all(grid[r - i][c + i] == piece for i in range(4)):
                return [(r - i, c + i) for i in range(4)]

    return None



def check_tie(grid):
    """Check if the game is a tie."""
    return all(grid[ROW_COUNT - 1][col] != 0 for col in range(COLUMN_COUNT))


# Main program
show_main_menu()
start_game()
