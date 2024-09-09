from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    def bfs(self, start_vertex):
        visited = [False] * self.vertices
        queue = deque([start_vertex])
        visited[start_vertex] = True
        result = []

        while queue:
            vertex = queue.popleft()
            result.append(vertex)

            for neighbor in self.graph[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

        return result

    def dfs(self, start_vertex):
        def dfs_util(v, visited, result):
            visited[v] = True
            result.append(v)

            for neighbor in self.graph[v]:
                if not visited[neighbor]:
                    dfs_util(neighbor, visited, result)

        visited = [False] * self.vertices
        result = []
        dfs_util(start_vertex, visited, result)
        return result

def shortest_path(graph, start_vertex, end_vertex):
    visited = [False] * len(graph.graph)
    queue = deque([(start_vertex, [start_vertex])])
    visited[start_vertex] = True

    while queue:
        (current_vertex, path) = queue.popleft()

        for neighbor in graph.graph[current_vertex]:
            if neighbor == end_vertex:
                return path + [end_vertex]
            if not visited[neighbor]:
                queue.append((neighbor, path + [neighbor]))
                visited[neighbor] = True

    return []
