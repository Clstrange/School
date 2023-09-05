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
import sys
import getopt


def walker(name, directions, lengths, trials):
    p = person.Person(
        name,
        directions
    )
    for length in lengths:
        p.take_a_walk(length, trials)
        print(p)

    return p


def main(argv):
    """The main function of the application"""
    error_message = (
        "main.py "
        + "-l <[list_of_walk_lengths]> "
        + "-t <number_of_trials> "
        + "-w <Pa,Mi-Ma,Reg,All>"
    )
    lengths = []
    trials = 0
    who = ""

    try:
        opts, args = getopt.getopt(argv, "hl:t:w:", ["lengths=",
                                                    "trials=", "who="])
    except getopt.GetoptError:
        print(error_message)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(error_message)
            sys.exit()

        if opt in ("-l", "--lengths"):
            l = arg.strip("][").split(",")
            for v in l:
                lengths.append(int(v))
        elif opt in ("-t", "--trials"):
            trials = int(arg)
        elif opt in ("-w", "--who"):
            who = arg

    if who == "All":
        pa = walker(
            "Pa",
            ["NORTH", "EAST", "SOUTH", "WEST"],
            lengths,
            trials
        )
        ma = walker(
            "Mi-Ma",
            ["NORTH", "EAST", "SOUTH", "WEST", "SOUTH"],
            lengths,
            trials
        )
        reg = walker(
            "Reg",
            ["EAST", "WEST"],
            lengths,
            trials
        )
    elif who == "Pa":
        pa = walker(
            "Pa",
            ["NORTH", "EAST", "SOUTH", "WEST"],
            lengths,
            trials
        )
    elif who == "Mi-Ma":
        ma = walker(
            "Mi-Ma",
            ["NORTH", "EAST", "SOUTH", "WEST", "SOUTH"],
            lengths,
            trials
        )
    elif who == "Reg":
        reg = walker(
            "Reg",
            ["EAST", "WEST"],
            lengths,
            trials
        )
    else:
        print(error_message)


if __name__ == '__main__':
    main(sys.argv[1:])
