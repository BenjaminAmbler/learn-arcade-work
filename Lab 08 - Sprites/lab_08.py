"""

Welcome to Space Dodge. You are a spaceship pilot flying
through an asteroid belt. You are trying to dodge
the asteroids and collect the extra lives.
These asteroids are actually attracted to your ship
because your ship has a gravity device and
you can't turn it off.


Instructions:

Move with the mouse. Try to avoid the asteroids and collect
the extra lives (the tiny green spaceships)
If you hit 3 asteroids it's game over. If you collect all of the
extra lives you win! But it's still game over.

 """

import random
import arcade
import os

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 1
EXTRA_LIFE_COUNT = 10
ASTEROID_COUNT = 7


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Dodge the Rocks, Collect the Tiny Green Ships"
SPRITE_SPEED = 0.5


class GameOverView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("game_over_screenshot.png")

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        # arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)

class Asteroid(arcade.Sprite):
    """
    This class represents the asteroids on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """
    #
    # def reset_pos(self):
    #
    #     # Reset the asteroids to a random position off of the right side of the screen
    #     self.center_y = random.randrange(SCREEN_HEIGHT)
    #     self.center_x = random.randrange(SCREEN_WIDTH + 20,
    #                                  SCREEN_WIDTH + 100)
    #
    # def update(self):
    #
    #     # Move the asteroids from right to left
    #     self.center_x -= 2
    #
    #     # check if the asteroid has moved off of the screen.
    #     # if so, reset it.
    #     # this might need to be changed to self.right instead
    #     if self.left < 0:
    #         self.reset_pos()

    def follow_sprite(self, player_sprite):
        """
        This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        """

        if self.center_y < player_sprite.center_y:
            self.center_y += min(SPRITE_SPEED, player_sprite.center_y - self.center_y)
        elif self.center_y > player_sprite.center_y:
            self.center_y -= min(SPRITE_SPEED, self.center_y - player_sprite.center_y)

        if self.center_x < player_sprite.center_x:
            self.center_x += min(SPRITE_SPEED, player_sprite.center_x - self.center_x)
        elif self.center_x > player_sprite.center_x:
            self.center_x -= min(SPRITE_SPEED, self.center_x - player_sprite.center_x)


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


class GameView(arcade.View):
    """ Our custom View Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold sprite lists
        self.player_list = None
        self.extra_life_list = None
        self.asteroid_list = None

        # good sound instance variable
        self.good_sound = arcade.load_sound(":resources:sounds/upgrade4.wav")
        self.good_sound_player = None

        # bad sound instance variable
        self.bad_sound = arcade.load_sound(":resources:sounds/explosion2.wav")
        self.bad_sound_player = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.window.set_mouse_visible(False)

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

        for asteroid in self.asteroid_list:
            asteroid.follow_sprite(self.player_sprite)

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        # if len(self.extra_life_list) > 0:
            self.extra_life_list.update()
            self.asteroid_list.update()




        # Generate a list of all sprites that collided with the player.
        extra_life_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.extra_life_list)
        asteroid_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                 self.asteroid_list)

        # Loop through each colliding sprite, remove it, and add to the score
        # and play a sound
        for extra_life in extra_life_hit_list:
            if not self.good_sound_player or not self.good_sound_player.playing:
                self.good_sound_player = arcade.play_sound(self.good_sound)
            extra_life.remove_from_sprite_lists()
            self.score += 1

        for asteroid in asteroid_hit_list:
            if not self.bad_sound_player or not self.bad_sound_player.playing:
                self.bad_sound_player = arcade.play_sound(self.bad_sound)
            asteroid.remove_from_sprite_lists()
            self.score -= 5

        # Check length of extra life and asteroids list. If it is zero or if
        # you hit too many asteroids, display the
        # game over view
        if len(self.extra_life_list) == 0:
            view = GameOverView()
            self.window.show_view(view)
        elif len(self.asteroid_list) == 4:
            view = GameOverView()
            self.window.show_view(view)




def main():
    """ Main function """

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = GameView()
    window.show_view(start_view)
    start_view.setup()
    arcade.run()


if __name__ == "__main__":
    main()