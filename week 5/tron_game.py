import pygame
from game_board import GameBoard
from player import Player
from mock_ai import MockAI

def initialize_game():
    """
    Initialize Pygame and create the game window.
    :return: Pygame screen object
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Tron Game")
    return screen

def handle_events() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def update_game_state(player1: Player, player2: Player, game_board: GameBoard) -> int:
    # Store the next positions
    next_x1, next_y1 = player1.x + player1.direction[0], player1.y + player1.direction[1]
    next_x2, next_y2 = player2.x + player2.direction[0], player2.y + player2.direction[1]
    
    # Check for collisions at the next positions
    collision1 = game_board.is_collision(next_x1, next_y1)
    collision2 = game_board.is_collision(next_x2, next_y2)
    
    # Check for head-on collision
    head_on_collision = (next_x1, next_y1) == (next_x2, next_y2)
    
    if head_on_collision:
        return 3  # It's a draw
    elif collision1 and collision2:
        return 3  # It's a draw
    elif collision1:
        return 2  # Player 2 wins (Player 1 loses)
    elif collision2:
        return 1  # Player 1 wins (Player 2 loses)
    
    # If no collisions, update the positions
    player1.move()
    player2.move()
    
    # Update the game board
    game_board.grid[player1.y][player1.x] = player1.player_id
    game_board.grid[player2.y][player2.x] = player2.player_id
    
    return 0

def draw_game(screen: pygame.Surface, game_board: GameBoard, player1: Player, player2: Player):
    """
    Draw the current game state.
    :param screen: Pygame screen object to draw on
    :param game_board: GameBoard object to draw
    :param player1: Player object for player 1
    :param player2: Player object for player 2
    """
    screen.fill((0, 0, 0))
    game_board.draw(screen)
    player1.draw(screen)
    player2.draw(screen)
    pygame.display.flip()

def main():
    """
    Main game loop.
    """
    screen = initialize_game()
    game_board = GameBoard(40, 30)
    ai1 = MockAI()
    ai2 = MockAI()
    player1 = Player(10, 15, (255, 0, 0), 1, ai1)
    player2 = Player(30, 15, (0, 0, 255), 2, ai2)
    clock = pygame.time.Clock()

    running = True
    while running:
        running = handle_events()
        if running:
            result = update_game_state(player1, player2, game_board)
            if result != 0:
                running = False
                if result == 1:
                    print("Player 1 wins!")
                elif result == 2:
                    print("Player 2 wins!")
                else:
                    print("It's a draw!")
        draw_game(screen, game_board, player1, player2)
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()