""" This is a test program
to try out using comments
and to try drawing in the
Python programming language with the Arcade library
"""

# Import the "arcade" library

import arcade

arcade.open_window(600, 600, "Ben's Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw a rectangle
# Left of 0, right of 599,
# Top of 300, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)
# Drawing code goes here

# Finish drawing
arcade.finish_render()

# Keep the window open
arcade.run()
