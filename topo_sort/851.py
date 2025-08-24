# There is a group of n people labeled from 0 to n - 1 where each person has a different amount of 
# money and a different level of quietness.

# You are given an array richer where richer[i] = [ai, bi] indicates that ai has more money than 
# bi and an integer array quiet where quiet[i] is the quietness of the ith person. All the given data
#  in richer are logically correct (i.e., the data will not lead you to a situation where x is richer 
# than y and y is richer than x at the same time).

# Return an integer array answer where answer[x] = y if y is the least quiet person 
# (that is, the person y with the smallest value of quiet[y]) among all people who 
# definitely have equal to or more money than the person x

# The "richer" relationship graph is a DAG (Directed Acyclic Graph),
#  meaning it has no cycles. Topological sort ensures we process each
#  person only after all their richer prerequisites are processed.

def loudAndRich(richer, quiet):
    n = len(quiet)
    neighbors = [[] for _ in range(n)]
    answer = [None] * n

    for u, v in richer: # we want to store richer neighbors
        neighbors[v].append(u) # we created directed graph, pointing to richer nbs
    
    def dfs(node):
        if answer[node] is not None:
            return answer[node]
        
        quietest = node
        for nb in neighbors[node]:
            cand = dfs(nb)
            if quiet[cand] < quiet[quietest]:
                quietest = cand

        answer[node] = quietest
        return quietest
    
    for i in range(n):
        if answer[i] is None:
            dfs(i)

    return answer

from collections import deque

def loudAndRich(richer, quiet):
    n = len(quiet)
    neighbors = [[] for _ in range(n)]
    answer = [i for i in range(n)]
    indegree = [0] * n

    for u, v in richer: # we want to store richer neighbors
        neighbors[v].append(u) # we created directed graph, pointing to richer nbs
        indegree[u] += 1

    dq = deque()    
    for i in range(n):
        if indegree[i] == 0:
            dq.append(i)

    while dq:
        node = dq.popleft()
        for nb in neighbors[node]:
            if quiet[answer[node]] < quiet[answer[nb]]:
                answer[nb] = answer[node]
            indegree[nb] -= 1
            if indegree[nb] == 0:
                dq.append(nb)

    return answer
        
richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0] #[5,5,2,5,4,5,6,7]
print(loudAndRich(richer, quiet))

richer = []
quiet = [0] #[0]
print(loudAndRich(richer, quiet))