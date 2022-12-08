"""
File: 
Name: Ting-Wen
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
circle = GOval(SIZE, SIZE, x=START_X, y=START_Y)
window = GWindow(800, 500, title='bouncing_ball.py')
window.add(circle)
circle.filled = True
start = 0  # set up a button for the ball movement only for the first click


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global start

    onmouseclicked(drop)
    # start += 1


def drop(wenny):
    global start
    gravity1 = 0
    start = 1
    if circle.x == START_X and circle.y == START_Y:
        while start == 1:  # only the first click the ball will drop
            circle.move(VX, gravity1)
            gravity1 += GRAVITY
            # print('fall')
            if circle.y + SIZE >= window.height:
                gravity1 = -(gravity1 * REDUCE)
            pause(DELAY)
            if circle.x + SIZE >= window.width:
                count = 0
                while circle.y + SIZE >= window.height:
                    count += 1
                    print(count)
                    if count == 3:  # after the circle get out of the window, it falls on the floor three times
                        window.remove(circle)
                        gravity1 = 0  # the velocity back to zero
                        start = 0
                        break
        window.add(circle, x=START_X, y=START_Y)  # add the circle back to its starting point


if __name__ == "__main__":
    main()
