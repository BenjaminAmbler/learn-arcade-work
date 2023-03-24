""" coins = extra lives. Need to try this again.

Tried replacing:

coin = extra_life

Coin = Extra_Life

COIN = EXTRA_LIFE

but it kept messing up the whole thing.

I'll have to try some more later when I get some more time.

"coins" = good sprites, which are extra lives. These are the tiny little
spaceships.

Bad sprites = asteroids.

 """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.5
# EXTRA_LIVES_COUNT = 50
EXTRA_LIFE_COUNT = 50
ASTEROID_COUNT = 3


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Asteroid(arcade.Sprite):
    """
    This class represents the asteroids on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the asteroids to a random position off of the right side of the screen
        self.center_y = random.randrange(SCREEN_HEIGHT)
        self.center_x = random.randrange(SCREEN_WIDTH + 20,
                                     SCREEN_WIDTH + 100)

    def update(self):

        # Move the asteroids from right to left
        self.center_x -= 1

        # check if the asteroid has moved off of the screen.
        # if so, reset it.
        # this might need to be chaned to self.right instead
        if self.left < 0:
            self.reset_pos()


class Extra_Life(arcade.Sprite):
    """
    This class represents the coins on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the extra lives to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the extra lives from the top to the bottom
        # Make it rain! (extra lives)
        self.center_y -= 1

        # check if the extra life has fallen off the bottom of the screen.
        # if so, reset it.
        if self.top < 0:
            self.reset_pos()





class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Dodge The Rocks, Collect The Extra Lives")

        # Variables that will hold sprite lists
        self.player_list = None
        self.extra_life_list = None
        self.asteroid_list = None

        # sound instance variables
        self.good_sound = arcade.load_sound(":resources:sounds/upgrade5.wav")
        self.good_sound_player = None

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
        self.extra_life_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite(":resources:images/space_shooter/playerShip1_blue.png",
                                           SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the extra lives
        for i in range(EXTRA_LIFE_COUNT):

            # Create the good sprite instance
            # Coin image from kenney.nl
            extra_life = Extra_Life(":resources:images/space_shooter/playerLife1_green.png", SPRITE_SCALING_COIN)

            # Position the coin
            extra_life.center_x = random.randrange(SCREEN_WIDTH)
            extra_life.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.extra_life_list.append(extra_life)


        # Create the asteroids


        for i in range(ASTEROID_COUNT):

            # Create the good sprite instance
            # Coin image from kenney.nl
            asteroid = Asteroid(":resources:images/space_shooter/meteorGrey_big3.png", SPRITE_SCALING_COIN)

            # Position the asteroid
            asteroid.center_x = random.randrange(SCREEN_WIDTH)
            asteroid.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the asteroid to the lists
            self.asteroid_list.append(asteroid)


    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.extra_life_list.draw()
        self.asteroid_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.extra_life_list.update()
        self.asteroid_list.update()

        # Generate a list of all sprites that collided with the player.
        extra_life_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.extra_life_list)
        asteroid_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                 self.asteroid_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for extra_life in extra_life_hit_list:
            if not self.good_sound_player or not self.good_sound_player.playing:
                self.good_sound_player = arcade.play_sound(self.good_sound)
            extra_life.remove_from_sprite_lists()
            self.score += 1

        for asteroid in asteroid_hit_list:
            # if not self.bad_sound_player or not self.bad_sound_player.playing:
            #     self.bad_sound_player = arcade.play_sound(self.bad_sound)
            asteroid.remove_from_sprite_lists()
            self.score -= 5


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()