# There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th 
# item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are 
# zero indexed. A group can have no item belonging to it.

# Return a sorted list of the items such that:

# The items that belong to the same group are next to each other in the sorted list.
# There are some relations between these items where beforeItems[i] is a list containing all the items that 
# should come before the i-th item in the sorted array (to the left of the i-th item).
# Return any solution if there is more than one solution and return an empty list if there is no 

from collections import deque, defaultdict
def sortItems(n, m, group, beforeItems): # m to ilosc grup
    edges = [[] for _ in range(n)]
    indegree = [0] * n

    new_group = m
    for i in range(n):
        if group[i] == -1:
            group[i] = new_group
            new_group += 1

    total_groups = new_group
    # osobno potrzebujemy zrobic edges i indegree dla grup

    group_edges = [[] for _ in range(total_groups)]
    group_indegree = [0] * total_groups

    for v, u_list in enumerate(beforeItems):
        for u in u_list:
            edges[u].append(v) # teraz tworzymy poprawna kolejnosc do toposorta
            indegree[v] += 1 # trzeba wykonac u przed v

            if group[v] != group[u]: # sa w roznych grupach
                group_edges[group[u]].append(group[v])
                group_indegree[group[v]] += 1

    # toposortem bedziemy rozwiazywac problem kolejnosci. Kahn's algorithm. Musimy tylko wziac pod uwage fakt,
    # ze wierzcholki musza byc ze soba grupowane ze wzgledu na przynaleznosc.

    # potrzebujemy posortowac wszystkie wierzcholki a potem wziac pod uwage grupy
    def kahns(edges, indegree, nodes):
        dq = deque([node for node in nodes if indegree[node] == 0])
        ans = []
        while dq:
            u = dq.popleft()
            ans.append(u)
            for v in edges[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    dq.append(v)
        return ans if len(ans) == len(nodes) else []
        
    nodes = list(range(total_groups))
    group_order = kahns(group_edges, group_indegree[:], nodes)
    if not group_order:
        return []

    all_nodes = list(range(n))
    node_order = kahns(edges, indegree[:], all_nodes)
    if not node_order:
        return []
    
    # mamy osobno group order i item order, teraz wystarczy zrzutowac jedno na drugie w wyniku
    group_to_items = defaultdict(list)
    for node in node_order:
        group_to_items[group[node]].append(node)

    ans = []
    for g in group_order:
        ans.extend(group_to_items[g])

    return ans

n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
print(sortItems(n,m,group,beforeItems))