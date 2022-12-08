"""
File: 
Name: Ting Wen
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the GOval
SIZE = 20
circle = GOval(SIZE, SIZE)
window = GWindow()
count = 0


def main():
    """
    This program creates lines on an instance of GWindow class. There is a circle indicating the user’s first click. A
    line appears at the condition where the circle disappears as the user clicks on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(wenny):
    global count, circle
    if count % 2 != 0:
        line = GLine(circle.x, circle.y, wenny.x, wenny.y)
        window.add(line)
        # maybe_obj = window.get_object_at(circle.x, circle.y)
        # if maybe_obj is not None:
        #     window.remove(maybe_obj)
        window.remove(circle)
        count += 1

    else:
        circle = GOval(SIZE, SIZE, x=wenny.x - circle.width / 2, y=wenny.y - circle.height / 2)
        circle.filled = True
        circle.fill_color = "white"
        window.add(circle)
        count += 1


if __name__ == "__main__":
    main()
