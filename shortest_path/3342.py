# There is a dungeon with n x m rooms arranged as a grid.

# You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time
# in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and
# can move to an adjacent room. Moving between adjacent rooms takes one second for one move and two 
# seconds for the next, alternating between the two.

# Return the minimum time to reach the room (n - 1, m - 1).
# Two rooms are adjacent if they share a common wall, either horizontally or vertically.

def minTimeToReach(moveTime):
    m = len(moveTime)
    n = len(moveTime[0])

    dist = [[[float('inf'), float('inf')] for _ in range(n)] for _ in range(m)]
    dist[0][0][0] = 0
    dist[0][0][1] = 0
    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    # print(dist)

    from heapq import heappop, heappush
    q = []
    heappush(q, (0, 0, 0, 0)) # czas, x, y, wait
    # wait 0 to 1 sekunda
    # wait 1 to 2 sekundy

    while q:
        d, x, y, wait = heappop(q)

        if d > dist[x][y][wait]:
            continue

        if x == n-1 and y == m-1:
            return d
        
        step = 1 if wait == 0 else 2
        nwait = 1 - wait
        
        for dx, dy in moves:
            nx, ny = dx+x, dy+y
            if 0 <= nx < m and 0 <= ny < n:
                time = max(moveTime[nx][ny], d) + step 
                if time < dist[nx][ny][nwait]:
                    dist[nx][ny][nwait] = time
                    heappush(q, (time, nx, ny, nwait))
                
    return min(dist[-1][-1])

moveTime = [[0,4],[4,4]]
print(minTimeToReach(moveTime))