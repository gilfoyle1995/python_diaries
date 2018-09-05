#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 20:17:43 2018

@author: arpanpain
"""

class Node(object):
    def __init__(self , name):
        """
        assumption: name is the string 
        """
        self.name = name
        
    def getNode(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    
class Edge(object):
    def __init__(self , src , dest):
        """
        assumes src and dest are Nodes
        """
        self.src = src
        self.dest = dest
        
    def getSource(self):
        return self.src
    
    def getDestination(self):
        return self.dest
    
    def __str__(self):
        return self.src.getNode() + " ------> " + self.dest.getNode()
    

class Digraph(object):
    def __init__(self):
        self.edges = {}
        
    def addNode(self ,node):
        if node in self.edges:
            raise ValueError("Duplicate Node")
        else:
            self.edges[node] = []
            
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.edges and dest in self.edges):
            raise ValueError("Node not in graph")
        self.edges[src].append(dest)
        
        
    def childrenOf(self , node):
        return self.edges[node]
    
    def hasNode(self , node):
        return node in self.edges
    
    def getNode(self , name):
        for node in self.edges:
            if node.getNode() == name:
                return node
        raise NameError("name not found")
        
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result += src.getNode() + " ---> " + dest.getNode() + "\n"
        result = result[:-1]
        return result
    
    
class Graph(Digraph):
    def addEdge(self , edge):
        Digraph.addEdge(self , edge)
        reverse = Edge(edge.getDestination() , edge.getSource())
        Digraph.addEdge(self , reverse)


def buildCityGraph(graphtype):
    g = graphtype()
    
    for names in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'):
        g.addNode(Node(names))
        
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g

def printPath(path):
    result = ""
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result += '-->'
    return result


def DFS(graph , start , end , path , shortest , toPrint = False):
    if toPrint:
        print("current DFS path: " , printPath(path))
    path = path + [start]
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                newpath = DFS(graph , node , end , path , shortest , toPrint)
                if newpath != None:
                    shortest = newpath
        elif toPrint:
            print("already visited" , node)
    return shortest


def BFS(graph , start , end):
    #frontier is the nodes visited in one move
    level = {start : 0}
    parent = {start: None}
    i = 1
    frontier = [start]
    while frontier:
        for u in frontier:
            next1 = []
            #print(u)
            for v in graph.childrenOf(u):
                #print(u , v)
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next1.append(v)
        frontier = next1
        i += 1
    def buildPath(end):
        if end == None:
            return []
        else:
            p_node = parent[end]
            path = buildPath(p_node) + [end]
            return path
    path = buildPath(end)
    return path

def shortestPath(graph , start , end ,toPrint = False):
    path = BFS(graph , start , end)
    return path

def testSP(source , destination):
    g = buildCityGraph(Digraph)
    
    path = shortestPath(g , g.getNode(source) ,g.getNode(destination) ,True)
    if path != None:
        result = printPath(path)
        print(result)
    else:
        print("there is no path from " , source , " to " , destination )
print(buildCityGraph(Digraph))    
testSP('Chicago' , 'New York')
    