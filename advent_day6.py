# Advent of Code 2023 day 6
import math


def boat_dist(press_time, race_time):
    """How far does a boat go in the race_time allowed if button pressed for press_time ms?"""
    return press_time * (race_time - press_time)


def beat_dist(race_time, distance):
    """This works but is naive - should do a binary search instead of exhaustive"""
    x = sum(
        [
            1 * (boat_dist(presstime, race_time) > distance)
            for presstime in range(0, race_time)
        ]
    )
    return x


def pt1():
    with open("advent.txt", "rt") as fin:
        raw = [row.strip().split(":") for row in fin]
    times = [int(i) for i in raw[0][1].split()]
    dists = [int(i) for i in raw[1][1].split()]

    options = [beat_dist(t, d) for t, d in zip(times, dists)]
    print("Part 1: ", math.prod(options))


def pt2():
    with open("advent.txt", "rt") as fin:
        raw = [row.strip().split(":") for row in fin]
    race_time = int("".join(raw[0][1].split()))
    current_record = int("".join(raw[1][1].split()))

    low_optima = binary_search(0, race_time, race_time / 10, race_time, current_record)
    print(
        f"Part 2: short-press answer: {low_optima} long-press answer: {race_time-low_optima}"
    )
    print(f"Number of options: {race_time-2*low_optima+1}")


def binary_search(min_x, max_x, current_x, race_time, current_record):
    """Recursive binary search within given constraints
    Just need to find the minimum point where the boat_distance crosses the current_record
    """
    d1 = boat_dist(current_x, race_time)
    d2 = boat_dist(current_x + 1, race_time)
    # print(f"{d1}  {d2}  Current: {current_x} ")
    if d1 <= current_record and d2 > current_record:
        return current_x + 1
    else:
        if d1 < current_record:
            next_x = int((max_x - current_x) / 2 + current_x)
            return binary_search(current_x, max_x, next_x, race_time, current_record)
        else:
            next_x = int((current_x - min_x) / 2 + min_x)
            return binary_search(min_x, current_x, next_x, race_time, current_record)


# final answer: 29891250
if __name__ == "__main__":
    pt1()
    pt2()
