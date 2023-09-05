"""
person.py

This module, written by Paul Strange, handles a person performing a
random walk.

To instantiate a person, enter:

person = Person(aPersonName, [walkDirections])

Person methods:

take_a_walk(steps, trials)

LICENSE: This is private software for the sole use of Cody Strange.  Not
to be used for actual assignment.
"""

import statistics as stat
import random as rand
import math


class Trial:
    def __init__(self, assigned_max=0.0):
        self.max = assigned_max
        self.min = 9999999999999.0
        self.steps = []
        self.max_coordinate = [0, 0]
        self.min_coordinate = [0, 0]

    def add_step(self, step):
        """Add a step to the trial"""
        self.steps.append(step)

    def min_max(self, step, dist):
        """Find the min and max for the trial"""
        if self.max < dist:
            self.max = dist
            self.max_coordinate = step

        if self.min > dist:
            self.min = dist
            self.min_coordinate = step

    def get_max(self):
        """Return the max distance"""
        return self.max

    def get_max_coordinate(self):
        """Return the max coordinate"""
        return self.max_coordinate

    def get_min(self):
        """Return the min distance"""
        return self.min


class Walk:
    def __init__(self, walk_directions):
        self.walk_directions = walk_directions
        self.step_count = 0
        self.steps = []
        self.trials = []
        self.max_trial = Trial()
        self.min_trial = Trial(9999999999)

    def find_min_max_trial(self, current_trial):
        """Find the min and the max for the output"""
        if self.max_trial.get_max() < current_trial.get_max():
            self.max_trial = current_trial

        if self.min_trial.get_max() > current_trial.get_max():
            self.min_trial = current_trial

    def take_a_walk(self, step_count, trial_count):
        """Perform the random walk"""
        self.step_count = step_count

        for t in range(trial_count):
            last = [0, 0]
            this_trial = Trial()
            this_trial.add_step(last)
            self.trials.append(this_trial)

            for s in range(1, step_count):
                direction = rand.choice(self.walk_directions)
                step = [0, 0]

                if direction == "NORTH":
                    step[0] = last[0]
                    step[1] = last[1] + 1
                elif direction == "EAST":
                    step[0] = last[0] + 1
                    step[1] = last[1]
                elif direction == "SOUTH":
                    step[0] = last[0]
                    step[1] = last[1] - 1
                else:
                    step[0] = last[0] - 1
                    step[1] = last[1]

                dist = math.dist([0, 0], step)
                self.steps.append(dist)
                this_trial.add_step(step)
                this_trial.min_max(step, dist)
                last = step

            self.find_min_max_trial(this_trial)

    def __str__(self):
        """Create the output as required by the assignment"""
        mean = stat.mean(self.steps)
        sd = stat.stdev(self.steps, mean)
        return (
            "Mean = " + "{:.1f}".format(mean)
            + " CV = " + "{:.1f}".format(sd/mean)
            + "\n"
            + "Max = " + "{:.1f}".format(self.max_trial.get_max())
            + " Min = " + "{:.1f}".format(self.min_trial.get_max())
            + "\n"
        )


class Person:
    def __init__(self, name, walk_directions=None):
        self.name = name
        if walk_directions is None:
            self.walk_directions = ["NORTH", "EAST", "SOUTH", "WEST"]
        else:
            self.walk_directions = walk_directions
        self.walk = Walk(self.walk_directions)
        self.step_count = 0

    def take_a_walk(self, step_count, trial_count):
        """Perform the random walk"""
        self.step_count = step_count
        self.walk = Walk(self.walk_directions)
        self.walk.take_a_walk(step_count, trial_count)

    def __str__(self):
        """Create the output as required by the assignment"""
        return (
            self.name
            + " random walk of "
            + str(self.step_count)
            + " steps"
            + "\n"
            + str(self.walk)
        )
