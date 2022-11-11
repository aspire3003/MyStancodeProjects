"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.


File:breakout.py
Name:David Lin

This is a basic breakout game which is made from breakoutgraphics.py objects and methods
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 20         # 100 frames per second
NUM_LIVES = 3		# Number of attempts


def main():
    live_count = NUM_LIVES
    graphics = BreakoutGraphics()
    graphics.set_ball_speed()
    # Add the animation loop her
    while True:
        pause(FRAME_RATE)
        if graphics.game_start:
            graphics.ball.move(graphics.get_dx(),graphics.get_dy())
            # ball rebound in window
            if graphics.ball.y < 0:
                graphics.bouncing_ball_dy()
            if graphics.ball.x + 2*graphics.ball_radius > graphics.window.width or graphics.ball.x < 0: # left and right
                graphics.bouncing_ball_dx()
            # ball fall and restart condition
            if graphics.ball.y > graphics.window.height:
                live_count -= 1
                graphics.game_start = False
                graphics.ball.x = graphics.window.width/2-graphics.ball_radius/2
                graphics.ball.y = graphics.window.height/2-graphics.ball_radius/2
                graphics.window.add(graphics.ball)
                if live_count == 0:  # game over
                    graphics.window.add(graphics.game_over_label)
                    break
            if graphics.bricks_total == 0:  # win
                graphics.ball.x = graphics.window.width / 2 - graphics.ball_radius / 2
                graphics.ball.y = graphics.window.height / 2 - graphics.ball_radius / 2
                graphics.window.add(graphics.ball)
                graphics.window.add(graphics.you_win_label)
                break
            # ball collision
            graphics.collision_check()




if __name__ == '__main__':
    main()
