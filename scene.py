# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, left_bound=0, bottom_bound=285, right_bound=800, top_bound=500)
    draw_mountain(canvas)
    draw_land(canvas, left_bound=0, bottom_bound=0, right_bound=800, top_bound=280)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

# Define your functions such as
# draw_sky and draw_ground here.


def draw_sky(canvas, left_bound, bottom_bound, right_bound, top_bound):
    draw_rectangle(canvas, left_bound, bottom_bound, right_bound, top_bound, fill="lightCyan2")

    draw_sun(canvas)
    draw_clouds(canvas, x0=590, y0=405, x1=710, y1=450)
    draw_clouds(canvas, x0=245, y0=405, x1=405, y1=440)
    draw_bird(canvas, start_x=300, start_y=425, left_wing_x=305, left_wing_y=430, left_body_x=320,
              left_body_y=418, right_body_x=335, right_body_y=430, right_wing_x=340, right_wing_y=425, distance=50)

def draw_sun(canvas):
    """Draw sun's ring, and rays"""

    # ring
    draw_oval(canvas, 100, 300, 200, 400, fill="orange", outline="")
    draw_oval(canvas, 105, 295, 195, 395, fill="yellow", outline="")

    # rays
    draw_line(canvas, 100, 380, 0, 430, width=6, fill="yellow")
    draw_line(canvas, 120, 400, 75, 445, width=6, fill="orange")
    draw_line(canvas, 150, 410, 150, 500, width=6, fill="yellow")
    draw_line(canvas, 190, 400, 250, 450, width=6, fill="orange")
    draw_line(canvas, 200, 380, 380, 500, width=6, fill="yellow")

def draw_clouds(canvas, x0, y0, x1, y1):
    # draw_line(canvas, 600, 400, 700, 400, fill="white", width=3)
    # draw_oval(canvas, 590, 400, 610, 425, fill="white")
    scene_width = 800
    scene_height = 500
    half_height = round(scene_height / 2)
    min_diam = 30
    max_diam = 30
    for i in range(40):
        x = random.randint(x0, x1)
        y = random.randint(y0, y1)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                  fill="white", outline="")

def draw_bird(canvas, start_x, start_y, left_wing_x, left_wing_y, left_body_x, left_body_y, right_body_x,
              right_body_y, right_wing_x, right_wing_y, distance):
    """Draw 5 birds using for loop"""

    for i in range(1, 6):
        # Loop five time to draw 5 birds

        if i % 2 == 0:
            start_x += distance
            left_wing_x += distance
            left_body_x += distance
            right_body_x += distance
            right_wing_x += distance
            draw_line(canvas, start_x, start_y-distance, left_wing_x, left_wing_y-distance, left_body_x,
                      left_body_y-distance, right_body_x, right_body_y-distance, right_wing_x, right_wing_y-distance, width=2, fill="black")
        else:
            start_x += distance
            left_wing_x += distance
            left_body_x += distance
            right_body_x += distance
            right_wing_x += distance

            draw_line(canvas, start_x, start_y, left_wing_x, left_wing_y, left_body_x, left_body_y,
                      right_body_x, right_body_y, right_wing_x, right_wing_y, width=2, fill="black")

def draw_land(canvas, left_bound, bottom_bound, right_bound, top_bound):
    """Draw grass, and call draw road function"""

    # grass
    draw_rectangle(canvas, left_bound, bottom_bound,
                   right_bound, top_bound, fill="springGreen3")

    draw_road(canvas)

def draw_road(canvas):
    """Draw the lines on the road, and call car function.

    Parameters
        canvas: Where the function will draw the road and car
    """

    # asphalt
    draw_polygon(canvas,
                 50, 0, 700, 0, 400, 300, 350, 300, outline="", fill="gray51")

    # left white line
    draw_line(canvas, 60, 0, 360, 300, width=4, fill="white")

    # right white line
    draw_line(canvas, 690, 0, 390, 300, width=4, fill="white")

    # dividing yellow line
    draw_polygon(canvas,
                 365, 0, 385, 0, 375, 300, outline="", fill="goldenrod1")

    draw_car(canvas)

def draw_car(canvas):
    """Draw car parts."""

    # wheels and underbody
    draw_polygon(canvas, 420, 10, 420, 40, 530, 40, 530, 10, 550,
                 10, 550, 50, 400, 50, 400, 10, width=2, fill="black")

    # left tire stripes
    draw_line(canvas, 405, 50, 405, 15, fill="white")
    draw_line(canvas, 410, 50, 410, 25, fill="white")
    draw_line(canvas, 415, 50, 415, 15, fill="white")

    # right tire stripes
    draw_line(canvas, 535, 50, 535, 15, fill="white")
    draw_line(canvas, 540, 50, 540, 25, fill="white")
    draw_line(canvas, 545, 50, 545, 15, fill="white")

    # trunk
    draw_polygon(canvas, 390, 60, 405, 40, 545, 40,
                 560, 60, 390, 60, fill="white")
    draw_line(canvas, 398, 50, 552, 50, width=2)
    draw_polygon(canvas, 390, 60, 405, 65, 545, 65, 560, 60, fill="black")

    # headlights and plate number
    draw_rectangle(canvas, 405, 65, 545, 90, fill="steelBlue")
    draw_rectangle(canvas, 450, 67, 500, 85, fill="white")
    draw_text(canvas, 475, 75, "CSE111", fill="black")
    draw_oval(canvas, 410, 70, 425, 85, fill="yellow")
    draw_oval(canvas, 430, 70, 445, 85, fill="yellow")
    draw_oval(canvas, 505, 70, 520, 85, fill="yellow")
    draw_oval(canvas, 525, 70, 540, 85, fill="yellow")

    # roof
    draw_polygon(canvas, 405, 90, 420, 145, 530, 145,
                 545, 90, outline="", fill="turquoise")

    # rear windshield
    draw_polygon(canvas, 415, 100, 425, 135, 525,
                 135, 535, 100, fill="floralWhite")

def draw_mountain(canvas):
    """Draw Mountain Range"""

    draw_polygon(canvas,
                 0, 280, 800, 280, 800, 325, 675, 375, 450, 325, 275, 400, 150, 350, 0, 400, outline="slateGray4", fill="steelBlue")

# Call the main function so that
# this program will start executing.
main()
