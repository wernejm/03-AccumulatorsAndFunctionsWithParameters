"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and James Werne.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:

    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------

    window = rg.RoseWindow(400,400)

    circle1 = rg.Circle(rg.Point(300, 150), 100)
    circle1.fill_color = 'blue'
    circle2 = rg.Circle(rg.Point(145, 230), 50)

    circle1.attach_to(window)
    circle2.attach_to(window)

    window.render()
    window.close_on_mouse_click()



def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------

    window = rg.RoseWindow(400,400)

    xcentcirc = 100
    ycentcirc = 75
    xcentrec = (200 + 325)/2
    ycentrec = (35 + 250)/2


    circle = rg.Circle(rg.Point(xcentcirc, ycentcirc), 70)
    circle.fill_color = 'blue'
    circle.outline_thickness = 7

    rectangle = rg.Rectangle(rg.Point(200, 35), rg.Point(325, 250))
    rectangle.outline_thickness = 3

    circle.attach_to(window)
    rectangle.attach_to(window)



    ## Print Statements
    print('      Circle Properties:      ')
    print('Outline Thickness: ', circle.outline_thickness )
    print('Fill Color: ', circle.fill_color)
    print('Center: (', xcentcirc, ',', ycentcirc, ')')
    print('Center X Coordinate: ', xcentcirc)
    print('Center Y Coordinate: ', ycentcirc)

    print('      Rectangle Properties:     ')
    print('Outline Thickness: ', rectangle.outline_thickness)
    print('Fill Color: ', rectangle.fill_color)
    print('Center: (', xcentrec, ',', ycentrec, ')')
    print('Center X Coordinate: ', xcentrec)
    print('Center Y Coordinate: ', ycentrec)



    window.render()
    window.close_on_mouse_click()


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # DONE: 4. Implement and test this function.


    window = rg.RoseWindow(400, 400)

    line = rg.Line(rg.Point(50, 300), rg.Point(190, 270))

    thickline = rg.Line(rg.Point(115, 20), rg.Point(327, 35))
    thickline.thickness = 6
    thickline.get_midpoint()

    line.attach_to(window)
    thickline.attach_to(window)

    # Print Statements

    print('Midpoint of Thicker Line: ', thickline.get_midpoint())
    print('221.0')
    print('27.5')

    window.render()
    window.close_on_mouse_click()



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
