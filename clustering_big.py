# -*- coding: utf-8 -*-
"""
Created on Sun May  7 17:54:48 2017
Description: Writing a code for implementing clustering using an algorithms that resembles
Kruskals.
@author: Yonarp
"""

import networkx as nx
Uf = nx.utils.UnionFind()

def PrintClusters(Uf):
    for i in Uf:
        print (i,Uf[i],bin(i))

def GetTheArray(num):
    sumList = list()
    for i in range(num):
        sumList.append(2**i)
#    print (sumList)
    for i in range(num):
        for j in range(i+1,num):
            sumList.append(2**i+2**j)
    return sumList

def GetNearbyNums(num,sumList):
    length = len(sumList)
    for i in range(length):
        sumList[i]^=num
        if(sumList[i]>2**length):
            sumList[i]%=(2**length)
    return sumList

def PrintTheNumberOfClusters(Uf):
    clusters = set()
    for i in Uf:
#        print (Uf[i])
        clusters.add(Uf[i])
    print (len(clusters))

    
    
path = "clustering_big1.txt"

with open(path) as nodes:
    noOfNodes,bitsPerNode = map(int,nodes.readline().strip().split())
#    print (noOfNodes,bitsPerNode)
    vertices = set()
    foo = list()
    for node in nodes:
        vertex = node.strip().replace(" ","")
        vertices.add(int(vertex,2))
        Uf.union(int(vertex,2))
        foo.append(int(vertex,2))
#    PrintClusters(Uf)
#    print()
    sumList = GetTheArray(bitsPerNode)
    for vertex in vertices:
        sumlist = list(sumList)
        items  = GetNearbyNums(vertex,sumlist)
#        print ("vertex",vertex,bin(vertex))
#        print (items[23],"\t\t",bin(items[23]))
        for nearBy in items:
            if ((nearBy in vertices) and (Uf[vertex]!=Uf[nearBy])):
#                print (bin(vertex))
#                print (bin(nearBy))
#                print (items.index(nearBy))
#                print (len(items))
                Uf.union(vertex,nearBy)
#    print()
#    PrintClusters(Uf)
    PrintTheNumberOfClusters(Uf)