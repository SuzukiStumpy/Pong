#!/usr/bin/python3

# Graphics.py
# A set of general-purpose graphics functions that can be called as needed to
# control the display
#
# Author:  Mark Edwards
# Date:    21/06/2021
# Version: 0.01  -  Initial version
#

import pygame


def draw_text(surface, text, font, size, x, y, colour):
    """Renders a text string to the specified drawing surface

    Parameters
    ----------
    surface : pygame.Surface
        The surface to which we will render the text
    text : str
        The text we want to render
    font : str
        The filename of the font we want to use for display
    size : int
        The height of the font (in pixels)
    x, y : int
        The x and y coordinates of the centre of the string
    colour : (int, int, int)
        The RGB tuple of the colour we want to display the font in
    """
    font = pygame.font.Font(font, size)
    text_surface = font.render(text, True, colour)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_surface, text_rect)
