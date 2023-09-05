"""
main.py

This module, written by Paul Strange, handles a "person" performing a
random walk.

TODO:
    * Verify text formatting in text output to match that from the
      assignment
    * Test case #7 talks about a random number seed, I do not use a
      seed for the random number generator.  Verify if seed is required.
    * Test case #9 discuses lists, tuples, and dictionaries.  While
      those are used, I also use classes.  Verify if classes are ok.
    * Test case #11 is unsatisfied
    * Test case #13, I do not know what the required docstring
      information is
    * Test case #16, I do not use Thonny or pylint, verify with one or
      both
    * Text case #17 is unsatisfied

LICENSE: This is private software for the sole use of Cody Strange.  Not
to be used for actual assignment.
"""
import person


def main():
    """The main function of the application"""
    pa = person.Person(
        "Pa"
    )
    pa.take_a_walk(100, 50)
    print(pa)
    pa.take_a_walk(1000, 50)
    print(pa)

    ma = person.Person(
        "Mi-Ma",
        ["NORTH", "EAST", "SOUTH", "WEST", "SOUTH"]
    )
    ma.take_a_walk(100, 50)
    print(ma)
    ma.take_a_walk(1000, 50)
    print(ma)

    reg = person.Person(
        "Reg",
        ["EAST", "WEST"]
    )
    reg.take_a_walk(100, 50)
    print(reg)
    reg.take_a_walk(1000, 50)
    print(reg)


if __name__ == '__main__':
    main()
