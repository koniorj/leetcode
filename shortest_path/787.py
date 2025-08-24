# There are n cities connected by some number of flights. You are given an array flights where 
# flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

# You are also given three integers src, dst, and k, return the cheapest price
# from src to dst with at most k stops. If there is no such route, return -1.

def findCheapestPrice(n, flights, src, dst, k):
    adj_list = [[] for _ in range(n)]
    dist = [float('inf')] * n
    dist[src] = 0

    for u, v, w in flights:
        adj_list[u].append((w, v))

    from queue import PriorityQueue
    pq = PriorityQueue()
    pq.put((0, src, 0)) # node, stops, dist

    while not pq.empty():
        stops, v, dv = pq.get()

        if stops > k:
            continue
   
        for du, u in adj_list[v]:
            if du + dv < dist[u] and stops <= k:
                dist[u] = du + dv
                pq.put((stops+1, u, du+dv))

    return dist[dst] if dist[dst] != float('inf') else -1

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
print(findCheapestPrice(n, flights, src, dst, k))