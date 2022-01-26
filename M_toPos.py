import networkx as nx
import random
import math

def hierarchy_pos(G, root=None, width=1., vert_gap = 0.5, vert_loc = 0, xcenter = 0,lns=4):
    temp=list(G.nodes)
    pos = {root:(xcenter,vert_loc)}
    fact=math.factorial(lns)
    vert_gap=fact*0.1
    q=1
    cnt=0
    c=lns*(lns-1)/2
    z=fact/2 - c/2
    for i in range(len(temp)-1):
        children = list(G.neighbors(temp[i]))
        xcenter=pos[temp[i]][0]
        if(i>z):
            q=-1
        for child in children:
            if(temp.index(temp[i])>temp.index(child)):
                children.remove(child)



        if len(children)!=0:

            dx = width/(len(children)**q)
            nextx = xcenter - width/2 + dx/2
            if(i==0):
                vert_loc-=vert_gap
            elif ( pos[temp[i]][1]!=pos[temp[i-1]][1]):
                vert_loc-=vert_gap

            for child in children:
                if(child not in pos.keys()):
                    pos[child]=(nextx,vert_loc)

                nextx += dx
            if ( pos[temp[i]][1]!=pos[temp[i+1]][1]):
                width = dx
    b= int(z+c)

    for i in range(b,len(temp)):

        pos[temp[i]]=(-pos[temp[int(z)-1-cnt]][0],pos[temp[i]][1])

        cnt+=1

    return pos
