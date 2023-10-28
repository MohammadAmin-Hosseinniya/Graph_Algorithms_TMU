import math
import time

def tsp_nearest_neighbor(filename):
    # To read input file:
    with open(filename, "r") as file:
        lines = []
        for line in file:
            lines.append(list(map(int, line.strip().split())))
        
    num_points = lines[0][0]
    points = lines[1:]

    # Create a list to store the visited points
    visited = [False] * num_points

    # Start at the first point
    current_point = 0
    visited[current_point] = True

    # Initialize variables for the tour order and length
    tour_order = [current_point]
    tour_length = 0

    # Iterate through all the points
    for _ in range(num_points - 1):
        # Find the nearest neighbor
        nearest_neighbor = None
        min_distance = math.inf

        # The loop below goes on till all of points are visited:
        for i in range(num_points):
            if not visited[i]:
                distance = math.sqrt((points[current_point][0] - points[i][0]) ** 2 + (points[current_point][1] - points[i][1]) ** 2)
                if distance < min_distance:
                    min_distance = distance
                    nearest_neighbor = i

        # Update the current point and mark it as visited
        current_point = nearest_neighbor
        visited[current_point] = True

        # Add the current point to the tour order and update the tour length
        tour_order.append(current_point)
        tour_length += min_distance

    # Add the distance from the last point back to the starting point
    tour_length += math.sqrt((points[current_point][0] - points[0][0]) ** 2 + (points[current_point][1] - points[0][1]) ** 2)

    return tour_order, tour_length

# Usage

input_file = "NN_input_0.txt"

start_time = time.time()
tour_order, tour_length = tsp_nearest_neighbor(input_file)
end_time = time.time()

elapsed_time = end_time - start_time

print("Tour Order:", tour_order)
print("Tour Length:", tour_length)
print("Elapsed Time:", elapsed_time, "seconds")