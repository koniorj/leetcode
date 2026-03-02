# There is a country of n cities numbered from 0 to n - 1 where all the cities are connected by bi-directional roads. 
# The roads are represented as a 2D integer array edges where edges[i] = [xi, yi, timei] denotes 
# a road between cities xi and yi that takes timei minutes to travel. There may be multiple roads 
# of differing travel times connecting the same two cities, but no road connects a city to itself.

# Each time you pass through a city, you must pay a passing fee. This is represented as a 0-indexed 
# integer array passingFees of length n where passingFees[j] is the amount of dollars you must pay
#  when you pass through city j.

# In the beginning, you are at city 0 and want to reach city n - 1 in maxTime minutes or less. 
# The cost of your journey is the summation of passing fees for each city that you passed 
# through at some moment of your journey (including the source and destination cities).

# Given maxTime, edges, and passingFees, return the minimum cost to complete your journey, 
# or -1 if you cannot complete it within maxTime minutes.

def minCost(maxTime, edges, passingFees):
    n = len(passingFees)
    adj = [[] for _ in range(n)]

    for u,v,w in edges:
        adj[u].append((w,v))
        adj[v].append((w,u))

    dp = {(0,0): passingFees[0]} # min cost przy dist, node
    from collections import deque
    dq = deque()
    dq.append((passingFees[0], 0, 0)) # cost, dist, node

    while dq:
        ucost, utime, u = dq.pop()

        for dv, v in adj[u]:
            vcost = ucost + passingFees[v]
            vtime = utime + dv
            if vtime <= maxTime:
                if (vtime, v) not in dp or dp[(vtime,v)] > vcost:
                    dp[(vtime,v)] = vcost
                    dq.append((vcost, vtime, v))

    ans = min((cost for (t, node), cost in dp.items() if node == n-1), default=float('inf'))
    return ans if ans != float('inf') else -1

maxTime = 30
edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]]
passingFees = [5,1,2,20,20,3]
print(minCost(maxTime, edges, passingFees))