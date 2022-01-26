import itertools
import numpy.random as rnd
import networkx as nx
import matplotlib.pyplot as plt
import math


def hierarchy_pos(G, root=None, width=1., vert_gap=0.5, vert_loc=0, xcenter=0, lns=4):
    temp = list(G.nodes)
    pos = {root: (xcenter, vert_loc)}
    fact = math.factorial(lns)
    vert_gap = fact*0.1
    q = 1
    cnt = 0
    c = lns*(lns-1)/2
    z = fact/2 - c/2
    for i in range(len(temp)-1):
        children = list(G.neighbors(temp[i]))
        xcenter = pos[temp[i]][0]
        if(i > z):
            q = -1
        for child in children:
            if(temp.index(temp[i]) > temp.index(child)):
                children.remove(child)

        if len(children) != 0:

            dx = width/(len(children)**q)
            nextx = xcenter - width/2 + dx/2
            if(i == 0):
                vert_loc -= vert_gap
            elif (pos[temp[i]][1] != pos[temp[i-1]][1]):
                vert_loc -= vert_gap

            for child in children:
                if(child not in pos.keys()):
                    pos[child] = (nextx, vert_loc)

                nextx += dx
            if (pos[temp[i]][1] != pos[temp[i+1]][1]):
                width = dx
    b = int(z+c)

    for i in range(b, len(temp)):

        pos[temp[i]] = (-pos[temp[int(z)-1-cnt]][0], pos[temp[i]][1])

        cnt += 1

    return pos


def toOneRange(allows, cnt=0):
    lst_have = []

    lens = len(allows)

    temp = 0
    for i in range(lens-1):
        temp = allows[i]
        allows[i] = allows[i+1]
        allows[i+1] = temp
        lst_have.append([0 for i in range(lens)])
        for j in range(lens):
            lst_have[i][j] += allows[j]
        temp = allows[i]
        allows[i] = allows[i+1]
        allows[i+1] = temp

    return lst_have


def toAll(kit_range, final_range_cond, final_range_bord):
    l = len(final_range_bord)

    if (l > 5):
        print("Розмірність занадто велика для візуалізації графа варіантів")
        return
    allows = [i for i in range(l)]
    temp = 0
    graph = nx.Graph()
    lns = len(allows)
    lns *= lns-1
    lns /= 2
    lst_have = [allows]
    j = 1
    r = math.factorial(len(allows))

    while temp < r:

        temp_lst = toOneRange(lst_have[temp])
        for i in range(len(temp_lst)):
            if(temp_lst[i] not in lst_have):
                lst_have.append(temp_lst[i])
                graph.add_edge(str(lst_have[temp]), str(lst_have[j]))
                j += 1
            elif(lst_have.index(temp_lst[i]) > lst_have.index(lst_have[temp])):
                graph.add_edge(str(lst_have[temp]), str(lst_have[lst_have.index(temp_lst[i])]))

        temp += 1

    pos = hierarchy_pos(graph, str(lst_have[0]), width=120., lns=len(allows))
    cor = []
    for i in range(r):
        if(lst_have[i] == final_range_cond and lst_have[i] == final_range_bord):
            cor.append('pink')
        elif(lst_have[i] == final_range_cond):
            cor.append('b')
        elif(lst_have[i] == final_range_bord):
            cor.append('g')
        elif(lst_have[i] in kit_range):
            cor.append('y')
        else:
            cor.append('r')
    nx.draw(graph, pos=pos,
            node_color=cor,

            with_labels=True)
    plt.show()
