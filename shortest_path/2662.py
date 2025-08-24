# You are given an array start where start = [startX, startY] represents your initial 
# position (startX, startY) in a 2D space. You are also given the array target where 
# target = [targetX, targetY] represents your target position (targetX, targetY).

# The cost of going from a position (x1, y1) to any other position in the space (x2, y2) is |x2 - x1| + |y2 - y1|.

# There are also some special roads. You are given a 2D array specialRoads where 
# specialRoads[i] = [x1i, y1i, x2i, y2i, costi] indicates that the ith special 
# road goes in one direction from (x1i, y1i) to (x2i, y2i) with a cost equal to costi. 
# You can use each special road any number of times.

# Return the minimum cost required to go from (startX, startY) to (targetX, targetY).

def minimumCost(start, target, specialRoads):
    dist = lambda x,y: abs(x[0]-y[0])+abs(x[1]-y[1])
    specialRoads = tuple((cost,(x1,y1),(x2,y2)) for x1,y1,x2,y2,cost in specialRoads if dist((x1,y1),(x2,y2)) > cost)

    visited = set()
    check = dist(start, target)

    from heapq import heappop, heappush
    hq = [(0, (start[0], start[1]))] # dist, pos

    while hq:
        cost, pos = heappop(hq)

        if pos in visited or cost > check:
            continue

        check = min(check, cost+dist(pos, target))
        visited.add(pos)

        for pay, begin, end in specialRoads:
            heappush(hq, (cost+pay+dist(pos, begin), end))

    return check

start = [3,2]
target = [5,7]
specialRoads = [[5,7,3,2,1],[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]
print(minimumCost(start, target, specialRoads))

