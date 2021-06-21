#!/usr/bin/python3

# State.py
# A general definition of a State within a game.  Serves as a base class for
# specific states defined per-game.
#
# Author:  Mark Edwards
# Date:    20/06/2021
# Version: 0.01  -  Initial version
#
import pygame


# A generic state to be managed via the StateManager object.  Note that all
# methods expect the first passed parameter to be a reference to the actual
# game object itself.  This allows for access to any global elements stored
# within the main game object itself (e.g. the game.is_running flag
# referenced in the handle_events() method
class State:
    def __init__(self):
        """Perform any on-load initialisation of the state.  e.g. preload
        resources, set persistent buffer lengths, etc. """
        pass

    def handle_events(self, game):
        """Run the 'event pump' and handle any events that arise.  This base
        class provides a simple event pump that merely checks the presence of
        the pressing of the space bar and raises the pygame.QUIT event.
        Processing of the pygame.QUIT event causes the game itself to
        terminate"""
        # Run event pump
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
            if event.type == pygame.QUIT:
                game.is_running = False
        # End event pump

    def update(self, game):
        """Update the simulation"""
        pass

    def display(self, game):
        """Draw the current frame"""
        pass

    def startup(self, game):
        """Perform any state specific initialisation each time the state
        becomes current (e.g. resetting scores, setting player positions,
        etc."""
        pass

    def cleanup(self, game):
        """Perform any cleanup of resources once the state is no longer
        current (e.g. clearing buffers, deallocating resources, etc."""
        pass
