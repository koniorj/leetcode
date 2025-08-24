class Solution:
    def findMinHeightTrees(self, n: int, edges):
        if n == 1:
            return [0]
        
        adj = {}
        for u, v in edges:
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            adj[u].append(v)
            adj[v].append(u)

        visited = [0] * n
        from collections import deque
        dq = deque()
        for i in range(n):
            if len(adj.get(i, [])) == 1:
                dq.append(i)
                visited[i] += 1

        prev = None
        while dq:
            prev = [*dq] # jak list()
            size = len(dq)

            for _ in range(size):
                node = dq.popleft()
                for nb in adj.get(node, []):
                    if visited[nb] < len(adj[nb]):
                        visited[nb] += 1

                        if visited[nb] == len(adj[nb]) - 1:
                            dq.append(nb)

        return prev
   