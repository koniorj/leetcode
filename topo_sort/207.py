# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must 
# take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# we're checking if our courses create a DAG or not.
def canFinish(numCourses, prerequisites):
    edges = [[] for _ in range(numCourses)]
    for (u, v) in prerequisites:
        edges[u].append(v)

    visited = [0] * (numCourses) # 0: unvisited, 1: visiting, 2: visited

    def check_cycle(v):
        if visited[v] == 2:
            return False
        if visited[v] == 1:
            return True # cycle detected
        visited[v] = 1
        for u in edges[v]:
            if check_cycle(u):
                return True
        visited[v] = 2
        return False

    for v in range(numCourses):
        if visited[v] == 0:
            if check_cycle(v):
                return False
    return True

numCourses = 2
prerequisites = [[1,0]] #true
print(canFinish(numCourses, prerequisites))
numCourses = 2
prerequisites = [[1,0],[0,1]] #false
print(canFinish(numCourses, prerequisites))

# V2: return a list of courses