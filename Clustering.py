# -*- coding: utf-8 -*-
"""
Created on Sun May  7 17:54:48 2017
Description: Writing a code for implementing clustering using an algorithms that resembles
Kruskals.
@author: Yonarp
"""

import heapq


def populateLeaderArrayEdgesHeap(path):
    heap = []
    with open(path) as edges:
        noOfNodes = edges.readline()
        Leaders  = [0] + [i+1 for i in range(int(noOfNodes))]
        
        for edge in edges:
            first,second,length = list(map(int,edge.strip().split()))
            heapq.heappush(heap,[length,first,second])
    return heap,Leaders
        
 
def pickEachEdge(heap,Leaders,n):
    while(1):
        length,first,second = heapq.heappop(heap)
        # print (first,second,length)
        minSwap(first,second)
        if(Leaders[first]!=Leaders[second]):
            leadFirst,leadSecond = Leaders[first],Leaders[second]
            for i in range(len(Leaders)):
                if i is 0:
                    continue
                if(Leaders[i]==leadFirst or Leaders[i]==leadSecond):
#                    if(i == 497 or i == 135):
#                        print(first, second) 
#                        print(Leaders[135],Leaders[497])
                    Leaders[i]=leadFirst
#                    print(Leaders[135],Leaders[497])
#                    if(Leaders[135] != Leaders[497]):
#                        print ("Pranoy")
                    
        #Count the number of clusters
        clusters = list(set(Leaders[1:]))
        if(len(clusters)== n):
            break
    return clusters



def minSwap(m,n):
    if(m<n):
        return m,n
    else:
        return n,m

def populateMinClusterMatrix(heap,Leaders,clusters,MinClusterMatrix):
    while(heap):
        length,first,second = heapq.heappop(heap)
        firstIndex,secondIndex = clusters.index(Leaders[first]), \
                                        clusters.index(Leaders[second])
        firstIndex,secondIndex = minSwap(firstIndex,secondIndex)
        if(Leaders[first]!=Leaders[second]):
            if(length == 2):
                print ("length",length)
                print ("first and second",first,second)
                print ("Leaders[first] and Leaders[second]",Leaders[first],Leaders[second])
            if(length<MinClusterMatrix[firstIndex][secondIndex]):
                MinClusterMatrix[firstIndex][secondIndex] = length
                


#maxSpacing = -100000000
#for i in range(len(clusters)):
#    for j in range(len(clusters)):
#        if(MinClusterDis[i][j] == 10000000):
#            continue
#        if(MinClusterDis[i][j] > maxSpacing):
#            maxSpacing = MinClusterDis[i][j]

#heap = [[-heap[i][0],heap[i][1],heap[i][2]] for i in range(len(heap))]
#
#while(True):
#    length,first,second = heapq.heappop(heap)
#    if (Leaders[first]!=Leaders[second]):
#        break


def main():
    path = "clustering1.txt"
    heap,Leaders = populateLeaderArrayEdgesHeap(path)
    #print ("\nheap",heap)
    #print ("\nLeaders",Leaders)
    #print ("\nPick edges till the clusters are four")
    
    clusters = pickEachEdge(heap,Leaders,4)
#    print ("\nheap",heap)
#    print ("\nLeaders",Leaders)
#    print  ("Leader of 135 is", Leaders[135],"and Leader of 497 is", Leaders[497])
#    print  ("Leader of 440 is", Leaders[440],"and Leader of 493 is", Leaders[493])
    print ("\nClusters", clusters)
#    
    MinClusterMatrix = [[10000000]*len(clusters) for i in range(len(clusters))]
    print ("\nMinClusterMatrix before populating ",MinClusterMatrix)
    heapTemp,temp = populateLeaderArrayEdgesHeap(path)
#    print ("\nheapTemp",heapTemp)
    populateMinClusterMatrix(heapTemp,Leaders,clusters,MinClusterMatrix)
    print ("\nMinClusterMatrix after populating ",MinClusterMatrix)
#    maxSpacing = min([y for x in MinClusterMatrix for y in x])
#    #print ('\nThe length of the maximum spacing for final cluster is ',maxSpacing)
    
main()