class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        safe_nodes = []
        visited = [-1] * n # -1 -> not visited
        # 0 -> visiting
        # 1 -> visited
        safe = [None] * n

        # cycle detection, kind of
        def dfs(v):
            if safe[v] is not None:
                return safe[v]
            elif len(graph[v]) == 0:
                return True

            if visited[v] == 0:
                return False # it's not a safe node, cycle detected
            elif visited[v] == 1:
                return safe[v]

            visited[v] = 0
            for u in graph[v]:
                if not dfs(u):
                    safe[v] = False
                    return False

            visited[v] = 1
            safe[v] = True
            return True

        for i in range(n):
            if dfs(i):
                safe_nodes.append(i)

        return safe_nodes