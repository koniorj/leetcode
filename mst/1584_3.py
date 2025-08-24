# Return the minimum cost to make all points connected. All points are connected 
# if there is exactly one simple path between any two points.

from queue import PriorityQueue
def minCostConnectPoints(points):
    def distance(x, y):
        return abs(x[0]-y[0]) + abs(x[1]-y[1])
    
    # points.sort() # rosnaco po x, potem rosnaco po y (juz sa posortowane)
    n = len(points)
    dist = [float('inf')] * n
    dist[0] = 0
    visited = [False] * n
    min_cost = 0
    pq = PriorityQueue()
    pq.put((0, 0)) # dist, v

    while not pq.empty():
        d, v = pq.get()
        if visited[v]:
            continue

        visited[v] = True
        min_cost += d

        for u in range(n):
            if u == v:
                continue
            if not visited[u]:
                du = distance(points[v], points[u])
                if du < dist[u]:
                    dist[u] = du
                    pq.put((du, u))

    return min_cost


points = [[0,0],[2,2],[3,10],[5,2],[7,0]] # 20
print(minCostConnectPoints(points))

points = [[3,12],[-2,5],[-4,1]] # 18
print(minCostConnectPoints(points))
