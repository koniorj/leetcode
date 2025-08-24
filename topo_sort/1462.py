# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given 
# an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first
#  if you want to take course bi.

# For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
# Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a
#  prerequisite of course c, then course a is a prerequisite of course c.

# You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should 
# answer whether course uj is a prerequisite of course vj or not.

# Return a boolean array answer, where answer[j] is the answer to the jth query.

def checkIfPrerequisite(numCourses, prerequisites, queries):
    edges = [[] for _ in range(numCourses)]
    for u, v in prerequisites:
        edges[u].append(v)

    answer = []
    for u, v in queries:
        stack = [u]
        visited = [False] * numCourses
        found = False
        while stack and not found:
            node = stack.pop()
            visited[node] = True
            for nb in edges[node]:
                if nb == v:
                    found = True
                    break
                if not visited[nb]:
                    stack.append(nb)
        answer.append(found)

    return answer

# rozw 2: indegree + kolejka :)

def checkIfPrerequisite(numCourses, prerequisites, queries):
    edges = [[] for _ in range(numCourses)]
    indegree = [0 for _ in range(numCourses)]

    for u, v in prerequisites:
        edges[u].append(v)
        indegree[v] += 1

    from collections import deque
    dq = deque()
    for v in range(numCourses):
        if indegree[v] == 0:
            dq.append(v)

    preqs = [set() for _ in range(numCourses)]
    while dq:
        node = dq.popleft()
        for neighbor in edges[node]:
            preqs[neighbor].add(node)
            preqs[neighbor].update(preqs[node])
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                dq.append(neighbor)

    return [u in preqs[v] for u,v in queries]

numCourses = 2
prerequisites = [[1,0]]
queries = [[0,1],[1,0]] # false, true
print(checkIfPrerequisite(numCourses, prerequisites, queries))