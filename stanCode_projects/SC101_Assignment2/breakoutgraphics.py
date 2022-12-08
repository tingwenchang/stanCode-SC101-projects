"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.brick_cols = brick_cols
        self.brick_rows = brick_rows
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle=GRect(paddle_width,paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle,x= (self.window.width-self.paddle.width)/2, y=self.window.height-paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(2 * ball_radius, 2 * ball_radius)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)
        # Default initial velocity for the ball
        # Initialize our mouse listeners
        onmouseclicked(self.drop)
        onmousemoved(self.change_position)
        self.__dx=0
        self.__dy = 0

        # Draw bricks
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if j == 0 or j == 1:
                    self.brick.fill_color = 'red'
                    self.brick.color="red"
                if j == 2 or j == 3:
                    self.brick.fill_color = 'orange'
                    self.brick.color = "orange"
                if j == 4 or j == 5:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = "yellow"
                if j == 6 or j == 7:
                    self.brick.fill_color = 'green'
                    self.brick.color = "green"
                if j == 8 or j == 9:
                    self.brick.fill_color = 'blue'
                    self.brick.color = "blue"
                self.window.add(self.brick, x=i * (brick_width + brick_spacing), y=brick_offset+j *
                                                                                   (brick_height + brick_spacing))

    def change_position(self,Wenny):
        self.paddle.x = Wenny.x-self.paddle.width/2
        if self.paddle.x > self.window.width - self.paddle.width:
            self.paddle.x = self.window.width - self.paddle.width
        if self.paddle.x < 0:
            self.paddle.x = 0

    def drop(self,Wenny):
        if self.__dx ==0 and self.__dy ==0:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if (random.random() > 0.5):
                self.__dx = -self.__dx


    def get_dx(self):
        #self.__dx = random.randint(1, MAX_X_SPEED)
        return self.__dx

    def get_dy(self):
        #self.__dy = INITIAL_Y_SPEED
        return self.__dy

    def set_dx(self):
        self.__dx = -self.__dx

    def set_dy(self):
        self.__dy = -self.__dy

    def reset(self):
        self.__dx = 0
        self.__dy = 0
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                            y=(self.window.height - self.ball.height) / 2)





