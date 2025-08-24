# takim niby toposortem sprawdzac czy kolor a musi byc przed kolorem b
# nastepnie wykrywanie cyklu dfs-em
# 60 kolorow max

from collections import defaultdict

def isPrintable(targetGrid):
    graph = defaultdict(set)
    n, m = len(targetGrid), len(targetGrid[0])
    visited = [0] * 61

    # dla kazdego koloru bedziemy zmniejszac prostokat. W znalezionym prostokacie szukac innego

    for c in range(1, 61):
        l, r, t, b = m, -1, n, -1 # na odwrot oznaczenia zeby znalezc latwo min i max
        for i in range(n):
            for j in range(m):
                if targetGrid[i][j] == c:
                    l = min(j, l)
                    r = max(j, r)
                    t = min(i, t)
                    b = max(i, b)
                    # znalezlismy wlasnie bounding box dla takiego koloru
        # teraz szukamy w tym boxie innego koloru :)
        for i in range(t, b+1):
            for j in range(l, r+1):
                if targetGrid[i][j] != c:
                    graph[targetGrid[i][j]].add(c) # c bylo przed obecnym

    # w tym momencie mamy utworzony graf zaleznosci. Teraz probujemy wykryc cykl w grafie. Jesli bez cyklu - ok
    def dfs(i, graph):
        if visited[i] == -1:
            return False # jest cyklu
        if visited[i] == 1:
            return True # brak cyklu
        # inaczej nie byl uzyty. Wiec przypisujemy sami
        visited[i] = -1
        for j in graph[i]: # dla kazdego poprzedniego koloru
            if not dfs(j, graph): # jesli nie bylo tam cyklu
                return False
        visited[i] = 1
        return True               

    # pozostalo nam sprawdzic czy zaden kolor nie tworzy cyklu.
    for c in range(1, 61):
        if not dfs(c, graph):
            return False    
    return True
