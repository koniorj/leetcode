# You are given an array points representing integer coordinates of some points on a 2D-plane, 
# where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them:
#  |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected
#  if there is exactly one simple path between any two points.

from queue import PriorityQueue
def minCostConnectPoints(points):
    def dist(p1, p2):
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
    
    n = len(points)
    dp = [float('inf')] * n
    visited = [False] * n
    dp[0] = 0
    cost = 0

    pq = PriorityQueue()
    pq.put((0, 0)) #dist, v
    while not pq.empty():
        dv, v = pq.get()
        if visited[v]:
            continue

        visited[v] = True
        cost += dv

        for nb in range(n):
            if nb != v:
                if not visited[nb]:
                    nd = dist(points[v], points[nb])
                    if dp[nb] > nd:
                        dp[nb] = nd
                        pq.put((nd, nb))

    return cost

points = [[0,0],[2,2],[3,10],[5,2],[7,0]] # 20
print(minCostConnectPoints(points))

points = [[3,12],[-2,5],[-4,1]] # 18
print(minCostConnectPoints(points))