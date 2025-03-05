import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Game constants
GRID_SIZE = 20
WIDTH, HEIGHT = 600, 600
FPS = 15

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PLAYER_COLOR = (0, 255, 255)
AI_COLOR = (255, 0, 0)

# Initialize the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tron Game with AI")
clock = pygame.time.Clock()

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


# Player class
class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.direction = RIGHT
        self.trail = [(x, y)]

    def move(self):
        self.x += self.direction[0] * GRID_SIZE
        self.y += self.direction[1] * GRID_SIZE

        # Check for wall collision
        if self.x < 0 or self.x >= WIDTH or self.y < 0 or self.y >= HEIGHT:
            return False  # Player runs into the wall

        self.trail.append((self.x, self.y))
        return True

    def get_head(self):
        return (self.x, self.y)

    def draw(self):
        for segment in self.trail:
            pygame.draw.rect(screen, self.color, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))


# AI class with smarter behavior
class AI(Player):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def choose_direction(self, grid, player_pos):
        directions = [UP, DOWN, LEFT, RIGHT]
        random.shuffle(directions)

        # Filter out invalid moves (like going off the grid)
        valid_directions = []
        for direction in directions:
            new_x = self.x + direction[0] * GRID_SIZE
            new_y = self.y + direction[1] * GRID_SIZE
            if (new_x, new_y) not in self.trail and 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT:
                valid_directions.append(direction)

        # Avoid moving into the player's trail unless there's no other choice
        safe_directions = []
        for direction in valid_directions:
            new_x = self.x + direction[0] * GRID_SIZE
            new_y = self.y + direction[1] * GRID_SIZE
            if (new_x, new_y) not in player.trail:  # Ensure the AI doesn't run into the player's trail
                safe_directions.append(direction)

        # If there are safe directions available, choose one
        if safe_directions:
            best_direction = None
            best_distance = float('inf')

            # Prioritize getting closer to the player
            for direction in safe_directions:
                new_x = self.x + direction[0] * GRID_SIZE
                new_y = self.y + direction[1] * GRID_SIZE
                distance_to_player = abs(new_x - player_pos[0]) + abs(new_y - player_pos[1])  # Manhattan distance

                if distance_to_player < best_distance:
                    best_distance = distance_to_player
                    best_direction = direction
            return best_direction

        # If there are no safe directions, the AI will be forced to run into the player's trail or a dead end
        return valid_directions[0]  # Default to any direction if no valid ones are found


# Initialize players
player = Player(WIDTH // 4, HEIGHT // 2, PLAYER_COLOR)
ai = AI(3 * WIDTH // 4, HEIGHT // 2, AI_COLOR)

# Main game loop
while True:
    screen.fill(BLACK)

    # Check for events (quitting the game)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement (WASD or Arrow keys)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.direction = LEFT
    elif keys[pygame.K_RIGHT]:
        player.direction = RIGHT
    elif keys[pygame.K_UP]:
        player.direction = UP
    elif keys[pygame.K_DOWN]:
        player.direction = DOWN

    # AI movement with smarter decision-making
    ai.direction = ai.choose_direction(ai.trail, player.get_head())

    # Move both players and check if they hit the wall
    if not player.move():
        print("Game Over! AI Wins!")
        pygame.quit()
        sys.exit()

    if not ai.move():
        print("Game Over! Player Wins!")
        pygame.quit()
        sys.exit()

    # Draw both players
    player.draw()
    ai.draw()

    # Collision detection (game over condition)
    if player.get_head() in player.trail[:-1] or player.get_head() in ai.trail:
        print("Game Over! AI Wins!")
        pygame.quit()
        sys.exit()
    if ai.get_head() in ai.trail[:-1] or ai.get_head() in player.trail:
        print("Game Over! Player Wins!")
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(FPS)
