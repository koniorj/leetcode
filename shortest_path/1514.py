def maxProbability(n, edges, succProb, start_node, end_node):
    # to jest po prostu szukanie sciezki o najwiekszej lacznej wadze. Znowu Dijkstra.
    # no i floaty, o tym trzeba pamietac

    #BARDZO SLABE COMPLEXITY DIJKSTRA, BELLMAN LEPSZY!! 

    prob = [0.0] * n
    prob[start_node] = 1.0

    m = len(succProb)
    adj_list = [[] for _ in range(n)]
    for i in range(m):
        adj_list[edges[i][0]].append((succProb[i], edges[i][1]))
        adj_list[edges[i][1]].append((succProb[i], edges[i][0]))

    from queue import PriorityQueue
    pq = PriorityQueue()
    pq.put((-1.0, start_node)) # prob, node

    while not pq.empty():
        pv, v = pq.get()
        pv = -pv

        if pv < prob[v]: # juz tu bylismy z lepszym prawd
            continue

        for pu, u in adj_list[v]:
            if pv*pu > prob[u]:
                prob[u] = pv*pu
                pq.put((-prob[u], u))

    return prob[end_node]

# n = 3
# edges = [[0,1],[1,2],[0,2]]
# succProb = [0.5,0.5,0.2]
# start = 0
# end = 2
# print(maxProbability(n, edges, succProb, start, end))

def maxProbability(n, edges, succProb, start_node, end_node):
    dist = [0] * n
    dist[start_node] = 1

    for _ in range(n-1):
        flag = False
        for i, (u, v) in enumerate(edges):
            if dist[u] * succProb[i] > dist[v]:
                dist[v] = dist[u] * succProb[i]
                flag = True
            if dist[v] * succProb[i] > dist[u]:
                dist[u] = dist[v] * succProb[i]
                flag = True
        if not flag:
            break

    return dist[end_node]

n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2
print(maxProbability(n, edges, succProb, start, end))