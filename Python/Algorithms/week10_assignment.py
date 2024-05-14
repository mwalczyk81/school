def ford_fulkerson(graph, s, t):
    """
    Implement the Ford-Fulkerson algorithm to compute the maximum flow in the network 'graph' from source 's' to sink 't'.
    Return the value of the maximum flow.
    """
    def bfs(graph, s, t, parent):
        visited = [False] * len(graph)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for v in range(len(graph)):
                if visited[v] is False and graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
        return True if visited[t] else False

    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(graph, s, t, parent):
        path_flow = float("Inf")
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = u

        max_flow += path_flow

        v = t
        while v != s:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u

    return max_flow