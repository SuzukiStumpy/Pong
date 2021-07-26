#!/usr/bin/python3

# MainGameState.py
# A state class for the game logic itself.  Called from the main menu state
#
# Author:  Mark Edwards
# Date:    05/07/2021
# Version: 0.01  -  Initial version
#
from State import State
from Graphics import *
import math


class MainGame(State):
    def __init__(self, game):
        """Performs any on-load initialisation of the state.  e.g. preloading
        of resources, set persistent buffer lengths, etc."""

        # Call the parent class init method (just in case there's setup in
        # there we need to also use.
        super().__init__(game)

        # Do our custom initialisation here
        self.score_p1 = 0
        self.score_p2 = 0
        self.num_players = 0
        self.game_is_running = False

        self.p1_down = False
        self.p1_up = False
        self.p2_down = False
        self.p2_up = False

        self.playfield = None

    def handle_events(self):
        """Run the 'event pump' for this particular state.  Note that we
        don't call the superclass handler here as each state should
        individually process the state messages"""
        for event in pygame.event.get():
            # First check to see if the game is quitting
            if event.type == pygame.QUIT:
                self.game_is_running = False

            # Check to see if the user has pressed a key, if so, set the
            # appropriate flags
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_is_running = False
                if event.key == pygame.K_a:
                    self.p1_up = True
                if event.key == pygame.K_z:
                    self.p1_down = True
                if event.key == pygame.K_COMMA:
                    self.p2_down = True
                if event.key == pygame.K_l:
                    self.p2_up = True
    # End handle_events

    def update(self, game_time, dt):
        """Update the simulation"""
        if not self.game_is_running:
            self.game.state_manager.pop()

    # End update

    def display(self):
        """Draw the current frame"""
        # We don't need to worry about clearing the previous frame since the
        # playfield will obscure everything
        self.display_surface.blit(self.playfield, (0, 0))

        # Display the drawing canvas on the game window...
        self.game.display_window.blit(self.display_surface, (0, 0))
    # End display

    def startup(self):
        """Perform any state specific initialisation each time the state
        becomes current (e.g. resetting scores, setting player positions,
        etc."""
        super().startup()

        # Load in the background playfield and assign to a surface so we can
        # simply blit it as needed
        self.playfield = pygame.image.load("playfield.png")
        self.playfield.convert()

        self.game_is_running = True

    def cleanup(self):
        """Perform any cleanup of resources once the state is no longer
        current (e.g. clearing buffers, deallocating resources, etc."""
        super().cleanup()
