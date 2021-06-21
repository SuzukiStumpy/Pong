#!/usr/bin/python3

# StateManager.py
# The main state management function.  Has responsibility for loading and
# initialising each individual state within the game, and for marshalling the
# current state into and out of scope.  If the state stack ever becomes
# empty, then the State Manager will terminate the game.
#
# Author:  Mark Edwards
# Date:    20/06/2021
# Version: 0.01  -  Initial version
#
import importlib
import sys


class StateManager:
    def __init__(self, states, game):
        """Initialises the StateManager object and checks and loads the
        initial set of states into the system.  Ensures that the default
        state is pushed onto the state stack and sets the current_state
        variable to point to it so that the program can begin execution"""

        # Store a reference to the enclosing 'game' object.  This allows us to
        # terminate the program execution should the state stack become empty.
        self._game = game

        # State_stack is a list which contains the set of currently executing
        # states.  The state at the end of the list is the current active state
        self.state_stack = []
        self.current_state = None

        # Load the states and bootstrap the state manager
        # States is stored as a dictionary so we can refer to states by name
        self.states = self._load_states(states)

    def push(self, state):
        """Adds the specified state to the end of the state_stack list and
        updates the current_state instance variable.  Also causes the new
        state to perform any required setup tasks before it kicks in"""
        self.state_stack.append(state)
        self.current_state = self.state_stack[-1]
        self.current_state.startup(self._game)

    def pop(self):
        """Removes the currently executing state from the stack and, if there
        are any remaining states, updates the current_state instance variable
        to point back to it.  If there are no remaining states, then exits
        the game"""
        # Perform any necessary cleanup functionality before terminating the
        # state
        self.current_state.cleanup(self._game)
        self.state_stack.pop()

        # Terminate the game if we've popped the last item from the stack...
        if len(self.state_stack) == 0:
            self._game.is_running = False
        else:
            self.current_state = self.state_stack[-1]

    def _load_states(self, states):
        """Private method used to load the state matrix into the StateManager
        object from their individual modules"""
        state_defs = {}

        for this_state in states:
            try:
                # Do the import
                module = importlib.import_module(this_state['file'])
                class_ = getattr(module, this_state['name'])
                state_defs[this_state['name']] = class_()
            except ModuleNotFoundError:
                # Raise an exception on error
                print(f"The module "
                      f"{this_state['file']}.py could not be loaded.  Aborting.")
                sys.exit(ModuleNotFoundError)
            except AttributeError:
                # Raise an exception on error
                print(f"The class {this_state['name']} cound not be found in "
                      f"module {this_state['file'].py}.  Aborting.")
                sys.exit(AttributeError)

            if this_state['default'] is True:
                self.push(state_defs[this_state['name']])

        # Now that we've imported all the states, invalidate the cache so
        # that Python can recognise the new code
        importlib.invalidate_caches()

        return state_defs
