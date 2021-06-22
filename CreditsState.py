#!/usr/bin/python3

# CreditsState.py
# Defines the state for showing the credits screen.  Transitioned in from the
# main menu.  Either coming to the end of the scroll, or pressing the escape
# key will exit back to the main menu
#
# Author:  Mark Edwards
# Date:    21/06/2021
# Version: 0.01  -  Initial version
#
from State import State
from Graphics import *


class Credits(State):
    def __init__(self, game):
        """Perform any on-load initialisation of the state.  e.g. preload
        resources, set persistent buffer lengths, etc. """

        # Call the parent class init method so we can make use of any generic
        # setup we can use.
        super().__init__(game)

        # Do our custom initialisation here
        self.finished = False
        self.scroll_offset = self.game.height
        self.scroll_speed = self.game.height / 10

        self.credits_surf = None    # Placeholder for the rendered credits

    def handle_events(self):
        """Run the 'event pump' and handle any events that arise.  This base
        class provides a simple event pump that merely checks the presence of
        the pressing of the space bar and raises the pygame.QUIT event.
        Processing of the pygame.QUIT event causes the game itself to
        terminate"""
        # Run event pump
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.is_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.finished = True
    # End handle events

    def update(self, game_time, dt):
        """Update the simulation"""
        # The only interaction here is if the user has pressed the escape
        # key, in which case, we simply pop this state off of the stack...
        if self.finished is True:
            self.game.state_manager.pop()

        # Move the credits up the screen.
        self.scroll_offset -= self.scroll_speed * dt

        # If we've scrolled off the top of the screen, wrap around again...
        if self.scroll_offset < -self.credits_surf.get_height():
            self.scroll_offset = self.display_height
    # End update

    def display(self):
        """Draw the current frame"""
        self.display_surface.fill(self.black)

        self.display_surface.blit(self.credits_surf, (0, self.scroll_offset))

        self.game.display_window.blit(self.display_surface, (0, 0))
    # End display

    def startup(self):
        """Perform any state specific initialisation each time the state
        becomes current (e.g. resetting scores, setting player positions,
        etc."""
        super().startup()

        # We'll generate the credits here since we want to render them to a
        # surface which we'll simply use throughout the life of the object.
        # That way, we can be more efficient.

        # The credits that we want to scroll through.  Consists of a list of
        # tuples which defines: Style (based on HTML markup tags), the Text
        # to display (line by line), the colour of the text (as an RGB tuple)
        # Where we want to add spacing, we simply add blank lines of the
        # appropriate style
        credits = [
            ("h1", "PONG", (255, 255, 161)),
            ("h2", "", (0, 0, 0)),
            ("h2", "", (0, 0, 0)),
            ("h2", "Original Concept", (255, 255, 255)),
            ("p", "Allan Alcorn", (200, 200, 200)),
            ("p", "Ted Dabney", (200, 200, 200)),
            ("p", "Nolan Bushnell", (200, 200, 200)),
            ("h1", "", (0, 0, 0)),
            ("h2", "This Implementation", (255, 255, 255)),
            ("p", "Mark Edwards", (200, 200, 200)),
            ("h1", "", (0, 0, 0)),
            ("h1", "", (0, 0, 0)),
            ("p", "Press the 'Escape' key to return to the menu", (128, 128,
                                                                   128))
        ]

        # Definitions for the various styles in the credits.  Typically
        # related to font height, but also to whether fonts are set bold or not
        styles = {
            "h1": (200, True),
            "h2": (25, True),
            "p": (20, False)
        }

        canvas_height = 0

        # Extract just the style tags from the credits list
        credit_styles = [s[0] for s in credits]

        for i in credit_styles:
            canvas_height += styles[i][0] + 5   # +5 adds a 5px buffer around
                                                # lines

        self.credits_surf = pygame.Surface((self.display_width, canvas_height))
        self.credits_surf.fill(self.black)

        # Get half the first offset for our starting point
        v_offset = 0

        for cstyle, text, colour in credits:
            draw_text(self.credits_surf,
                      text,
                      pygame.font.get_default_font(),
                      styles[cstyle][0],
                      self.display_width // 2,
                      v_offset + styles[cstyle][0] // 2,
                      colour)

            v_offset += styles[cstyle][0] + 5

    def cleanup(self):
        """Perform any cleanup of resources once the state is no longer
        current (e.g. clearing buffers, deallocating resources, etc."""
        # Destroy the drawing surface for the state to free memory when GC runs
        super().cleanup()

        # Free up the memory used by the credits surface
        self.credits_surf = None
