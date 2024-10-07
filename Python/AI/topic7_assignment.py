"""
Robotics and Perception Assignment

This assignment covers introductory topics in Robotics within the field of AI, focusing on sensory processing,
computer vision, and motion planning and pathfinding algorithms.

Prior to starting, make sure to have the following libraries installed:
- OpenCV (cv2)
- numpy
- matplotlib

You can install them using pip:
pip install opencv-python numpy matplotlib
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import heapq

def image_processing(image_path):
    """
    Load an image and apply basic processing techniques such as grayscale conversion,
    thresholding, and edge detection.

    Parameters:
    image_path (str): The file path to an image.

    Returns:
    processed_images (dict): A dictionary with keys 'grayscale', 'thresholded', and 'edges' corresponding
                             to the processed images.
    """
    # Your code here
    processed_images = {}
    try:
        # Check if the file exists
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image at path {image_path} not found.")
        
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Failed to load image from {image_path}.")
        
        # Convert to grayscale
        grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        processed_images['grayscale'] = grayscale
        
        # Only need the thresholded image here
        thresholded = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)[1]
        processed_images['thresholded'] = thresholded
        
        # Detect edges
        edges = cv2.Canny(grayscale, 100, 200)
        processed_images['edges'] = edges

        return processed_images

    except FileNotFoundError as fnf_error:
        print(fnf_error)
        return None
    except ValueError as val_error:
        print(val_error)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def sensory_processing(sensor_data):
    """
    Process raw sensor data to detect obstacles in the environment.

    Parameters:
    sensor_data (list of float): Simulated distance sensor readings in an environment with obstacles.

    Returns:
    obstacles (list of int): Indices of the sensor readings that are classified as obstacles.
    """
    # Your code here
    obstacle_threshold = 1.5 
    
    try:
        return [index for index, distance in enumerate(sensor_data) if distance < obstacle_threshold]        
    
    except TypeError as e:
        print(f"Invalid input data: {e}")
        return None
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def pathfinding(grid, start, goal):
    """
    Implement a pathfinding algorithm (such as A* or Dijkstra's) to find a path from start to goal in a grid.

    Parameters:
    grid (numpy.ndarray): 2D array representing the grid where 0s are passable tiles and 1s are obstacles.
    start (tuple): Starting grid position as a tuple (row, column).
    goal (tuple): Goal grid position as a tuple (row, column).

    Returns:
    path (list): The path from start to goal as a list of tuples (row, column). Return an empty list if no path is found.
    """
    # Your code here
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    try:
        # Making sure that the start and goal are valid
        if not (0 <= start[0] < len(grid) and 0 <= start[1] < len(grid[0])):
            raise ValueError("Start point is out of grid bounds.")
        if not (0 <= goal[0] < len(grid) and 0 <= goal[1] < len(grid[0])):
            raise ValueError("Goal point is out of grid bounds.")
        if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
            raise ValueError("Start or goal point is an obstacle.")
        
        # Priority queue
        frontier = []
        heapq.heappush(frontier, (0, start))
        
        came_from = {start: None}
        cost_so_far = {start: 0}
        
        # Movement directions order is up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while frontier:
            # Only need current here so not assigning priority
            current = heapq.heappop(frontier)[1]
            
            # Great success!
            if current == goal:
                break
            
            # Explore neighbors
            for direction in directions:
                next_point = (current[0] + direction[0], current[1] + direction[1])
                
                # Ensure the next point is within the grid and not an obstacle
                if 0 <= next_point[0] < len(grid) and 0 <= next_point[1] < len(grid[0]) and grid[next_point[0]][next_point[1]] != 1:
                    
                    new_cost = cost_so_far[current] + 1
                    
                    # If the next point has not been visited or we found a cheaper path
                    if next_point not in cost_so_far or new_cost < cost_so_far[next_point]:
                        cost_so_far[next_point] = new_cost
                        priority = new_cost + heuristic(goal, next_point)
                        heapq.heappush(frontier, (priority, next_point))
                        came_from[next_point] = current
        
        # Reconstruct the path from goal to start
        path = []
        if goal in came_from:
            current = goal
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
        
        # Test expects an empty list if no path is found
        return path if path else []

    except ValueError as ve:
        print(f"Error: {ve}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []