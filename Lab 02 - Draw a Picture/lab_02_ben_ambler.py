# --------------------------------------------------------------------
# Trying to make a picture with a mountain in the background
# and a little house and some "happy little trees"
# as Bob Ross would say
# --------------------------------------------------------------------

# import the Arcade library
import arcade

# open a window
# arcade.open_window(1000, 600, "Ben's Mountain Cabin")

# Do the math to figure out our screen dimensions
arcade.open_window(1000, 600, "Ben's Mountain Cabin")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw a mountain range in the background using a polygon with a list of points
arcade.draw_polygon_filled(((0, 0), # bottom left point
                            (125, 350), # shoulder
                            (250, 550), # peak
                            (350, 415), # valley
                            (450, 550), # peak
                            (510, 450), # valley
                            (600, 550), # peak
                            (700, 400), # valley
                            (800, 550), # peak
                            (900, 400), # shoulder
                            (1000, 0), # bottom right point
                            ),
                           arcade.color.DARK_VIOLET)

# Draw a rectangle
# Left point at 0, right point at 1000,
# Top of 40, bottom of 0
# this is for the grass on the bottom of the picture
arcade.draw_lrtb_rectangle_filled(0, 1000, 40, 0, arcade.csscolor.GREEN)

# first tree
# Tree trunk
# Center of 75, 70
# Width of 20
# Height of 60
arcade.draw_rectangle_filled(75, 70, 20, 60, arcade.color.DARK_BROWN)
arcade.draw_circle_filled(75, 90, 30, arcade.color.DARK_GREEN)

# Draw an ellipse with a rectangle with a center of (300, 300)
# Width of 350
# Height of 200
#arcade.draw_rectangle_outline(300, 300, 350, 200, arcade.csscolor.BLACK, 3)
#arcade.draw_ellipse_outline(300, 300, 350, 200, arcade.csscolor.RED, 3)

# Another tree, with a trunk and ellipse for its top
arcade.draw_rectangle_filled(200, 70, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 90, 70, 60, arcade.csscolor.DARK_GREEN)

# Another tree, with a trunk and arc for its top
# Arc centered at (300, 340) with a with of 60 and a height of 100.
# The starting angle is 0, and ending angle is 180.
arcade.draw_rectangle_filled(300, 70, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 90, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

# Another tree, with its trunk and for its top, a triangle this time.
# Triangle is made of these three points:
# (400, 400), (370, 320), and (430, 320)
arcade.draw_rectangle_filled(400, 120, 20, 60, arcade.color.DARK_BROWN)
arcade.draw_triangle_filled(370, 150, 400, 200, 430, 150, arcade.color.DARK_GREEN )

# tiny far away tree with three triangles
arcade.draw_rectangle_filled(820, 435, 3, 30, arcade.color.DARK_BROWN)
arcade.draw_triangle_filled(815, 445, 820, 450, 825, 445, arcade.color.DARK_GREEN )
arcade.draw_triangle_filled(810, 440, 820, 445, 830, 440, arcade.color.DARK_GREEN )
arcade.draw_triangle_filled(805, 435, 820, 440, 835, 435, arcade.color.DARK_GREEN )

# tiny far away tree with three triangles
arcade.draw_rectangle_filled(220, 335, 3, 30, arcade.color.DARK_BROWN)
arcade.draw_triangle_filled(215, 345, 220, 350, 225, 345, arcade.color.DARK_GREEN )
arcade.draw_triangle_filled(210, 340, 220, 345, 230, 340, arcade.color.DARK_GREEN )
arcade.draw_triangle_filled(205, 335, 220, 340, 235, 335, arcade.color.DARK_GREEN )

# Draw a tree using a polygon with a list of points
arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 400),
                            (480, 360),
                            (470, 320),
                            (530, 320),
                            (520, 360),
                            ),
                           arcade.csscolor.DARK_GREEN)

# Draw a tree using a polygon with a list of points
arcade.draw_rectangle_filled(600, 320, 20, 60, arcade.color.DARK_BROWN)
arcade.draw_polygon_filled(((600, 400),
                            (580, 360),
                            (570, 320),
                            (630, 320),
                            (620, 360),
                            ),
                           arcade.csscolor.DARK_GREEN)

# draw a cabin
# draw the main cabin wall center of 850, 70 width of 150 height of 60
arcade.draw_rectangle_filled(850, 70, 150, 60, arcade.color.DARK_BROWN)
# draw the door
arcade.draw_rectangle_filled(815, 60, 30, 40, arcade.color.BLACK)
# draw the window
arcade.draw_rectangle_filled(890, 80, 20, 20, arcade.color.BLACK)
arcade.draw_triangle_filled(750, 100, 850, 130, 950, 100, arcade.color.WHITE)
# horizontal lines for the logs
# (start x, start y, end x, end y)
arcade.draw_line(775, 90, 925, 90, arcade.color.BLACK, 1)
arcade.draw_line(775, 80, 925, 80, arcade.color.BLACK, 1)
arcade.draw_line(775, 70, 925, 70, arcade.color.BLACK, 1)
arcade.draw_line(775, 60, 925, 60, arcade.color.BLACK, 1)
arcade.draw_line(775, 50, 925, 50, arcade.color.BLACK, 1)

# Draw a sun (x, y, diameter)
arcade.draw_circle_filled(70, 525, 40, arcade.color.YELLOW)

# Rays to the left, right, up, and down
# (start x, start y, end x, end y)
# horizontal ray
arcade.draw_line(5, 525, 135, 525, arcade.color.YELLOW, 3)

# (start x, start y, end x, end y)
# vertical ray
arcade.draw_line(70, 450, 70, 595, arcade.color.YELLOW, 3)

# (start x, start y, end x, end y)
# Diagonal ray going from bottom left, to top right
arcade.draw_line(25, 465, 120, 575, arcade.color.YELLOW, 3)

# (start x, start y, end x, end y)
# Diagonal ray going from top left to bottom right
arcade.draw_line(25, 575, 120, 470, arcade.color.YELLOW, 3)


# Draw text at (10, 10, with a font size of 10 pts.
arcade.draw_text("'And over here, maybe... maybe there's a happy little tree -Bob Ross'",
                 550, 15,
                 arcade.color.BLUE, 10)


# draw a rolling hill
#arcade.draw_arc_outline(center_x=600,
#                        center_y=340,
#                        width=1200,
#                        color=arcade.csscolor.GREEN,
#                        start_angle=0,
#                        end_angle=180,
#                        border_width=30,
#                        tilt_angle=0)

# Finish drawing
arcade.finish_render()

# Keep the window open
arcade.run()