def getAncestors(n, edges):
    ancestors = [set() for _ in range(n)]
    # visited = [False] * n mamy powiedziane ze jest acykliczny
    adj_list = [[] for _ in range(n)]
    indegree = [0] * n

    for u, v in edges:
        adj_list[u].append(v)
        indegree[v] += 1

    from collections import deque
    dq = deque()
    for i in range(n):
        if indegree[i] == 0:
            dq.append(i)
            # visited[i] = True niby acykliczny

    while dq:
        u = dq.popleft()
        # wiemy o u ze ma indegree=0, czyli juz mamy zbudowane jego ancestors
        for nb in adj_list[u]:
            ancestors[nb].update(ancestors[u])
            ancestors[nb].add(u) # u na pewno jest przodkiem kazdego swojego sasiada
            indegree[nb] -= 1
            if indegree[nb] == 0:
                dq.append(nb)

    return [sorted(list(ancestors[i])) for i in range(n)]

n = 8
edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
print(getAncestors(n, edgeList))