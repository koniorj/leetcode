# There is an undirected weighted connected graph. You are given a positive integer n which denotes 
# that the graph has n nodes labeled from 1 to n, and an array edges where each edges[i] = [ui, vi, weighti]
# denotes that there is an edge between nodes ui and vi with weight equal to weighti.

# A path from node start to node end is a sequence of nodes [z0, z1, z2, ..., zk] such that z0 = start 
# and zk = end and there is an edge between zi and zi+1 where 0 <= i <= k-1.

# The distance of a path is the sum of the weights on the edges of the path. Let distanceToLastNode(x) 
# denote the shortest distance of a path between node n and node x. A restricted path is a path that 
# also satisfies that distanceToLastNode(zi) > distanceToLastNode(zi+1) where 0 <= i <= k-1.

# Return the number of restricted paths from node 1 to node n. Since that number may be too large, 
# return it modulo 10^9 + 7.

# dijkstra z wierzcholka n do kazdego innego. Szukamy najkrotszej sciezki, potem
def countRestrictedPaths(n, edges):
    dist = [float('inf')] * n # przesunieta numeracja
    dist[n-1] = 0
    adj_list = [[] for _ in range(n)]
    mod = 10**9 + 7

    for u,v,w in edges:
        adj_list[u-1].append((w,v-1))
        adj_list[v-1].append((w,u-1))

    from queue import PriorityQueue
    pq = PriorityQueue()
    pq.put((0, n-1)) # waga, node

    while not pq.empty():
        w, u = pq.get() 
        if w > dist[u]:
            continue
        for wv, v in adj_list[u]:
            if dist[v] > wv+w:
                dist[v] = wv+w
                pq.put((w+wv, v))

    # wiec mamy juz liste dystansow. Teraz DFS-em sprawdzimy te warunki distance to last node
    dp = [-1] * n # niepoliczone
    def dfs(u):
        if u == n-1:
            return 1 # no bo on sam do siebie ma taki dystans
        if dp[u] != -1:
            return dp[u]
        cnt = 0
        for wv, v in adj_list[u]:
            if dist[u] > dist[v]:
                cnt = (cnt + dfs(v)) 
        dp[u] = cnt
        return cnt % mod
    
    return dfs(0)
                

def countRestrictedPaths(n, edges):
    dist = [float('inf')] * n # przesunieta numeracja
    dist[n-1] = 0
    adj_list = [[] for _ in range(n)]
    mod = 10**9 + 7

    for u,v,w in edges:
        adj_list[u-1].append((w,v-1))
        adj_list[v-1].append((w,u-1))

    from queue import PriorityQueue
    pq = PriorityQueue()
    pq.put((0, n-1))

    while not pq.empty():
        d, node = pq.get()
        if d > dist[node]:
            continue
        for dv, v in adj_list[node]:
            if d+dv < dist[v]:
                dist[v] = d+dv
                pq.put((d+dv, v))

    ans = [0] * n
    ans[n-1] = 1    
    nodes_sort = sorted(range(n), key=lambda x: dist[x])
    # print(nodes_sort)
    # teraz wszystkie sciezki sa restricted z definicji

    for u in nodes_sort:
        for dv, v in adj_list[u]:
            if dist[v] > dist[u]:
                ans[v] = (ans[v] + ans[u]) % mod
                
    return ans[0]

n = 5
edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
print(countRestrictedPaths(n, edges))