import random
import arcade

SPRITE_SCALING_PLAYER = 1.5
SPRITE_SCALING_COIN = 0.5
SPRITE_SCALING_LASER = 0.8
COIN_COUNT = 10

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites and Bullets Demo")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.bullet_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Set up the player
        self.score = 0

        # Image from kenney.nl

        """
        filename – Filename of an image that represents the sprite.
        scale – Scale the image up or down. Scale of 1.0 is none.
        image_x – X offset to sprite within sprite sheet.
        image_y – Y offset to sprite within sprite sheet.
        image_width – Width of the sprite
        image_height – Height of the sprite
        center_x – Location of the sprite
        center_y – Location of the sprite
        flipped_horizontally – Mirror the sprite image. Flip left/right across vertical axis.
        flipped_vertically – Flip the image up/down across the horizontal axis.
        """

        self.player_sprite = arcade.Sprite(":resources:images/topdown_tanks/tank_blue.png",
                                           SPRITE_SCALING_PLAYER,
                                           # image_x = 0,
                                           # image_y = 0,
                                           # image_width = 0,
                                           # image_height = 0,
                                           # center_x = 0,
                                           # center_y = 0,
                                           # flipped_horizontally = False,
                                           flipped_vertically = True)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_fall.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            # add 150 in the code below to keep the zombies above the player
            coin.center_y = random.randrange(150, SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.coin_list.draw()
        self.player_list.draw()
        self.bullet_list.draw()

        # Render the text
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x
        # Commented out this line to keep the player on the bottom of the screen
        # self.player_sprite.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """
        # create a bullet
        bullet = arcade.Sprite("laserBlue01.png, SPRITE_SCALING_LASER")
        self.bullet_list.append(bullet)


    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.coin_list.update()
        self.bullet_list.update()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()