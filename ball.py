'''
Module for the pong-ball.
'''
import pygame
import entity
import random

class Ball(entity.Entity):
    '''
    Pong ball class.
    Controls movement/reset fnctions of ball.
    '''

    def __init__(self, x, y, width, height, window, colour, x_speed, y_speed):
        '''
        Parameters:
            x <int>: x-position of the players shuttle.
            y <int>: x-position of the players shuttle.
            window <Pygame display>: The pygame window.
        '''
        super().__init__(x, y, width, height, window, colour)

        self.x_speed = x_speed
        self.y_speed = y_speed

    def move_ball(self):
        '''
        Moves the ball.
        '''
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

    def reset_ball(self):
        '''
        Returns the ball to the center of the screen, with a random speed.
        '''
        self.rect.x = 500
        self.rect.y = 500

        x_speeds = [random.randint(-1, -1), random.randint(1,1)]
        self.x_speed = random.choice(x_speeds)

        y_speeds = [random.randint(-1, -1), random.randint(1,1)]
        self.y_speed = random.choice(y_speeds)