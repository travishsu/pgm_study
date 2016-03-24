import networkx as nx

def findAllParents(node):
    L = G.predecessors(node)
    L_repeat = []
    for Y in L:
        L_repeat.extend(findParents(Y))
    for Y in L_repeat:
        if Y not in L:
            L.append(Y)
    return L

def findAllChilds(node):
    L = G.successors(node)
    L_repeat = []
    for Y in L:
        L_repeat.extend(findChilds(Y))
    for Y in L_repeat:
        if Y not in L:
            L.append(Y)
    return L

def union(A, B):
    L = A
    for e in B:
        if e not in A:
            L.append(e)
    return L

def reachable(X, Z):
    L = list(Z)
    A = []
    while not not L:
        Y = L[0]
        L.pop(0)
        if Y not in A:
            L = union(L, G.predecessors(Y))
        A = union(A, [Y])
    L = []
    L.append((X,0))
    V = []
    R = []
    while not not L:
        YandDir = L[0]
        Y = YandDir[0]
        d = YandDir[1]
        L.pop(0)
        if YandDir not in V:
            if Y not in Z:
                R = union(R, [Y])
            V = union(V, [YandDir])
            if d == 0 and Y not in Z:
                for z in G.predecessors(Y):
                    L = union(L, [(z, 0)])
                for z in G.successors(Y):
                    L = union(L, [(z, 1)])
            elif d == 1:
                if Y not in Z:
                    for z in G.successors(Y):
                        L = union(L, [(z, 1)])
                if Y in A:
                    for z in G.predecessors(Y):
                        L = union(L, [(z, 0)])
    return R

def main():
    global G
    G = nx.DiGraph()
    G.add_nodes_from('DIGSL')
    G.add_edges_from([('D', 'G'), ('I', 'G'), ('I', 'S'), ('G', 'L')])
    Z = ['G', 'I']
    X = 'S'
    print reachable(X, Z)
main()
