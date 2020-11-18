"""
Math 560
Project 5
Fall 2020

Partner 1:
Partner 2:
Date:
"""

# Import math, itertools, and time.
import math
import itertools
import time

# Import the Priority Queue.
from p5priorityQueue import *

################################################################################

"""
Prim's Algorithm
"""
def prim(adjList, adjMat):
    ##### Your implementation goes here. #####
    return

################################################################################

"""
Kruskal's Algorithm
Note: the edgeList is ALREADY SORTED!
Note: Use the isEqual method of the Vertex class when comparing vertices.
"""
def kruskal(adjList, edgeList):

    # Loop through and initialize all vertices
    for vertex in adjList:
        makeset(vertex)

    # Initialize X
    X = []

    # Loop through a sorted edgeList and get the vertices of each edge
    for e in edgeList:
        u, v = e.vertices

        # If U and V do not share a root, append the edge and union u and v
        if find(u) != find(v):
            X.append(e)
            union(u,v)

    return X

################################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union

These functions will operate directly on the input vertex objects.
"""

"""
makeset: this function will create a singleton set with root v.
"""
def makeset(v):
    # Initialize v.pi to itself and height to 0
    v.pi = v
    v.height = 0
    return

"""
find: this function will return the root of the set that contains v.
Note: we will use path compression here.

"""
def find(v):
    # Compressed Path to find the root that contains v
    if v != v.pi:
        v.pi = find(v.pi)

    return v.pi

"""
union: this function will union the sets of vertices v and u.
"""
def union(u,v):
    # Find roots of U and V
    ru = find(u)
    rv = find(v)

    # If they share the same root return
    if ru.isEqual(rv):
        return
    # If u is taller than v, point v to u
    if ru.height > rv.height:
        rv.pi = ru
    # Elif v is taller than u, point u to v
    elif ru.height < rv.height:
        ru.pi = rv
    # Else point u to v and increase the height of v by 1
    else:
        ru.pi = rv
        rv.height+=1
    return

################################################################################

"""
TSP
"""
def tsp(adjList, start):
    ##### Your implementation goes here. #####


    tour = [10]
    return tour




################################################################################

# Import the tests (since we have now defined prim and kruskal).
from p5tests import *

"""
Main function.
"""
if __name__ == "__main__":
    verb = False # Set to true for more printed info.
    #print('Testing Prim\n')
    #print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))