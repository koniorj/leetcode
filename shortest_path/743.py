def networkDelayTime(times, n, k):
    dist = [float('inf') for _ in range(n)] # od 1 do n numeracja, musimy przesunac
    adj_list = [[] for _ in range(n)]
    dist[k-1] = 0

    for u, v, w in times:
        adj_list[u-1].append((w,v-1))

    from queue import PriorityQueue
    pq = PriorityQueue()
    pq.put((0, k-1))

    while not pq.empty():
        d, v = pq.get()
        if d > dist[v]:
            continue

        for du, u in adj_list[v]:
            if du+d < dist[u]:
                dist[u] = du+d
                pq.put((du+d, u))

    ans = max(dist)
    return ans if ans != float('inf') else -1

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(networkDelayTime(times, n, k))