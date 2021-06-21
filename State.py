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
    def __init__(self, game):
        """Perform any on-load initialisation of the state.  e.g. preload
        resources, set persistent buffer lengths, etc. """
        # Store a reference to the game object so we can refer back to it
        self.game = game

        # Here, we'll define some basic display constants which we'll want to
        # use for pretty much every state, along with empty placeholders for
        # the drawing canvas for the state.  These will be defined when the
        # state's startup code is executed
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        # Assign an instance placeholder for the drawing canvas for this state
        # We'll actually allocate this during the startup call and deallocate
        # when we exit
        self.display_surface = None
        self.display_width = None
        self.display_height = None

    def handle_events(self):
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
                self.game.is_running = False
        # End event pump

    def update(self, game_time, dt):
        """Update the simulation"""
        pass

    def display(self):
        """Draw the current frame"""
        pass

    def startup(self):
        """Perform any state specific initialisation each time the state
        becomes current (e.g. resetting scores, setting player positions,
        etc."""
        # Define the drawing surface for the state so we can render output
        self.display_surface = pygame.Surface(self.game.resolution)
        self.display_width = self.display_surface.get_width()
        self.display_height = self.display_surface.get_height()

    def cleanup(self):
        """Perform any cleanup of resources once the state is no longer
        current (e.g. clearing buffers, deallocating resources, etc."""
        # Destroy the drawing surface for the state to free memory when GC runs
        self.display_surface = None
