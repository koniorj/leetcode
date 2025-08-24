def tarjan(graph):
    n = len(graph)
    visit_order = [-1] * n # kiedy odwiedziliśmy dany wierzchołek
    lowest = [-1] * n # najwcześniejszy odwiedzony wierzchołek osiągalny z tego wierzchołka
    on_stack = [False] * n
    stack = []
    result = []
    index = 0 # rośnie za każdym razem, gdy odwiedzamy nowy wierzchołek

    def dfs(v):
        nonlocal index

        visit_order[v] = lowest[v] = index 
        index += 1

        stack.append(v)
        on_stack[v] = True

        for u in graph[v]:
            if visit_order[u] == -1: # nie bylismy jeszcze
                dfs(u) # wchodzimy teraz
                lowest[v] = min(lowest[u], lowest[v])
            elif on_stack[u]:
                lowest[v] = min(lowest[u], lowest[v])

        if lowest[v] == visit_order[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v:
                    break

            result.append(scc)

    for v in range(n):
        if visit_order[v] == -1:
            dfs(v)

    return result
