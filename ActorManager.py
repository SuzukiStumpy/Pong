#!/usr/bin/python3

# ActorManager.py
# A class to manage the object instances that will be generated as part of
# the game code.
#
# Author:  Mark Edwards
# Date:    26/07/2021
# Version: 0.01  -  Initial version
#
class ActorManager:
    def __init__(self, game):
        self.game = game     # Reference to the main game object
        self.objects = {}    # Dictionary containing all the basic objects
        self.instances = []  # List containing all the active actor instances

    def load_objects(self, objects):
        """Initialisation function.  Discards the current set of instantiable
        objects and allows us to specify a new set"""
        pass

    def create_instance(self, tag):
        """Creates a new instance of an Actor"""
        pass

    def destroy_instance(self, instance):
        """Destroys an instance of an Actor"""
        pass

    def update(self):
        """Update all the active instances"""

    def draw(self):
        """Draw all the active instances"""
        pass
