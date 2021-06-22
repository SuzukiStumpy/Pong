#!/usr/bin/python3

# pong.py
# A Python implementation of the original Atari Pong using the pygame library
#
# Author:  Mark Edwards
# Date:    14/06/2021
# Version: 0.01  -  Initial version
#

import time
import pygame
import StateManager


class Game:
    """The main object used in the game"""

    def __init__(self, state_defs):
        """Perform the basic initialisation and set up the screen"""
        pygame.init()

        # Define the screen dimensions and initialise the display
        self.resolution = (self.width, self.height) = (1024, 768)
        #display_flags = pygame.FULLSCREEN | pygame.SCALED
        display_flags = pygame.SCALED

        #  Probably don't need this in the game object
        #  itself.
        #  self.display_surface = pygame.Surface(self.resolution)
        self.display_window = pygame.display.set_mode(
            self.resolution,
            display_flags)

        # Perform any global game specific setup here
        self.frames_per_second = 60
        self.dt = 1/self.frames_per_second
        self.is_running = True  # This is the terminator for the main loop

        # Define and initialise the state manager (do this last so we have
        # the game class otherwise all set up
        self.state_manager = StateManager.StateManager(state_defs, self)
    # End method __init__

    def run(self):
        """The main game loop"""
        # First, set up the frame timers
        t = 0.0
        current_time = time.perf_counter()
        accumulator = 0.0

        while self.is_running:
            new_time = time.perf_counter()
            frame_time = new_time - current_time
            current_time = new_time

            accumulator += frame_time

            # Run update loop
            while accumulator >= self.dt:
                # Run the event pump
                self.state_manager.current_state.handle_events()

                # Do update code
                self.state_manager.current_state.update(t, self.dt)

                accumulator -= self.dt
                t += self.dt
            # End update loop

            # Do render
            self.state_manager.current_state.display()
            pygame.display.flip()

        # End main loop
    # End method run
# End class Game


if __name__ == '__main__':
    states = [
        {"name": "MainMenu", "file": "MainMenuState", "default": True},
        {"name": "Credits", "file": "CreditsState", "default": False},
    ]
    game = Game(states)
    game.run()
