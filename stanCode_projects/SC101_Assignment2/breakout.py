"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
import random

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = 0
    # Add the animation loop here!
    while True:
        #milestone 4
        bricknums = graphics.brick_cols*graphics.brick_rows
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            graphics.reset()
            lives+=1
            if lives==NUM_LIVES:
                break
        if bricknums ==0:
            break

        graphics.ball.move(graphics.get_dx(),graphics.get_dy())
        maybe_obj = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        if maybe_obj is not None:
            if maybe_obj is graphics.paddle:
                if graphics.get_dy() > 0:
                    graphics.set_dy()
            else:
                graphics.set_dy()
                graphics.window.remove(maybe_obj)
                bricknums-=1
        else:
            maybe_obj = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y)
            if maybe_obj is not None:
                if maybe_obj is graphics.paddle:
                    if graphics.get_dy()>0:
                        graphics.set_dy()
                else:
                    graphics.set_dy()
                    graphics.window.remove(maybe_obj)
                    bricknums -= 1
            else:
                maybe_obj = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height)
                if maybe_obj is not None:
                    if maybe_obj is graphics.paddle:
                        if graphics.get_dy() > 0:
                            graphics.set_dy()
                    else:
                        graphics.set_dy()
                        graphics.window.remove(maybe_obj)
                        bricknums -= 1
                else:
                    maybe_obj = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y +
                                                              graphics.ball.height)
                    if maybe_obj is graphics.paddle:
                        if graphics.get_dy() > 0:
                            graphics.set_dy()
                    elif maybe_obj is not None:
                        graphics.set_dy()
                        graphics.window.remove(maybe_obj)
                        bricknums -= 1

        if graphics.ball.x<0:
            graphics.set_dx()
        if graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.set_dx()
        if graphics.ball.y<0:
            graphics.set_dy()
        pause(FRAME_RATE)       # 100 frames per second






if __name__ == '__main__':
    main()
