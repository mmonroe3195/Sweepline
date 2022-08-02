"""
    File:        sweep.py
    Author:      Madison Monroe
    Course:      CS 307 - Computational Geometry
    Collaborators: Andrea and AJ
    Assignment:  Problem Set 2 - Line Segment Intersection
    Description: Methods to generate horizontal and vertical segments
    and compute their intersection points.
"""
from typing import List, Tuple
from sortedcontainers import SortedList
import random
import math

def valid_segment_list(segments):
    """Check is a list is a valid segment list."""

    if type(segments) != list or len(segments) % 2 != 0:
        return False

    for value in segments:
        if type(value) != tuple or len(value) != 2:
            return False

    return True

def generate_segments(num_segments : int, num_intersections: int) -> List[Tuple[int,int]]:
    """
    Generate a list of num_segments horizontal and vertical line segments.

        Keyword arguments:
        num_segments      -- the number of segments to generate
        num_intersections -- the number of intersections between
                             the generated segments

    Return a list of integer tuples (pairs). Supposing the list
    is called segments, line segment i is stored as endpoints
    in segment[2i] and segment[2i+1].

    My comments on how I generate the line segments to have the appropriate
    number of intersections:
    I used a similar method to what we talked about in office hours. First,
    chose the number of horizonal and vertical line segments I wanted. I used
    math.ceil(num_segments / 2) to choose the number of horizonal and calculated
    the vertical ones from there. Next, I created my horizonal lines segments.
    The trickier part was doing the vertical lines segments. I changed the
    length of my vertical line segments based on how many intersections needed.
    Once I reached the desired number of intersection, I added vertical shorter
    line segments (if needed) to ensure there were no more intersections.
    """
    if num_intersections > ((num_segments * num_segments) / 4):
        return None

    segments = []
    num_horizontal = math.ceil(num_segments / 2)
    num_vertical = num_segments - num_horizontal

    #horizontal line segment creation
    y_coordinate = 0
    for index in range(0, num_horizontal):
        segments.append((0, y_coordinate))
        segments.append((2 * (0 + num_vertical), y_coordinate))
        y_coordinate += 2

    #vertical line segment creation
    x_coordinate = 0
    for index in range(0, num_vertical):
        y_coordinate = -2

        if num_intersections > 0:
            segments.append((x_coordinate, y_coordinate))
            while y_coordinate < (num_horizontal * 2 - 2) and num_intersections > 0:
                y_coordinate += 2
                num_intersections -= 1

            segments.append((x_coordinate, y_coordinate))

        else:
            segments.append((x_coordinate, y_coordinate))
            segments.append((x_coordinate, y_coordinate + 1))

        x_coordinate += 2

    return segments

def report_intersections(segments: List[Tuple[int,int]]) -> List[Tuple[int,int]]:
    """
    Compute a list of the I intersections between horizontal
    and vertical line segments in time O(n lg n + I).

        Keyword arguments:
        segments -- a list of horizontal and vertical line segments
                    which are stored as tuples of integers (pairs)
                    of their endpoints. Line segment i is stored as
                    endpoints segments[2i] and segments[2i+1].

    Return a list of integer tuples (pairs), which are the intersection
    points between all line segments in segments.
    """
    if not valid_segment_list(segments):
        return None

    event_queue = []
    status = SortedList([])
    intersections = []

    index = 0

    while index < len(segments):
        x_coordinate1, y_coordinate1 = segments[index]
        x_coordinate2, y_coordinate2 = segments[index + 1]

        identifying_value = ""

        #horizonal line segment
        if y_coordinate1 == y_coordinate2:
            identifying_value = "y(" + str(x_coordinate1) + ", " + \
            str(x_coordinate2) + ")"
            #only one event is added for each horizonal line
            event_queue.append((x_coordinate1, y_coordinate1, identifying_value))

        #vertical line segment
        else:
            identifying_value = "x"
            event_queue.append((x_coordinate1, y_coordinate1, identifying_value))
            event_queue.append((x_coordinate2, y_coordinate2, identifying_value))

        index = index + 2

    event_queue.sort(key = lambda y: (-y[1], y[0]))

    index1 = 0
    while(index1 < len(event_queue)):
        current_event = event_queue[index1]
        index1 += 1
        x_coordinate, y_coordinate, identifier = current_event

        #it is a horizontal line segment
        if identifier[0] == "y":
            """checking if vertical segments with x upper-endpoints with the
            same y coordinate have not been added to the status yet. If there
            are any, they are added to the status."""
            while index1 < len(event_queue):
                x_coordinate2 , y_coordinate2, _ = event_queue[index1]

                if y_coordinate2 == y_coordinate and x_coordinate2 not in status:
                    index1 += 1
                    status.add(x_coordinate2)

                else:
                    break

            #identifiers for horizonal segments are in form y(start_x, stop_x)
            x_coordinate1 = int(identifier[identifier.find(", ") + 2:-1])

            start = status.bisect_left(x_coordinate)
            stop = status.bisect_left(x_coordinate1)

            for index in status[start:stop]:
                intersections.append((index, y_coordinate))

        #it is a vertical segment
        else:
            if x_coordinate not in status:
                status.add(x_coordinate)

            else:
                #it is a lower end point so we should remove from status
                del status[status.bisect_left(x_coordinate)]

    intersections.sort(key = lambda y: (-y[1], y[0]))
    return intersections

def test() -> None:
    """
    For C-4: Give code used for testing here and briefly describe
             in comments how you tested your code.
    First, I tested my code maually by creating line segments on Desmos and then
    entering them into my program. I would visually check on Desmos what I
    thought the solution would be and compare it to my program's output. Later,
    I added the generate_segments funtion and tried to automate the testing by
    outputting errors if the generate_segments function and my
    report_intersections funtion had different numbers of intersections. I ran a
    loop and used random numbers to make sure I was testing different lists of
    segments each time. I also tried to test edge cased to make sure my code
    worked properly."""
    print(report_intersections([(0,0), (5,0), (0, -2), (5, -2), (4, -4), (4,3)]))
    points = generate_segments(12,13) #num_segments, num_intersections
    print(points)
    print("len")
    print(len(points))
    print(report_intersections(points))
    print(report_intersections('hi'))
    print(report_intersections([(1,2,3), (1,2)]))
    print(report_intersections([(0,0)]))

    for _ in range(5000):
        num_intersections = random.randint(0, 50)

        while True:
            num_segments = random.randint(1, 80)
            if num_intersections <= (num_segments * num_segments / 4):
                break

        segments = generate_segments(num_segments, num_intersections)
        intersection = report_intersections(segments)

        if len(intersection) != num_intersections:
            print("Error!")
            print("report_intersections found")
            print(len(intersection))
            print("There should be")
            print(num_intersections)
