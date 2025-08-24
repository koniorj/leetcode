import heapq
def minCostConnectPoints(points):
    def distance(first, second):
        return abs(points[first][0] - points[second][0]) + abs(points[first][1] - points[second][1])

    def prim(graph):
        n = len(graph)
        cost = 0
        visited = [False] * n
        hq = [(0,0)]

        while hq:
            w, v = heapq.heappop(hq)
            if visited[v]:
                continue

            visited[v] = True
            cost += w

            for nb in range(n):
                if not visited[nb]:
                    dist = distance(v, nb)
                    heapq.heappush(hq, (dist, nb))

        return cost

    return prim(points)

points = [[0,0],[2,2],[3,10],[5,2],[7,0]] # 20
print(minCostConnectPoints(points))

points = [[3,12],[-2,5],[-4,1]] # 18
print(minCostConnectPoints(points))