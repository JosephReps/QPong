'''
Scoreboard module.
'''
import pygame

class Scoreboard():
    '''
    Scoreboard class for displaying scoreboard.
    '''

    def __init__(self, x, y, message, font_size, window):
        '''
        Parameters:
            x <int>: The x position of the scoreboard.
            y <int>: The y position of the scoreboard.
            message <str>: The text to be displayed.
            font_size <int>: Size of font.
            window <pygame object>: The window to display the score on.
        '''
        self.window = window
        self.x = x
        self.y = y
        self.message = message
        self.font_size = font_size

        self.scoreboard_font = pygame.font.SysFont('Comic Sans MS', self.font_size)
    
    def display_scoreboard(self):
        '''
        Displays the scoreboard to screen.
        '''
        text_surface = self.scoreboard_font.render(self.message, False, (255, 255, 255))
        self.window.blit(text_surface, (self.x, self.y))
