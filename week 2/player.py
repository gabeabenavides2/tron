
class Player:
    def __init__(self, x, y, player_id):
        """
        Initialize the player.
        :param x: Initial x-coordinate
        :param y: Initial y-coordinate
        :param color: Color of the player's trail
        """
        # TODO: Set initial position, color, direction (e.g., [1, 0] for right)
        # Initialize an empty list for the player's
        self.position = [x,y]
        self.player_trail = []
        self.direction = [1, 0]
        self.player_id = player_id

        if player_id == 1:
            self.direction = [1, 0]
        if player_id == 2:
            self.direction = [-1, 0]


    def move(self):
        """
        Move the player based on their current direction.
        """
        # TODO: Update the player's position based on their direction
        # Add the new position to the trail
        self.player_trail.append(self.position[:])
        self.position[0] = self.position[0] + self.direction[0]
        self.position[1] = self.position[1] + self.direction[1]


    def change_direction(self, direction):
        """
        Change the player's direction.
        :param direction: New direction as a list [dx, dy]
        """
        # TODO: Update the player's direction
        # Ensure the new direction is not opposite to the current direction
        test = [0,0]
        test[0] = direction[0] + self.direction[0]
        test[1] = direction[1] + self.direction[1]
        if test != [0,0]:
            self.direction = direction

    #def draw(self, screen):
        """
        Draw the player and their trail on the screen.
        :param screen: Pygame screen object to draw on
        """
        # TODO: Draw the player's current position and their entire trail

