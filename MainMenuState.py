#!/usr/bin/python3

# MainMenuState.py
# A state class for the main menu displayed in the game.  This will become
# the default state when we finally piece everything together and will
# display the initial menu/splash screen to the user.
#
# Author:  Mark Edwards
# Date:    21/06/2021
# Version: 0.01  -  Initial version
#
from State import State
from Graphics import *
import math


class MainMenu(State):
    def __init__(self, game):
        """Performs any on-load initialisation of the state.  e.g. preloading
        of resources, set persistent buffer lengths, etc."""

        # Call the parent class init method (just in case there's setup in
        # there we need to also use.
        super().__init__(game)

        # Do our custom initialisation here
        self.up = self.down = self.select = False

        # List of entries in the menu.  Each element is a tuple consisting of
        # the text to display, the y offset (in pixels from the top of the menu)
        # the colour of the text to render as an RGB tuple and finally a lambda
        # defining what we want to do when the menu item is selected.
        self.entries = [
            ("One Player", 0, (255, 255, 255),
                lambda: print("Start game one player")),
            ("Two Player", 25, (255, 255, 255),
                lambda: print("Start game two player")),
            ("Options", 60, (200, 200, 200),
                lambda: print("Show options menu")),
            ("Credits", 85, (200, 200, 200),
                lambda: print("Show credits")),
            ("Quit", 125, (128, 128, 128),
                lambda: pygame.event.post(pygame.event.Event(pygame.QUIT)))
        ]
        self.current_entry = 0   # Index of the currently selected menu item
        self.selected_pulse = 0  # Will be used to increase/decrease the size
                                 # of the selected menu item
        self.max_menu = len(self.entries)-1
        self.last_update = 0.0

    def handle_events(self):
        """Run the 'event pump' for this particular state.  Note that we
        don't call the superclass handler here as each state should
        individually process the state messages"""
        for event in pygame.event.get():
            # First, check to see if we're quitting the game
            if event.type == pygame.QUIT:
                self.game.is_running = False

            # Check to see if the user has pressed or released a key, if so,
            # set the appropriate flags
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.down = True
                if event.key == pygame.K_UP:
                    self.up = True
                if event.key == pygame.K_SPACE:
                    self.select = True
    # End handle_events

    def update(self, game_time, dt):
        """Update the simulation"""
        # We want to throttle the update of the menu items so that the cursor
        # doesn't move faster than the user can perceive it, so we'll limit
        # our updates to once every 0.25 seconds
        if self.last_update < game_time - 0.125:
            self.last_update = game_time

            if self.down is True and self.current_entry < self.max_menu:
                self.current_entry += 1
            if self.up is True and self.current_entry > 0:
                self.current_entry -= 1

            self.up = self.down = False

        if self.select is True:
            _, _, _, x = self.entries[self.current_entry]
            x()
            self.select = False
    # End update

    def display(self):
        """Draw the current frame"""
        self.display_surface.fill(self.black)

        # Show the title text
        draw_text(self.display_surface,
                  "PONG",
                  pygame.font.get_default_font(), 200,
                  self.display_width // 2,
                  200, (255, 255, 161))

        # Render the menu entries
        for idx in range(len(self.entries)):
            text, y_offset, colour, _ = self.entries[idx]

            # Set the size so the current entry 'pulses'
            if idx == self.current_entry:
                size = int(25 + 5 * math.sin(
                    self.selected_pulse))
                self.selected_pulse += 2 * self.game.dt
            else:
                size = 20

            draw_text(self.display_surface,
                      text,
                      pygame.font.get_default_font(), size,
                      self.display_width // 2,
                      self.display_height // 2 + y_offset,
                      colour)

        # Display the drawing canvas on the game window...
        self.game.display_window.blit(self.display_surface, (0, 0))
    # End display

    def startup(self):
        """Perform any state specific initialisation each time the state
        becomes current (e.g. resetting scores, setting player positions,
        etc."""
        super().startup()

    def cleanup(self):
        """Perform any cleanup of resources once the state is no longer
        current (e.g. clearing buffers, deallocating resources, etc."""
        super().cleanup()
