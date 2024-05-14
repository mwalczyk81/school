from collections import deque
import heapq

def bfs(graph, start):
    """
    Traverse the graph using Breadth First Search starting from the given node.
    Return the order in which the nodes are visited.
    """
    visited = set()
    traversal_order = []
    queue = deque([start])

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            traversal_order.append(current_node)
            visited.add(current_node)
            neighbors = graph[current_node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal_order

def dfs(graph, start):
    """
    Traverse the graph using Depth First Search starting from the given node.
    Return the order in which the nodes are visited.
    """
    visited = set()
    traversal_order = []
    stack = [start]

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            traversal_order.append(current_node)
            visited.add(current_node)
            neighbors = graph[current_node]

            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal_order

def dijkstra(graph, start):
    """
    Compute the shortest path from the start node to all other nodes in the graph using Dijkstra's algorithm.
    Return a list of minimum distances from the start node to every other node.
    """
    num_nodes = len(graph)
    distances = [float('inf')] * num_nodes
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in enumerate(graph[current_node]):
            if weight > 0:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

    return distances
