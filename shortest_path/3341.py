# There is a dungeon with n x m rooms arranged as a grid.

# You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the 
# minimum time in seconds after which the room opens and can be moved to. You start from
# the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent
# rooms takes exactly one second.

# Return the minimum time to reach the room (n - 1, m - 1).

# Two rooms are adjacent if they share a common wall, either horizontally or vertically

def minTimeToReach(moveTime):
    m = len(moveTime)
    n = len(moveTime[0])

    dist = [[float('inf') for _ in range(n)] for _ in range(m)]
    dist[0][0] = 0
    moves = [(1,0), (-1,0), (0,1), (0,-1)]

    visited = [[False] * n for _ in range(m)]
    stack = [(0,0,0)] # time, x, y

    while stack:
        time, x, y = stack.pop()

        if time > dist[x][y]:
            continue

        if not visited[x][y]:
            visited[x][y] = True
            for dx, dy in moves:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n:
                    if not visited[nx][ny]:
                        wait = max(moveTime[nx][ny], time) + 1
                        # case 1: wchodzimy bez czekania
                        # case 2: musimy zaczekac
                        if dist[nx][ny] >= wait:
                            dist[nx][ny] = wait
                            stack.append((wait, nx, ny))
                        
    return dist[-1][-1]

# moveTime = [[0,4],[4,4]]
# print(minTimeToReach(moveTime))
# moveTime = [[0,0,0],[0,0,0]]
# print(minTimeToReach(moveTime))

def minTimeToReach(moveTime):
    m = len(moveTime)
    n = len(moveTime[0])

    dist = [[float('inf') for _ in range(n)] for _ in range(m)]
    dist[0][0] = 0
    moves = [(1,0), (-1,0), (0,1), (0,-1)]

    from queue import PriorityQueue
    pq = PriorityQueue()
    pq.put((0, 0, 0)) # time, node

    while not pq.empty():
        d, x, y = pq.get()

        if d > dist[x][y]:
            continue

        if x == m-1 and y == n-1:
            return d

        for dx, dy in moves:
            if (0 <= dx + x < m) and (0 <= dy + y < n):
                wait = max(moveTime[dx+x][dy+y], d) + 1
                if wait < dist[dx+x][dy+y]:
                    dist[dx+x][dy+y] = wait
                    pq.put((wait, dx+x, dy+y))
                
    return dist[m-1][n-1]

moveTime = [[0,4],[4,4]]
print(minTimeToReach(moveTime))
moveTime = [[0,0,0],[0,0,0]]
print(minTimeToReach(moveTime))

def minTimeToReach(moveTime):
    m = len(moveTime)
    n = len(moveTime[0])

    dist = [[float('inf') for _ in range(n)] for _ in range(m)]
    dist[0][0] = 0
    moves = [(1,0), (-1,0), (0,1), (0,-1)]

    from heapq import heappop, heappush
    pq = []
    heappush(pq, (0, 0, 0)) # time, node

    while pq:
        d, x, y = heappop(pq)

        if d > dist[x][y]:
            continue

        if x == m-1 and y == n-1:
            return d
        
        for dx, dy in moves:
            if (0 <= dx + x < m) and (0 <= dy + y < n):
                wait = max(moveTime[dx+x][dy+y], d) + 1
                if wait < dist[dx+x][dy+y]:
                    dist[dx+x][dy+y] = wait
                    heappush(pq, (wait, dx+x, dy+y))
                
    return dist[m-1][n-1]

moveTime = [[0,4],[4,4]]
print(minTimeToReach(moveTime))
moveTime = [[0,0,0],[0,0,0]]
print(minTimeToReach(moveTime))