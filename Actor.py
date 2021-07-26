#!/usr/bin/python3

# Actor.py
# A class for defining the general object behaviour within the game
#
# Author:  Mark Edwards
# Date:    26/07/2021
# Version: 0.01  -  Initial version
#


class Actor:
    def __init__(self, manager, tag):
        """Performs any on-load initialisation of the Actor such as defining
        sensible defaults for any instance level variables"""
        self.x = self.y = 0
        self.direction = self.speed = self.acceleration = 0
        self.heading = 0
        self.manager = manager
        self.solid = self.visible = False
        self.active = self.dying = False
        self.tag = tag
        self.id = ""  # ID will be set when the object is instantiated.

    def create(self):
        """Code that executes when an instance of the object is created"""
        pass

    def update(self):
        """Code that executes once per cycle through the inner game loop"""
        pass

    def draw(self):
        """Code that executes once per frame to draw the actor"""
        pass

    def die(self):
        """Code that executes when the actor goes out of scope"""
        pass

    def on_collide(self, other):
        """Code that executes when the actor collides with another object"""
        pass
