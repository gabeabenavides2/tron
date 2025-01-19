import pygame
from game_board import GameBoard
from player import Player

pygame.init()


def initialize_game():
    """
    Initialize Pygame and create the game window.
    :return: Pygame screen object
    """
    # TODO: Initialize Pygame
    # Create and return a Pygame screen object
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    return screen


def handle_events(player1, player2):
    """
    Handle Pygame events, including player input.
    :param player: Player object to update based on input
    :return: False if the game should quit, True otherwise
    """
    # TODO: Loop through Pygame events
    # Handle QUIT event
    # Handle KEYDOWN events to change player direction
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1.change_direction([0, -1])
            elif event.key == pygame.K_DOWN:
                player1.change_direction([0, 1])
            elif event.key == pygame.K_RIGHT:
                player1.change_direction([1, 0])
            elif event.key == pygame.K_LEFT:
                player1.change_direction([-1, 0])
            elif event.key == pygame.K_w:
                player2.change_direction([0, -1])
            elif event.key == pygame.K_s:
                player2.change_direction([0, 1])
            elif event.key == pygame.K_d:
                player2.change_direction([1, 0])
            elif event.key == pygame.K_a:
                player2.change_direction([-1, 0])
        if event.type == pygame.QUIT:
            return False
    return True


def update_game_state(player1, player2, game_board):
    """
    Update the game state, including player movement and collision detection.
    :param player: Player object to update
    :param game_board: GameBoard object to check collisions against
    :return: False if the game is over (collision), True otherwise
    """
    # TODO: Move the player
    # Check for collisions with game_board
    # Update game_board with new player position
    once = True

    player1.move()
    player2.move()
    collision_detector = False
    who_collided = 0
    collision_detector, who_collided = game_board.is_collision(player1.position[0], player1.position[1], player2.position[0], player2.position[1])
    if collision_detector:
        return False, who_collided
    for pos in player1.player_trail:
        game_board.board[pos[1]][pos[0]] = 2
    for pos in player2.player_trail:
        game_board.board[pos[1]][pos[0]] = 4
    game_board.board[player1.position[1]][player1.position[0]] = 1
    game_board.board[player2.position[1]][player2.position[0]] = 3
    return True, who_collided


def draw_game(screen, game_board):
    """
    Draw the current game state.
    :param screen: Pygame screen object to draw on
    :param game_board: GameBoard object to draw
    :param player: Player object to draw
    """
    # TODO: Clear the screen
    # Draw the game board
    # Draw the player
    # Update the display
    background_color = (0, 0, 0)
    screen.fill(background_color)
    game_board.draw(screen)
    pygame.display.flip()


def winner_screen(screen, winner, player_1_score, player_2_score):
    running = True
    font = pygame.font.Font(None, 74)

    # Determine the winner message and color
    if winner == 1:
        message = 'Player 1 Wins!'
        color = (0, 0, 139)
    elif winner == 2:
        message = 'Player 2 Wins!'
        color = (139, 0, 0)
    else:
        message = "It's a Draw!"
        color = (255, 255, 0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()
                elif event.key == pygame.K_SPACE:
                    running = False

        screen.fill((0, 0, 0))  # Fill the screen with black

        # Display winner message
        text = font.render(message, True, color)
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(text, text_rect)

        # Display instruction to quit or continue
        instruction = "Press Enter to Continue or Q to Quit"
        instruction_text = pygame.font.Font(None, 50).render(instruction, True, (255, 255, 255))
        instruction_rect = instruction_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 100))
        screen.blit(instruction_text, instruction_rect)

        # Display scoreboard
        score_text = f"Player 1: {player_1_score}     Player 2: {player_2_score}"
        score_display = pygame.font.Font(None, 50).render(score_text, True, (255, 255, 255))
        score_rect = score_display.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 200))
        screen.blit(score_display, score_rect)

        pygame.display.flip()
        pygame.time.delay(100)


def main():
    """
    Main game loop.
    """
    # TODO: Initialize the game
    # Create game objects (game_board, player)
    # Run the game loop:
    #   - Handle events
    #   - Update game state
    #   - Draw game
    #   - Control game speed

    player1_score = 0
    player2_score = 0
    playing = True

    while playing:
        screen_width = 800
        screen_height = 600
        screen = pygame.display.set_mode((screen_width, screen_height))
        grid_height = 30
        grid_width = 40
        dark_blue = (0, 0, 139)
        dark_red = (139, 0, 0)
        grey = (64, 64, 64)
        board = GameBoard(grid_width, grid_height)
        player_2 = Player((grid_width // 3) * 2, grid_height // 2, 2)
        player_1 = Player(grid_width // 3, grid_height // 2, 1)




        running = True

        while running:

            running = handle_events(player_2, player_1)
            game_state, who_collided = update_game_state(player_1, player_2, board)
            if not game_state:
                running = False
                if who_collided == 1:
                    player2_score += 1
                    winner_screen(screen, 2, player1_score, player2_score)
                elif who_collided == 2:
                    player1_score += 1
                    winner_screen(screen, 1, player1_score, player2_score)
                elif who_collided == 3:
                    winner_screen(screen, 0, player1_score, player2_score)

            draw_game(screen, board)

            pygame.time.delay(60)

    pygame.quit()


if __name__ == "__main__":
    main()


