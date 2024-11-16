import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)

WIDTH = COLUMN_COUNT * SQUARESIZE
HEIGHT = (ROW_COUNT + 1) * SQUARESIZE
SIZE = (WIDTH, HEIGHT)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Screen
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Connect 4")

# Game variables
grid = [[0 for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
current_player = 1  # Player 1 starts (1 for Red, 2 for Yellow)

# Font
font = pygame.font.SysFont("monospace", 75)


def draw_grid():
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            # Draw the white background squares
            pygame.draw.rect(screen, WHITE, (c * SQUARESIZE, (r + 1) * SQUARESIZE, SQUARESIZE, SQUARESIZE))
            # Draw the black circles (empty spaces)
            pygame.draw.circle(screen, BLACK,
                               (int(c * SQUARESIZE + SQUARESIZE / 2),
                                int((r + 1) * SQUARESIZE + SQUARESIZE / 2)),
                               RADIUS)

    # Draw the pieces
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if grid[r][c] == 1:  # Red pieces
                pygame.draw.circle(screen, RED,
                                   (int(c * SQUARESIZE + SQUARESIZE / 2),
                                    HEIGHT - int(r * SQUARESIZE + SQUARESIZE / 2)),
                                   RADIUS)
            elif grid[r][c] == 2:  # Yellow pieces
                pygame.draw.circle(screen, YELLOW,
                                   (int(c * SQUARESIZE + SQUARESIZE / 2),
                                    HEIGHT - int(r * SQUARESIZE + SQUARESIZE / 2)),
                                   RADIUS)

    pygame.display.update()


def is_valid_location(col):
    return grid[ROW_COUNT - 1][col] == 0


def get_next_open_row(col):
    for r in range(ROW_COUNT):
        if grid[r][col] == 0:
            return r
    return None


def drop_piece(row, col, piece):
    grid[row][col] = piece


def check_win(piece):
    # Horizontal check
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if grid[r][c] == piece and grid[r][c + 1] == piece and grid[r][c + 2] == piece and grid[r][c + 3] == piece:
                return True

    # Vertical check
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT):
            if grid[r][c] == piece and grid[r + 1][c] == piece and grid[r + 2][c] == piece and grid[r + 3][c] == piece:
                return True

    # Positive diagonal check
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            if grid[r][c] == piece and grid[r + 1][c + 1] == piece and grid[r + 2][c + 2] == piece and grid[r + 3][
                c + 3] == piece:
                return True

    # Negative diagonal check
    for r in range(3, ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if grid[r][c] == piece and grid[r - 1][c + 1] == piece and grid[r - 2][c + 2] == piece and grid[r - 3][
                c + 3] == piece:
                return True

    return False


def check_tie():
    return all(grid[ROW_COUNT - 1][col] != 0 for col in range(COLUMN_COUNT))


def bot_move():
    valid_columns = [col for col in range(COLUMN_COUNT) if is_valid_location(col)]
    if valid_columns:
        col = random.choice(valid_columns)
        row = get_next_open_row(col)
        drop_piece(row, col, 2)  # Bot is player 2 (Yellow)
        return col


# Main game loop
game_over = False
draw_grid()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if current_player == 1:  # Human player
            if event.type == pygame.MOUSEMOTION:
                # Draw black rectangle at the top
                pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, SQUARESIZE))
                posx = event.pos[0]
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Draw black rectangle at the top
                pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, SQUARESIZE))

                # Get player's move
                posx = event.pos[0]
                col = int(posx // SQUARESIZE)

                if col >= 0 and col < COLUMN_COUNT and is_valid_location(col):
                    row = get_next_open_row(col)
                    if row is not None:
                        drop_piece(row, col, 1)

                        if check_win(1):
                            label = font.render("Player 1 wins!", 1, RED)
                            screen.blit(label, (40, 10))
                            game_over = True

                        elif check_tie():
                            label = font.render("It's a Tie!", 1, BLACK)
                            screen.blit(label, (40, 10))
                            game_over = True

                        draw_grid()

                        # Switch to bot
                        current_player = 2

    # Bot's turn
    if current_player == 2 and not game_over:
        pygame.time.wait(500)  # Small delay for bot move
        col = bot_move()

        if col is not None:
            if check_win(2):
                label = font.render("Bot wins!", 1, YELLOW)
                screen.blit(label, (40, 10))
                game_over = True

            elif check_tie():
                label = font.render("It's a Tie!", 1, BLACK)
                screen.blit(label, (40, 10))
                game_over = True

            draw_grid()
            # Switch back to human player
            current_player = 1

    if game_over:
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()