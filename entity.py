'''
Entity module.
'''
import pygame

class Entity(pygame.sprite.Sprite):
    '''
    Base class which will be used for all entities in the game.
    '''

    def __init__(self, x, y, width, height, window, colour):
        '''
        Parameters:
            x <int>: x-position of the players shuttle.
            y <int>: x-position of the players shuttle.
            window <Pygame display>: The pygame window.
            height <int>: The height of the object.
            width <int>: The width of the object.
            colour <tuple><int>: RGB colour.
        '''
        pygame.sprite.Sprite.__init__(self)

        self.window = window
        self.colour = colour
        self.height = height
        
        self.rect = pygame.Rect(x, y, width, height)


    def draw_self(self):
        '''
        Draws object to window.
        '''
        pygame.draw.rect(self.window, self.colour, self.rect)
