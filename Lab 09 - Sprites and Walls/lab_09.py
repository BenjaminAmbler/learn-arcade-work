"""
Lab 9

Move with the arrow keys.

This uses a scrolling screen

"""

import random
import arcade
from pyglet.math import Vec2
import os

SPRITE_SCALING = 0.5
SPRITE_SCALING_COIN = 0.5
COIN_COUNT = 30

DEFAULT_SCREEN_WIDTH = 1500
DEFAULT_SCREEN_HEIGHT = 700
SCREEN_TITLE = "Use To Move Around. Get All Of The Keys"


# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 520

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Load the sound when the application starts
        self.explosion_sound = arcade.load_sound(":resources:music/1918.mp3")
        self.explosion_sound_player = None
        if not self.explosion_sound_player or not self.explosion_sound_player.playing:
            self.explosion_sound_player = arcade.play_sound(self.explosion_sound)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # good sound instance variable
        self.good_sound = arcade.load_sound(":resources:sounds/coin5.wav")
        self.good_sound_player = None

        # Sprite lists
        self.all_sprites_list = None
        self.coin_list = None

        # Set up the player
        # self.player_list = None
        self.player_sprite = None
        self.wall_list = None
        self.physics_engine = None
        self.score = 0

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False


        # Create the cameras. One for the GUI, one for the sprites.

        # We scroll the 'sprite world' but not the GUI.

        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)


    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           scale=0.5)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_list.append(self.player_sprite)

        # # Create the coins
        # for i in range(COIN_COUNT):
        #     # Create the coin instance
        #     # Coin image from kenney.nl
        #     coin = arcade.Sprite(":resources:images/items/keyBlue.png", SPRITE_SCALING_COIN)
        #
        #     # Position the coin
        #     coin.center_x = random.randrange(DEFAULT_SCREEN_WIDTH)
        #     coin.center_y = random.randrange(DEFAULT_SCREEN_HEIGHT)
        #
        #     # Add the coin to the lists
        #     self.coin_list.append(coin)


        # set up outside vertical walls
        for x in range(0, 1280, 1279):
            for y in range(0, 1280, 64):
                    wall = arcade.Sprite(":resources:images/tiles/stone.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        # set up horizontal outside walls
        for y in range(0, 1280, 1279):
            for x in range(0, 1344, 64):
                    wall = arcade.Sprite(":resources:images/tiles/stone.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        # set up first bottom horizontal snow wall
        for y in range(454, 455):
            for x in range(64, 400, 64):
                    wall = arcade.Sprite(":resources:images/tiles/snowHalf.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        # snow wall first layer right side
            for y in range(454, 455):
                for x in range(564, 1200, 64):
                    wall = arcade.Sprite(":resources:images/tiles/snowHalf.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        # snow wall layer 1 left side
        for y in range(354, 355):
            for x in range(64, 400, 64):
                    wall = arcade.Sprite(":resources:images/tiles/snowHalf.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        # snow wall layer 1 right side
        for y in range(354, 355):
            for x in range(564, 980, 64):
                    wall = arcade.Sprite(":resources:images/tiles/snowHalf.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        # snow wall layer 2 left side
        for y in range(654, 655):
            for x in range(64, 100, 64):
                    wall = arcade.Sprite(":resources:images/tiles/snowHalf.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        # snow wall layer 2 more left side
        for y in range(654, 655):
            for x in range(264, 700, 64):
                    wall = arcade.Sprite(":resources:images/tiles/snowHalf.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        # snow wall layer 2 more left side
        for y in range(654, 655):
            for x in range(864, 980, 64):
                    wall = arcade.Sprite(":resources:images/tiles/snowHalf.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)


        # # place a few keys to collect with a list
        # coordinate_list = [64, 500], [500, 600], [200, 700], [1000, 800]
        #
        # # Loop through coordinates
        # for coordinate in coordinate_list:
        #     wall = arcade.Sprite(":resources:images/items/keyBlue.png", SPRITE_SCALING)
        #     wall.center_x = coordinate[0]
        #     wall.center_y = coordinate[1]
        #     self.wall_list.append(wall)

            # -- Randomly place coins where there are no walls
            # Create the coins
            for i in range(COIN_COUNT):

                # Create the coin instance
                # Coin image from kenney.nl
                coin = arcade.Sprite(":resources:images/items/keyBlue.png", SPRITE_SCALING_COIN)

                # --- IMPORTANT PART ---

                # Boolean variable if we successfully placed the coin
                coin_placed_successfully = False

                # Keep trying until success
                while not coin_placed_successfully:
                    # Position the coin
                    coin.center_x = random.randrange(0, 1200)
                    coin.center_y = random.randrange(0, 1200)

                    # See if the coin is hitting a wall
                    wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                    # See if the coin is hitting another coin
                    coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                    if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                        # It is!
                        coin_placed_successfully = True

                # Add the coin to the lists
                self.coin_list.append(coin)

                # --- END OF IMPORTANT PART ---

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        self.clear()


        # Select the camera we'll use to draw all our sprites

        self.camera_sprites.use()


        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()

        # Put the score on the screen.
        # output = f"Score: {self.score}"
        # arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        # Select the (unscrolled) camera for our GUI

        self.camera_gui.use()


        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLUE, 14)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            if not self.good_sound_player or not self.good_sound_player.playing:
                self.good_sound_player = arcade.play_sound(self.good_sound)
            coin.remove_from_sprite_lists()
            self.score += 1

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()


        # Scroll the screen to the player

        self.scroll_to_player()



    def scroll_to_player(self):

        """

        Scroll the window to the player.



        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.

        Anything between 0 and 1 will have the camera move to the location with a smoother

        pan.

        """



        position = Vec2(self.player_sprite.center_x - self.width / 2,

                        self.player_sprite.center_y - self.height / 2)

        self.camera_sprites.move_to(position, CAMERA_SPEED)



    def on_resize(self, width, height):

        """

        Resize window

        Handle the user grabbing the edge and resizing the window.

        """

        self.camera_sprites.resize(int(width), int(height))

        self.camera_gui.resize(int(width), int(height))



def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()