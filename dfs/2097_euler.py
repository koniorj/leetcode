# You are given a 0-indexed 2D integer array pairs where pairs[i] = [starti, endi]. 
# An arrangement of pairs is valid if for every index i where 1 <= i < pairs.length, we have endi-1 == starti.

# Return any valid arrangement of pairs.

# Note: The inputs will be generated such that there exists a valid arrangement of pairs.

def validArrangement(pairs):
    from collections import defaultdict, deque
    adj = defaultdict(list)
    in_out_deg = defaultdict(int)

    for u,v in pairs:
        adj[u].append(v)
        in_out_deg[v] += 1 # outdeg
        in_out_deg[u] -= 1 # indeg

    start = pairs[0][0] # jak nie znajdziemy roznicy to bierzemy losowy
    for node, deg in in_out_deg.items():
        if deg == -1:
            start = node
            break

    ans = []
    stack = deque([start])
    while stack:
        u = stack[-1]
        if adj[u]:
            stack.append(adj[u].pop())
        else:
            ans.append(stack.pop())

    res = []
    m = len(ans)
    ans.reverse()
    for i in range(1, m):
        res.append([ans[i-1], ans[i]])
        
    return res

pairs = [[5,1],[4,5],[11,9],[9,4]]
# [[11,9],[9,4],[4,5],[5,1]]
print(validArrangement(pairs))