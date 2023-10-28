import math
import itertools
import time

def tsp_exhaustive_search(filename):
    # To read input file:
    with open(filename, "r") as file:
        lines = []
        for line in file:
            lines.append(list(map(int, line.strip().split())))
        
    num_points = lines[0][0]
    points = lines[1:]

    # Generate all possible permutations of the points
    permutations = itertools.permutations(range(num_points))

    # Initialize variables for the best tour order and length
    best_tour_order = None
    best_tour_length = math.inf

    # Iterate through all permutations
    for tour_order in permutations:
        # Calculate the tour length for the current permutation
        tour_length = 0
        for i in range(num_points - 1):
            current_point = tour_order[i]
            next_point = tour_order[i + 1]
            distance = math.sqrt((points[current_point][0] - points[next_point][0]) ** 2 + (points[current_point][1] - points[next_point][1]) ** 2)
            tour_length += distance

        # Add the distance from the last point back to the starting point
        first_point = tour_order[0]
        last_point = tour_order[num_points - 1]
        distance = math.sqrt((points[last_point][0] - points[first_point][0]) ** 2 + (points[last_point][1] - points[first_point][1]) ** 2)
        tour_length += distance

        # Update the best tour order and length if the current tour is shorter
        if tour_length < best_tour_length:
            best_tour_order = tour_order
            best_tour_length = tour_length

    return best_tour_order, best_tour_length

# Usage

input_file = "ES_input_0.txt"

start_time = time.time()
tour_order, tour_length = tsp_exhaustive_search(input_file)
end_time = time.time()

elapsed_time = end_time - start_time

print("Tour Order:", tour_order)
print("Tour Length:", tour_length)
print("Elapsed Time:", elapsed_time, "seconds")