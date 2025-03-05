import pygame

pygame.init()


class GameBoard:
    def __init__(self, width, height):
        """
        Initialize the game board.
        :param width: Width of the game board in grid cells
        :param height: Height of the game board in grid cells
        """
        # TODO: Initialize a 2D list to represent the game board
        # 0 can represent empty cells, 1 for player trails
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def draw(self, screen):
        """
        Draw the game board on the screen.
        :param screen: Pygame screen object to draw on
        """
        # TODO: Iterate through the 2D list and draw rectangles for each cell
        # Empty cells can be one color, trails another
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        rect_width = screen_width / self.width
        rect_height = screen_height / self.height
        light_blue = (173, 216, 230)
        dark_blue = (0, 0, 139)
        dark_red = (139, 0, 0)
        light_red = (255, 102, 102)
        grey = (64, 64, 64)

        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == 1:
                    color = dark_blue
                elif self.grid[i][j] == 2:
                    color = light_blue
                elif self.grid[i][j] == 3:
                    color = dark_red
                elif self.grid[i][j] == 4:
                    color = light_red
                else:
                    color = grey
                pygame.draw.rect(screen, color, (rect_width * j, rect_height * i, rect_width, rect_height))

    def is_collision(self, x, y):
        """
        Check if the given coordinates collide with the board boundaries or a trail.
        :param x: X-coordinate to check
        :param y: Y-coordinate to check
        :return: True if collision, False otherwise
        """
        # TODO: Check if x and y are within board boundaries
        # Also check if the cell at (x, y) is not empty (i.e., has a trail)
        def is_out_of_bounds(x, y):
            return x < 0 or x >= self.width or y < 0 or y >= self.height

        player_out_of_bounds = is_out_of_bounds(x, y)

        if player_out_of_bounds:
            return True

        player_collision = self.grid[y][x] != 0

        if player_collision:
            return True

        return False




