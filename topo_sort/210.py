# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must 
# take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

# Return the ordering of courses you should take to finish all courses. If there are many valid answers,
# return any of them. If it is impossible to finish all courses, return an empty array.

from collections import deque

def findOrder(numCourses, prerequisites):
    n = numCourses
    order = []
    adj = [[] for _ in range(n)]
    indegree = [0] * n

    for u, v in prerequisites:
        adj[v].append(u)  
        indegree[u] += 1

    dq = deque()
    for i in range(n):
        if indegree[i] == 0:
            dq.append(i)

    while dq:
        v = dq.popleft()
        order.append(v)

        for nb in adj[v]:
            indegree[nb] -= 1
            if indegree[nb] == 0:
                dq.append(nb)

    return order if len(order) == n else []

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
print(findOrder(numCourses, prerequisites))

