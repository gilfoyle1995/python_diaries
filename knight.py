#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:32:57 2017

@author: arpanpain
"""

def ispossible(p,q):
    if(p < 8 and p >= 0 and q < 8 and q>=0):
        return True
    else:
        return False
        
def printpath(parent,end):
    s = end
    if(parent[s] == "none"):
        print(end,end ="")
        return 
    else:
        printpath(parent,parent[s])
        print("->",end="")
        print(end,end="")

def bfs(adj,start,end):
    moves = {start:0}
    parent = {start:"none"}
    frontier = [start]
    j =1;
    while frontier:
        next = []
        for u in frontier:
            #GRAPH INPUT PER NODE VISITED 
            for i in range(8):
                if(i == 0):
                    p = u[0] + 2
                    q = u[1] + 1
                    if(ispossible(p,q)):
                        adj[u].append((p,q))
                        if((p,q) not in adj.keys()):
                            adj[(p,q)] = []
                elif(i == 1):
                    p = u[0] + 2
                    q = u[1] - 1
                    if(ispossible(p,q)):
                        adj[u].append((p,q))
                        if((p,q) not in adj.keys()):
                            adj[(p,q)] = []
                elif(i == 2):
                    p = u[0] + 1
                    q = u[1] + 2
                    if(ispossible(p,q)):
                        adj[u].append((p,q))
                        if((p,q) not in adj.keys()):
                            adj[(p,q)] = []
                elif(i == 3):
                    p = u[0] + 1
                    q = u[1] - 2
                    if(ispossible(p,q)):
                        adj[u].append((p,q))
                        if((p,q)not in adj.keys()):
                            adj[(p,q)] = []
                elif(i == 4):
                    p = u[0] - 2
                    q = u[1] + 1
                    if(ispossible(p,q)):
                        adj[u].append((p,q))
                        if((p,q)not in adj.keys()):
                            adj[(p,q)] = []
                elif(i == 5):
                    p = u[0] - 2
                    q = u[1] - 1
                    if(ispossible(p,q)):
                        adj[u].append((p,q))
                        if((p,q)not in adj.keys()):
                            adj[(p,q)] = []
                elif(i == 6):
                    p = u[0] - 1
                    q = u[1] + 2
                    if(ispossible(p,q)):
                        adj[u].append((p,q))
                        if((p,q)not in adj.keys()):
                            adj[(p,q)] = []
                elif(i == 7):
                    p = u[0] - 1
                    q = u[1] - 2
                    if(ispossible(p,q)):
                        adj[u].append((p,q))
                        if((p,q)not in adj.keys()):
                            adj[(p,q)] = []
                    
            for v in adj[u]:
                if( (v not in moves) ):
                    moves[v] = j
                    parent[v] = u
                    next.append(v)
        frontier = next
        j+=1
    printpath(parent,end)
    return moves

#for initialisation of the graph
adj = {}
print("quiery engine is running ask moves now!!")
#input bishop's position
p,q = input().strip().split(" ")
start = (int(p),int(q))
adj[start] = []
#input chessboard size
n = input().strip()
n = int(n)
#input position to find
x, y = input().strip().split(" ")
end= (int(x), int(y))
#graph generation for knight
moves = bfs(adj,start,end)
print("with "+str(moves[end]) +" moves knight can reach from start:"+str(start)+"to end:"+str(end))
