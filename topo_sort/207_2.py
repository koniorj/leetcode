# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you 
# must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

def canFinish(numCourses, prerequisites):
    indegree = [0] * numCourses
    adj = [[] for _ in range(numCourses)]
    for a, b in prerequisites:
        indegree[a] += 1
        adj[b].append(a)

    from collections import deque
    q = deque()
    for i in range(numCourses):
        if indegree[i] == 0:
            q.append(i)

    done = []
    while q:
        u = q.popleft()
        done.append(u)

        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    if len(done) == numCourses:
        return True
    
    return False