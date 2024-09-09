"""
Search Algorithms and Problem Solving Assignment

This assignment delves into search strategies in AI, their implementation in Python, and
the application of these techniques in problem-solving.

Focus areas:
a. Overview of Search Strategies in AI
b. Implementation of Search Algorithms in Python
c. Problem-Solving Applications using Search Techniques
"""
import heapq
from collections import deque

def depth_first_search(graph, start, goal):
    """
    Implement the Depth-First Search (DFS) algorithm to find a path from start to goal.

    Parameters:
    graph (dict): A dictionary representing the graph, where keys are node names and values are lists of neighbors.
    start (str): The starting node name.
    goal (str): The goal node name.

    Returns:
    path (list): The path from start to goal as a list of node names. Return None if no path is found.
    """
    # Your code here
    stack = [(start, [start])]
    
    while stack:
        # Pop the top element from the stack (current node, current path)
        vertex, path = stack.pop()
        
        # Great success!
        if vertex == goal:
            return path
        
        # Explore all neighbors that are not in the current path (to avoid cycles)
        for neighbor in graph[vertex]:
            if neighbor not in path:
                # Push neighbor with the updated path onto the stack
                stack.append((neighbor, path + [neighbor]))
    
    # Return None if no path is found
    return None


def breadth_first_search(graph, start, goal):
    """
    Implement the Breadth-First Search (BFS) algorithm to find the shortest path from start to goal.

    Parameters:
    graph (dict): A dictionary representing the graph, where keys are node names and values are lists of neighbors.
    start (str): The starting node name.
    goal (str): The goal node name.

    Returns:
    path (list): The shortest path from start to goal as a list of node names. Return None if no path is found.
    """
    # Your code here
    # Queue to store (current node, path to current node)
    queue = deque([(start, [start])])
    
    # While the queue is not empty
    while queue:
        # Dequeue the front element (current node, current path)
        vertex, path = queue.popleft()
        
        # Great success!
        if vertex == goal:
            return path
        
        # Explore all neighbors that are not in the current path (to avoid cycles)
        for neighbor in graph[vertex]:
            if neighbor not in path:
                # Enqueue neighbor with the updated path
                queue.append((neighbor, path + [neighbor]))
    
    # Return None if no path is found
    return None


def a_star_search(graph, start, goal, h):
    """
    Implement the A* search algorithm to find the most efficient path from start to goal, given a heuristic function.

    Parameters:
    graph (dict): A dictionary representing the graph, where keys are node names and values are lists of neighbors
                  and the costs to move to those neighbors.
    start (str): The starting node name.
    goal (str): The goal node name.
    h (dict): A dictionary of heuristic estimates from each node to the goal.

    Returns:
    path (list): The most efficient path from start to goal as a list of node names, considering the heuristic function.
                 Return None if no path is found.
    """
    # Your code here

    open_set = [(h[start], start, [start])]
    
    # Tracking the cost of getting to a node
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    closed_list = []
    
    while open_set:
        # Using heaps to pop the smallest f value....Geeks For Geeks helped me on this (https://www.geeksforgeeks.org/a-search-algorithm/)
        _, current_node, path = heapq.heappop(open_set)
        
        # Great success!
        if current_node == goal:
            return path
        
        # Add to the closed list so we do not revisit
        closed_list.append(current_node)
        
        # Explore the neighborhood to find a node that has not been visited
        for neighbor in graph[current_node]:
            if neighbor in closed_list:
                continue
            
            temp_g_score = g_score[current_node] 
            
            if temp_g_score < g_score[neighbor]:
                g_score[neighbor] = temp_g_score
                f_score = temp_g_score + h[neighbor]
                heapq.heappush(open_set, (f_score, neighbor, path + [neighbor]))
    
    return None

