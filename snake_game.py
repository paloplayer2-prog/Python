import pygame
import random
import math

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Google Snake - Python Edition")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 24, bold=True)
game_over_font = pygame.font.SysFont("Arial", 42, bold=True)

# Colors
GRASS_LIGHT = (170, 215, 81)
GRASS_DARK = (162, 209, 73)
SNAKE_COLOR = (71, 113, 234)
APPLE_COLOR = (231, 71, 29)
CAKE_COLOR = (255, 255, 255)
CAKE_FROSTING_COLOR = (255, 192, 203)
BROWN = (101, 67, 33)
LEAF_GREEN = (34, 139, 34)
WHITE = (255, 255, 255)
EYE_WHITE = (255, 255, 255)
EYE_BLACK = (0, 0, 0)
SNAKE_SIZE = 20


GRID_COLS = SCREEN_WIDTH // SNAKE_SIZE
GRID_ROWS = SCREEN_HEIGHT // SNAKE_SIZE

def draw_checkerboard():
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            color = GRASS_LIGHT if (row + col) % 2 == 0 else GRASS_DARK
            pygame.draw.rect(screen, color, [col * SNAKE_SIZE, row * SNAKE_SIZE, SNAKE_SIZE, SNAKE_SIZE])

def draw_cake(x, y):
    center_x = x + SNAKE_SIZE // 2
    center_y = y + SNAKE_SIZE // 2
    pygame.draw.rect(screen, CAKE_COLOR, [center_x - 8, center_y - 8, 16, 16], border_radius=4)
    pygame.draw.rect(screen, CAKE_FROSTING_COLOR, [center_x - 8, center_y - 8, 16, 6], border_radius=4)


def draw_apple(x, y):
    center_x = x + SNAKE_SIZE // 2
    center_y = y + SNAKE_SIZE // 2
    pygame.draw.circle(screen, APPLE_COLOR, (center_x, center_y + 1), 8)
    pygame.draw.line(screen, BROWN, (center_x, center_y - 7), (center_x + 2, center_y - 10), 2)
    pygame.draw.circle(screen, LEAF_GREEN, (center_x + 4, center_y - 8), 2)

def draw_snake(body, direction):
    for segment in body:
        pygame.draw.rect(screen, SNAKE_COLOR, [segment[0] + 1, segment[1] + 1, SNAKE_SIZE - 2, SNAKE_SIZE - 2], border_radius=7)

    if len(body) > 0:
        hx, hy = body[-1][0], body[-1][1]
        if direction == "UP":
            eye1, eye2 = (hx + 5, hy + 5), (hx + 15, hy + 5)
        elif direction == "DOWN":
            eye1, eye2 = (hx + 5, hy + 15), (hx + 15, hy + 15)
        elif direction == "LEFT":
            eye1, eye2 = (hx + 5, hy + 5), (hx + 5, hy + 15)
        else:
            eye1, eye2 = (hx + 15, hy + 5), (hx + 15, hy + 15)

        pygame.draw.circle(screen, EYE_WHITE, eye1, 3)
        pygame.draw.circle(screen, EYE_WHITE, eye2, 3)
        pygame.draw.circle(screen, EYE_BLACK, eye1, 1)
        pygame.draw.circle(screen, EYE_BLACK, eye2, 1)


def spawn_food(snake_body):
    occupied = set(tuple(segment) for segment in snake_body)
    free_cells = [
        (col * SNAKE_SIZE, row * SNAKE_SIZE)
        for row in range(GRID_ROWS)
        for col in range(GRID_COLS)
        if (col * SNAKE_SIZE, row * SNAKE_SIZE) not in occupied
    ]
    if not free_cells:
        return None
    return random.choice(free_cells)

def reset_game():
    global head_x, head_y, x_change, y_change, snake_body, snake_length
    global food_x, food_y, game_over, direction, next_direction, you_win
    head_x = 300
    head_y = 300
    x_change = 0
    y_change = 0
    direction = "STOP"
    next_direction = "STOP"
    snake_body = [[head_x, head_y]]
    snake_length = 1
    food_x, food_y = spawn_food(snake_body)
    game_over = False
    you_win = False

reset_game()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_SPACE:
                reset_game()
            elif not game_over:
                if (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != "DOWN":
                    next_direction = "UP"
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != "UP":
                    next_direction = "DOWN"
                elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != "RIGHT":
                    next_direction = "LEFT"
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != "LEFT":
                    next_direction = "RIGHT"

    if not game_over:
        direction = next_direction
        if direction == "UP":
            x_change = 0
            y_change = -SNAKE_SIZE
        elif direction == "DOWN":
            x_change = 0
            y_change = SNAKE_SIZE
        elif direction == "LEFT":
            x_change = -SNAKE_SIZE
            y_change = 0
        elif direction == "RIGHT":
            x_change = SNAKE_SIZE
            y_change = 0

        head_x += x_change
        head_y += y_change

        if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT:
            game_over = True

        if direction != "STOP":
            snake_head = [head_x, head_y]
            snake_body.append(snake_head)

            if len(snake_body) > snake_length:
                del snake_body[0]

            for segment in snake_body[:-1]:
                if segment == snake_head:
                    game_over = True

        if head_x == food_x and head_y == food_y:
            snake_length += 1
            new_food = spawn_food(snake_body)
            if new_food is None:
                # Snake fills the entire board - the player has won
                game_over = True
                you_win = True
            else:
                food_x, food_y = new_food

    # --- DRAWING ---
    draw_checkerboard()
    draw_apple(food_x, food_y)
    draw_snake(snake_body, direction)

    score_text = font.render(f"🍎 Score: {snake_length - 1}", True, WHITE)
    screen.blit(score_text, [15, 15])

    if game_over:
        title = "YOU WIN!" if you_win else "GAME OVER"
        color = (30, 160, 30) if you_win else (200, 30, 30)
        msg1 = game_over_font.render(title, True, color)
        msg2 = font.render("Press SPACE to Play Again", True, WHITE)
        screen.blit(msg1, [SCREEN_WIDTH // 2 - msg1.get_width() // 2, SCREEN_HEIGHT // 2 - 40])
        screen.blit(msg2, [SCREEN_WIDTH // 2 - msg2.get_width() // 2, SCREEN_HEIGHT // 2 + 15])

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
