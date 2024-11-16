import pygame
import sys
import random
from collections import deque

# Initialize Pygame
pygame.init()

# Constants
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)

WIDTH = COLUMN_COUNT * SQUARESIZE
HEIGHT = (ROW_COUNT + 1) * SQUARESIZE  # Extra row for hovering pieces
SIZE = (WIDTH, HEIGHT)

BLUE = (30, 144, 255)  # RGB for light blue
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Screen setup
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Connect 4 with Restart, Undo, and 1v1 Mode")

# Fonts
small_font = pygame.font.SysFont("monospace", 30)
medium_font = pygame.font.SysFont("monospace", 40)
large_font = pygame.font.SysFont("monospace", 50)

# Game variables
player_scores = [0, 0]  # Scores for Player 1 and Bot/Player 2
score_record = []  # Persistent record of scores
game_mode = "bot"  # Default game mode: "bot" or "1v1"


def draw_grid(grid):
    """Draw the game grid and scores."""
    # Set the background to white
    screen.fill(WHITE)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, (r + 1) * SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c * SQUARESIZE + SQUARESIZE / 2), int((r + 1) * SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if grid[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c * SQUARESIZE + SQUARESIZE / 2), HEIGHT - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif grid[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c * SQUARESIZE + SQUARESIZE / 2), HEIGHT - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    # Draw the score
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
    score_text = medium_font.render(f"P1: {player_scores[0]}  P2/Bot: {player_scores[1]}", True, WHITE)
    screen.blit(score_text, (20, 10))

    pygame.display.update()


def show_popup():
    """Show a pop-up asking the player if they want to continue."""
    popup_running = True
    screen.fill(BLACK)
    title = medium_font.render("Do you want to continue?", True, WHITE)
    yes_option = small_font.render("1. Yes", True, RED)
    exit_option = small_font.render("2. Exit", True, YELLOW)

    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
    screen.blit(yes_option, (WIDTH // 2 - yes_option.get_width() // 2, 200))
    screen.blit(exit_option, (WIDTH // 2 - exit_option.get_width() // 2, 300))
    pygame.display.update()

    while popup_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # Yes
                    popup_running = False
                    return True
                elif event.key == pygame.K_2:  # Exit
                    pygame.quit()
                    sys.exit()


def show_main_menu():
    """Show the main menu for game mode selection."""
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


def start_game():
    """Start the Connect 4 game."""
    global player_scores, score_record

    # Initialize game variables
    grid = [[0 for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
    current_player = 1
    moves_stack = []  # Stack to store moves for undo functionality
    game_over = False

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
                        # Undo both moves if two or more moves exist
                        if len(moves_stack) >= 2:
                            for _ in range(2):  # Remove last two moves
                                last_move = moves_stack.pop()
                                row, col, player = last_move
                                grid[row][col] = 0  # Remove the piece from the grid
                            current_player = 1  # Revert to player's turn
                            draw_grid(grid)
                        elif len(moves_stack) == 1:  # Undo only one move if only one exists
                            last_move = moves_stack.pop()
                            row, col, player = last_move
                            grid[row][col] = 0
                            current_player = player
                            draw_grid(grid)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    posx = event.pos[0]
                    col = int(posx // SQUARESIZE)

                    if col >= 0 and col < COLUMN_COUNT and grid[ROW_COUNT - 1][col] == 0:
                        row = next(r for r in range(ROW_COUNT) if grid[r][col] == 0)
                        grid[row][col] = current_player
                        moves_stack.append((row, col, current_player))  # Push move onto the stack

                        if check_win(grid, current_player):
                            player_scores[current_player - 1] += 1
                            draw_grid(grid)
                            game_over = True
                        elif check_tie(grid):
                            draw_grid(grid)
                            game_over = True
                        else:
                            draw_grid(grid)
                            current_player = 3 - current_player  # Switch between 1 and 2

            if game_mode == "bot" and current_player == 2 and not game_over:
                pygame.time.wait(500)
                col = random.choice([c for c in range(COLUMN_COUNT) if grid[ROW_COUNT - 1][c] == 0])
                row = next(r for r in range(ROW_COUNT) if grid[r][col] == 0)
                grid[row][col] = 2
                moves_stack.append((row, col, current_player))  # Push bot's move onto the stack

                if check_win(grid, 2):
                    player_scores[1] += 1
                    draw_grid(grid)
                    game_over = True
                elif check_tie(grid):
                    draw_grid(grid)
                    game_over = True
                else:
                    draw_grid(grid)
                    current_player = 1

        if game_over:
            if show_popup():
                start_game()
            else:
                pygame.quit()
                sys.exit()


def check_win(grid, piece):
    """Check if the given piece has won."""
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if all(grid[r][c + i] == piece for i in range(4)):
                return True

    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT):
            if all(grid[r + i][c] == piece for i in range(4)):
                return True

    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            if all(grid[r + i][c + i] == piece for i in range(4)):
                return True

    for r in range(3, ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if all(grid[r - i][c + i] == piece for i in range(4)):
                return True

    return False


def check_tie(grid):
    """Check if the game is a tie."""
    return all(grid[ROW_COUNT - 1][col] != 0 for col in range(COLUMN_COUNT))


# Main program
show_main_menu()
start_game()