"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

File:breakoutgraphics.py
Name:David Lin

This file is a class which contains the objects and methods that breakout.py game can use
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 10        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=window_width/2-paddle_width/2, y=window_height-paddle_offset+paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2-ball_radius/2, y=window_height/2-ball_radius/2)
        self.ball.filled = True
        self.window.add(self.ball)
        self.ball_radius = BALL_RADIUS

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        self.game_start = False
        onmousemoved(self.paddle_move)
        onmouseclicked(self.switch)

        # Draw bricks
        self.b_x = 0
        self.b_y = BRICK_OFFSET
        self.bricks_array()
        self.bricks_total = brick_cols*brick_cols
        # Game Over
        self.game_over_label = GLabel("Game Over", x=0, y=2*brick_height)
        # You Win
        self.you_win_label = GLabel("You Win", x=0, y=2*brick_height)

    def bricks_array(self):
        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLS):
                self.bricks = GRect(BRICK_WIDTH, BRICK_HEIGHT, x=self.b_x, y=self.b_y)
                self.bricks.filled = True
                self.bricks.fill_color = 'red'
                self.b_y += (BRICK_HEIGHT + BRICK_SPACING)
                self.window.add(self.bricks)
                if col >= 2:
                    self.bricks.fill_color = 'blue'
                if col >= 4:
                    self.bricks.fill_color = 'orange'
                if col >= 6:
                    self.bricks.fill_color = 'yellow'
                if col >= 8:
                    self.bricks.fill_color = 'green'
            self.b_y = BRICK_OFFSET
            self.b_x += (BRICK_WIDTH + BRICK_SPACING)

    def paddle_move(self, mouse):
        if 0 <= mouse.x - self.paddle.width / 2 and mouse.x + self.paddle.width / 2 <= self.window.width:
            self.paddle.x = mouse.x - self.paddle.width / 2

    def switch(self, event):
        self.game_start = True

    def set_ball_speed(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def bouncing_ball_dx(self):
        self.__dx = -self.__dx

    def bouncing_ball_dy(self):
        self.__dy = -self.__dy

    def collision_check(self):
        for i in range(0, 2, 1):
            for j in range(0, 2, 1):
                collision_ball = self.window.get_object_at(self.ball.x + i * 2 * self.ball_radius+1,  # adding 1 to make sure upper limit within the for loop(下限包含上限不包含)
                                                           self.ball.y + j * 2 * self.ball_radius+1)
                if collision_ball is not None:
                    if collision_ball is self.paddle and self.get_dy() > 0: # prevent ball bouncing in the paddle rect
                        self.bouncing_ball_dy()
                    if collision_ball is not self.paddle:
                        self.window.remove(collision_ball)
                        self.bricks_total -= 1
                        self.__dx = random.randint(1, MAX_X_SPEED)
                        self.bouncing_ball_dy()
                    return
