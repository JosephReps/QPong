'''
Module for player.
'''
import pygame
import entity

class Player(entity.Entity):
    '''
    Player class.
    '''

    def __init__(self, x, y, width, height, window, colour, speed):
        '''
        Parameters:
            speed <int>: The speed of the player.
        '''
        super().__init__(x, y, width, height, window, colour)

        self.speed = speed
        self.score = 0

    def perform_action(self, action, ball_y, app, agent):
        '''
        Performs a player action.

        Parameters:
            action <int>: 0 or 1, corresponding to up and down movement.
            ball_y <int>: The y position of the ball.
            app <PongApp object>: The main game object.
            agent <str>: Which agent is performing the action.
        '''
        y_difference = abs(self.rect.center[1] - ball_y)

        if action == 0:
            if self.rect.y > 0:
                self.rect.y -= self.speed 

                if abs(self.rect.center[1] - ball_y) < y_difference:

                    ##
                    ## I know there is a better way of doing this but I just wanted to
                    ## get the learning working.
                    ##
                    ## Rewards the agent for moving towards the ball.
                    ## Punishes for moving away.
                    ##

                    if agent == "agent_1":
                        app.agent_1_reward = 0.5
                    elif agent == "agent_2":
                        app.agent_2_reward = 0.5
                else:
                    if agent == "agent_1":
                        app.agent_1_reward = -0.7
                    elif agent == "agent_2":
                        app.agent_2_reward = -0.7

        elif action == 1:
            if self.rect.y < 1000 - self.height:
                self.rect.y += self.speed 
                if abs(self.rect.center[1] - ball_y) < y_difference:
                    if agent == "agent_1":
                        app.agent_1_reward = 0.7
                    elif agent == "agent_2":
                        app.agent_2_reward = 0.7

                else:
                    if agent == "agent_1":
                        app.agent_1_reward = -0.7
                    elif agent == "agent_2":
                        app.agent_2_reward = -0.7