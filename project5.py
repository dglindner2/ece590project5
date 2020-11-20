"""
Math 560
Project 5
Fall 2020

Partner 1: George Lindner (dgl12)
Partner 2: Ezinne Nwankwo (esn11)
Date: November 20, 2020
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

    # Initialize all costs to infinity and previous to null.
    for vertex in adjList:
        vertex.cost = math.inf
        vertex.prev = None
        vertex.visited = False

    # Set start vertex and set the cost equal to zero.
    start = adjList[0]
    start.cost = 0

    # Create priority queue.
    Q = PriorityQueue(adjList)

    # Use cost to sort queue.
    while not Q.isEmpty():
        # Get the next unvisited vertex and visit it.
        v = Q.deleteMin()
        v.visited = True

        # For each edge out of v.
        for neighbor in v.neigh:
            # If the edge leads out, update
            if not neighbor.visited:
                if neighbor.cost > adjMat[v.rank][neighbor.rank]:
                    neighbor.cost = adjMat[v.rank][neighbor.rank]
                    neighbor.prev = v
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

    # Step 1: Initialize and Set Flags to False
    for vertex in adjList:
        vertex.dist = math.inf  # Infinite dist initially.
        vertex.visited = False  # Nothing visited at initialization.

    # Step 2: Set Start Visited Flag to True, Push start to stack, Initialize Path
    start.visited = True
    stack = [start]
    path = []

    # Step 3: While the stack is not empty, loop
    while len(stack) > 0:
        # Pop the top element off the stack and append to the path
        current = stack.pop()
        path.append(current.rank)

        # Look at neighbors of current node
        for neighbor in current.mstN:
            if neighbor.visited == False:
                # Set the visited flag to True for the neighbor and append to stack
                neighbor.visited = True
                stack.append(neighbor)

    # Append starting node to path to complete tour
    path.append(start.rank)


    tour = path
    return tour

################################################################################

# Import the tests (since we have now defined prim and kruskal).
from p5tests import *

"""
Main function.
"""
if __name__ == "__main__":
    verb = True # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))