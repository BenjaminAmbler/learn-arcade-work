
""" Lab 7 - User Control """

# Instructions:
# Move the tree with the arrow keys
# Move the snowball with the mouse.
# Makes a sound when you hit the edge of the screen
# Makes a sound when you press the left mouse button


import arcade
# laser_sound = arcade.load_sound("laser.wav")

""" --- constants --- """
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 7


# Create two functions that will draw the background. One
# will draw the mountain, one will draw the ground.
# Could probably combine this into one function later.
def draw_mountain(x, y):
    # Draw a mountain range in the background using a polygon with a list of points
    arcade.draw_polygon_filled(((0 + x, 0 + y), # bottom left point
                                (300 + x, 450 + y), # peak
                                (600 + x, 0 + y), # bottom right point
                                ),
                                arcade.color.DARK_VIOLET)

def draw_ground():
    # Draw the ground
    # Left point at 0, right point at SCREEN_WIDTH,
    # 1/10th the height of the screen
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 10, 0, arcade.csscolor.GREEN)

class Ball:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)

class Tree:
    def __init__(self, center_x, center_y, change_x, change_y, width, height, color):
        """ Constructor """
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        # sound instance variables
        self.laser_sound = arcade.load_sound("laser.wav")
        self.laser_sound_player = None

        # movement variables
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.color = color



    def draw(self):
    #     """ Draw the tree with the instance variables we have. """
    #     arcade.draw_rectangle_filled(self.center_x,
    #                               self.center_y,
    #                               self.width,
    #                               self.height,
    #                               self.
    #                               color)


        # # tiny far away tree with three triangles
        # arcade.draw_rectangle_filled(220 + self.center_x, 335 + self.center_y, 3, 30, self.color)
        # arcade.draw_triangle_filled(215 + self.center_x, 345 + self.center_y, 220 + self.center_x, 350 + self.center_y, 225 + self.center_x, 345 + self.center_y, arcade.color.DARK_GREEN)
        # arcade.draw_triangle_filled(210 + self.center_x, 340 + self.center_y, 220 + self.center_x, 345 + self.center_y, 230 + self.center_x, 340 + self.center_y, arcade.color.DARK_GREEN)
        # arcade.draw_triangle_filled(205 + self.center_x, 335 + self.center_y, 220 + self.center_x, 340 + self.center_y, 235 + self.center_x, 335 + self.center_y, arcade.color.DARK_GREEN)

    # tiny far away tree with a trunk and three triangles
        arcade.draw_rectangle_filled(0 + self.center_x, 0 + self.center_y, 5, 30, self.color)
        arcade.draw_triangle_filled(-5 + self.center_x, 25 + self.center_y,
                                    0 + self.center_x, 40 + self.center_y,
                                    5 + self.center_x, 25 + self.center_y,
                                    arcade.color.DARK_GREEN)
        arcade.draw_triangle_filled(-10 + self.center_x, 15 + self.center_y,
                                    0 + self.center_x, 30 + self.center_y,
                                    10 + self.center_x, 15 + self.center_y,
                                    arcade.color.DARK_GREEN)
        arcade.draw_triangle_filled(-15 + self.center_x, 10 + self.center_y,
                                    0 + self.center_x, 20 + self.center_y,
                                    15 + self.center_x, 10 + self.center_y,
                                    arcade.color.DARK_GREEN)

    def update(self):
        # Move the tree
        self.center_y += self.change_y
        self.center_x += self.change_x

        # See if the tree hit the edge of the screen. If so, change direction
        if self.center_x < self.width:
            self.center_x = self.width
            # This code makes the sound play on repeat 60 times a second
            # when you hit the edge of the screen. Sounds weird.
            # arcade.play_sound(laser_sound)

            # This code fixes it:
            if not self.laser_sound_player or not self.laser_sound_player.playing:
                self.laser_sound_player = arcade.play_sound(self.laser_sound)


        if self.center_x > SCREEN_WIDTH - self.width:
            self.center_x = SCREEN_WIDTH - self.width

            if not self.laser_sound_player or not self.laser_sound_player.playing:
                self.laser_sound_player = arcade.play_sound(self.laser_sound)

        if self.center_y < self.height:
            self.center_y = self.height

            if not self.laser_sound_player or not self.laser_sound_player.playing:
                self.laser_sound_player = arcade.play_sound(self.laser_sound)

        if self.center_y > SCREEN_HEIGHT - self.height:
            self.center_y = SCREEN_HEIGHT - self.height

            if not self.laser_sound_player or not self.laser_sound_player.playing:
                self.laser_sound_player = arcade.play_sound(self.laser_sound)


class MyGame(arcade.Window):
    """ Our custom window class """
    # self.laser_sound = arcade.load_sound("laser.wav")
    # self.laser_sound_player = None

    def __init__(self, width, height, title):
        """ Initializer """
        self.laser_sound = arcade.load_sound("laser.wav")
        self.laser_sound_player = None
        # Call the parent class's init function
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 User Control")

        # Mouse pointer visible over window or not...
        # Can change this with True or False
        self.set_mouse_visible(False)

        # Draw background here
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Create our tree
        self.tree = Tree(50, 50, 0, 0, 15, 50, arcade.color.DARK_BROWN)

        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.WHITE)
    def on_draw(self):
        """ called whenever we need to draw the window """
        arcade.start_render()
        self.tree.draw()
        self.ball.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.ball.position_x = x
        self.ball.position_y = y

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        # Get ready to draw stuff
        arcade.start_render()

        # Draw the mountains
        draw_mountain(0, 50)
        draw_mountain(50, 55)
        draw_mountain(100, 100)
        draw_mountain(150, 55)
        draw_mountain(200, 50)
        draw_mountain(250, 60)
        draw_mountain(300, 55)

        draw_ground()

        self.tree.draw()
        self.ball.draw()


    def update(self, delta_time):
        self.tree.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.tree.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.tree.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.tree.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.tree.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.tree.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.tree.change_y = 0

    # add a sound for when the left mouse button gets pressed
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if not self.laser_sound_player or not self.laser_sound_player.playing:
            self.laser_sound_player = arcade.play_sound(self.laser_sound)

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 User Control")
    arcade.run()


main()