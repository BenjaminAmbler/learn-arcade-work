# --------------------------------------------------------------------
# Trying to make a picture with a mountain in the background
# and a little house and some "happy little trees"
# as Bob Ross would say
# --------------------------------------------------------------------

# import the Arcade library
import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


def fat_tree(x, y):
    # Draw a fat tree using a polygon with a list of points
    arcade.draw_rectangle_filled(500 + x, 320 + y, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_polygon_filled(((500 + x, 400 + y),
                                (480 + x, 360 + y),
                                (470 + x, 320 + y),
                                (530 + x, 320 + y),
                                (520 + x, 360 + y),
                                ),
                               arcade.csscolor.DARK_GREEN)
def comfy_little_cabin(x, y):
    # draw a cabin
    # draw the main cabin wall center of 850, 70 width of 150 height of 60
    arcade.draw_rectangle_filled(850 + x, 70 + y, 150, 60, arcade.color.DARK_BROWN)
    # draw the door
    arcade.draw_rectangle_filled(815 + x, 60 + y, 30, 40, arcade.color.BLACK)
    # draw the window
    arcade.draw_rectangle_filled(890 + x, 80 + y, 20, 20, arcade.color.BLACK)
    arcade.draw_triangle_filled(750 + x, 100 + y, 850 + x, 130 + y, 950 + x, 100 + y, arcade.color.WHITE)
    # horizontal lines for the logs
    # (start x, start y, end x, end y)
    arcade.draw_line(775 + x, 90 + y, 925 + x, 90 + y, arcade.color.BLACK, 1)
    arcade.draw_line(775 + x, 80 + y, 925 + x, 80 + y, arcade.color.BLACK, 1)
    arcade.draw_line(775 + x, 70 + y, 925 + x, 70 + y, arcade.color.BLACK, 1)
    arcade.draw_line(775 + x, 60 + y, 925 + x, 60 + y, arcade.color.BLACK, 1)
    arcade.draw_line(775 + x, 50 + y, 925 + x, 50 + y, arcade.color.BLACK, 1)
def happy_little_tree(x, y):
    # tiny far away tree with three triangles
    arcade.draw_rectangle_filled(220 + x, 335 + y, 3, 30, arcade.color.DARK_BROWN)
    arcade.draw_triangle_filled(215 + x, 345 + y, 220 + x, 350 + y, 225 + x, 345 + y, arcade.color.DARK_GREEN )
    arcade.draw_triangle_filled(210 + x, 340 + y, 220 + x, 345 + y, 230 + x, 340 + y, arcade.color.DARK_GREEN )
    arcade.draw_triangle_filled(205 + x, 335 + y, 220 + x, 340 + y, 235 + x, 335 + y, arcade.color.DARK_GREEN )

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


def main():
    # open a window
    # arcade.open_window(SCREEN_WIDTH, SCREEN HEIGHT, "Ben's Mountain Cabin")

    # Do the math to figure out our screen dimensions
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Ben's Mountain Cabin")

    # Set the background color
    arcade.set_background_color(arcade.csscolor.SKY_BLUE)

    # Get ready to draw
    arcade.start_render()

    # make a mountain range out of functions
    # start calling dem draw_mountain functions
    draw_mountain(0, 50)
    draw_mountain(50, 55)
    draw_mountain(100, 100)
    draw_mountain(150, 55)
    draw_mountain(200, 50)
    draw_mountain(250, 60)
    draw_mountain(300, 55)


    # Draw a mountain range in the background using a polygon with a list of points
    #arcade.draw_polygon_filled(((0, 0), # bottom left point
    #                            (125, 350), # shoulder
    #                            (250, 550), # peak
    #                            (350, 415), # valley
    #                            (450, 550), # peak
    #                            (510, 450), # valley
    #                            (600, 550), # peak
    #                            (700, 400), # valley
    #                            (800, 550), # peak
    #                            (900, 400), # shoulder
    #                            (1000, 0), # bottom right point
    #                            ),
    #                           arcade.color.DARK_VIOLET)

    # Call the function to draw the ground
    draw_ground()

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
    arcade.draw_rectangle_filled(400, 70, 20, 60, arcade.color.DARK_BROWN)
    arcade.draw_triangle_filled(370, 100, 400, 150, 430, 100, arcade.color.DARK_GREEN )


    # call the function to draw a small forest of tiny happy little trees far away in the mountains
    happy_little_tree(50, 30)
    happy_little_tree(75, 50)
    happy_little_tree(85, -60)
    happy_little_tree(95, 70)
    happy_little_tree(105, 30)
    happy_little_tree(115, 50)
    happy_little_tree(125, -60)
    happy_little_tree(135, 30)
    happy_little_tree(145, 80)
    happy_little_tree(155, -90)
    happy_little_tree(165, 30)
    happy_little_tree(175, 70)
    happy_little_tree(185, 60)
    happy_little_tree(195, 30)
    happy_little_tree(205, -40)
    happy_little_tree(215, 30)
    happy_little_tree(225, 40)
    happy_little_tree(235, 30)
    happy_little_tree(245, 60)
    happy_little_tree(255, -70)
    happy_little_tree(265, 30)
    happy_little_tree(275, 90)
    happy_little_tree(285, 60)
    happy_little_tree(295, 100)
    happy_little_tree(305, -50)
    happy_little_tree(320, 30)
    happy_little_tree(330, 50)
    happy_little_tree(340, 60)
    happy_little_tree(350, 30)
    happy_little_tree(360, -60)
    happy_little_tree(370, 50)
    happy_little_tree(380, 30)
    happy_little_tree(390, 70)
    happy_little_tree(400, 80)
    happy_little_tree(410, 90)
    happy_little_tree(420, -30)
    happy_little_tree(430, 70)
    happy_little_tree(440, 60)
    happy_little_tree(450, 30)
    happy_little_tree(460, 40)
    happy_little_tree(450, 30)
    happy_little_tree(440, -30)
    happy_little_tree(430, 20)
    happy_little_tree(420, 10)
    happy_little_tree(410, 0)
    happy_little_tree(400, -10)
    happy_little_tree(390, -20)
    happy_little_tree(380, 30)
    happy_little_tree(370, -40)
    happy_little_tree(360, 50)


    # Call the fat tree polygon function, put it close to the comfy cabin
    fat_tree(250, -250)

    # call the comfy cabin function
    comfy_little_cabin(50, 15)

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

# Call the main function to get the program started
main()