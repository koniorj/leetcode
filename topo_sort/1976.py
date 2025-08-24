def countPaths(n, roads):
    mod = 10**9 + 7
    adj_list = [[] for _ in range(n)]

    # znalezc wszystkie sciezki od punktu a do b
    # wyglada jak odpalenie Dijkstry dwa razy. A w sumie to raz starczy

    for u, v, time in roads:
        adj_list[u].append((time, v))
        adj_list[v].append((time, u))

    from queue import PriorityQueue
    dist = [float('inf') for _ in range(n)]
    dist[0] = 0

    pq = PriorityQueue()
    pq.put((0, 0)) # dist, node
    paths = [0] * n
    paths[0] = 1

    while not pq.empty():
        dv, v = pq.get()

        if dv > dist[v]: # zeby nie marnowac czasu
            continue

        for du, u in adj_list[v]:
            if du + dv < dist[u]:
                dist[u] = du + dv
                paths[u] = paths[v] % mod
                pq.put((du+dv, u))
            elif du + dv == dist[u]:
                # pq.put((du+dv, u)) juz tu bylismy jednak wiecej bez sensu
                paths[u] = (paths[u] + paths[v]) % mod

    return paths[n-1] 

n = 7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
print(countPaths(n, roads))