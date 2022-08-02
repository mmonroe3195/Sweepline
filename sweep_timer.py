"""
    File:        sweep_timer.py
    Author:      Darren Strash
    Course:      CS 307 - Computational Geometry
    Assignment:  Problem Set 2 - Line Segment Intersection
    Description: Execute sweep-line algorithm (implemented by
                 you!) and print out a table of times to show
                 growth rates.
"""


from sweep import generate_segments
from sweep import report_intersections

import datetime

NUM_ITERATIONS = 3

def average_time(the_algorithm, endpoints):
    """call the_algorithm on endpoints repeatedly and return average time"""
    time_diff = None

    for iteration in range(0, NUM_ITERATIONS):
        endpoints_copy = endpoints[:]
        start = datetime.datetime.now()
        the_algorithm(endpoints_copy)
        end = datetime.datetime.now()
        if time_diff == None:
            time_diff = end - start
        else:
            time_diff = time_diff + end - start

    time_ms = time_diff.microseconds // 1000
    time_ms = time_ms + time_diff.seconds * 1000
    time_ms = time_ms + time_diff.days * 24 * 60 * 60 * 1000

    return time_ms

def get_table_entry(num_segments, num_intersections, item):
    """get the appropriate table entry, which is either a number of segments,
       a number of intersections, or a running time"""
    endpoints = generate_segments(num_segments, num_intersections)
    if item == "n":
        return num_segments
    elif item == "I":
        return num_intersections 
    elif item == "sweep":
        return average_time(report_intersections, endpoints) 
        
    return -1

def build_header_and_legend(option):
    """construct the header entries, which are also used to fill table entries"""
    # always print n (number of vertices)
    header = ["n", "I", "sweep"]

    print("Legend:")
    print("    n      : the number of line segments")
    print("    I      : the number of intersection points")
    print("    sweep  : the running time of the sweepline algorithm (in ms)")

    return header

def run_experiment(option):
    """run the timing experiement according to the user-supplied option"""
    header = build_header_and_legend(option)

    for item in header:
        print("{:>15} ".format(item), end="")
    print("")

    for i in range(2,35):
        size = 2**i
        num_intersections = size
        max_intersections = size
        separate = False
        if option == "vary":
            num_intersections = 4
            max_intersections = (size ** 2) // 4
            separate = True

        while num_intersections <= max_intersections:
            for item in header:
                print("{:>15} ".format(get_table_entry(size, num_intersections, item)), end="")
            num_intersections = 2 * num_intersections
            print("")
        if separate:
            print("")

def main():
    """Get user input and run appropriate timing experiment."""
    print("Welcome to Sweep Timer! Press Ctrl+C at any time to end...")

    option = input("Which test would you like to run (same,vary)? ")
    while option not in ["same", "vary"]:
        print("Unrecognized option '", option, "'")
        option = input("Which test would you like to run? (same,vary)?")

    if option == "same":
        print("Running algorithm with n segments and I=n intersections.")
        print("To vary the number of intersections, run test 'vary'.")
    elif option == "vary":
        print("Running algorithm with n segments and I (variable) intersections.")
    else:
        print("This shouldn't happen...")

    run_experiment(option)

if __name__ == "__main__":
    main()
