def findTheCity(n, edges, distanceThreshold):
    # szukamy najbardziej samotnego miasta
    # graf nieskierowany
    # wyglada na dijkstre z kazdego wierzcholka ... ale zbyt wolne

    # precompute floydem-warshallem dystanse wszystkiego od wszystkiego
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]

    for i in range(n):
            dist[i][i] = 0

    for u, v, w in edges:
        dist[u][v] = dist[v][u] = w

    for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[k][j]+dist[i][k]

    min_reach = float('inf')
    best_city = -1
    
    for i in range(n):
        reachable = 0
        for j in range(n):
            if dist[i][j] <= distanceThreshold:
                reachable += 1
        
        if reachable <= min_reach:
            min_reach = reachable
            best_city = i
    
    return best_city

n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
print(findTheCity(n, edges, distanceThreshold))