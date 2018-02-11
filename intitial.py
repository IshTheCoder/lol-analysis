import itertools
import collections
import comp182
import numpy
import random
import math


def bfs(g, startnode):
    """
    Perform a breadth-first search on g starting at node startnode.

    Arguments:
    g -- undirected graph
    startnode - node in g to start the search from

    Returns:
    The distances from startnode to each node.
    """
    dist = {}

    n={}

    # Initialize distances and predecessors
    for node in g:
        dist[node] = float('inf')
        
    dist[startnode] = 0
    n[startnode]=1
    # Initialize the search queue
    queue = collections.deque([startnode])

    # Loop until all connected nodes have been explored
    while queue:
        j = queue.popleft()
        for h in g[j]:
            if dist[h] == float('inf'):
                dist[h] = dist[j] + 1
                n[h]=n[j]
                queue.append(h)
            elif dist[h]==dist[j]+1:
                n[h]=n[j]+n[h]
    return dist, n

g1={0:set([1,2]),1:set([0,3]),2:set([0,3,4]),3:set([1,2,5]),4:set([2,5,6]),5:set([4,3]),6:set([4])}

print bfs(g1,1)

def compute_flow(g, dist, paths):
    """
    Computes the flow across all edges using the outputs from BFS.
    
    Arguments:
    g           -- a graph
    dist        -- a mapping of the distance of each node to the start node
    paths       -- a mapping of the number of shortest paths from the start node to each node
    
    Returns:
    The flow value of each edge in the graph.
    """
    queue1 = collections.deque()
    visited = []
    incoming_flow = {}
    flow_edge = {}
    
    # Begin with the nodes farthest from the start node
    greatestDistance = 0
    for node in g.keys():
        if dist[node] == greatestDistance:
            queue1.appendleft(node)
            incoming_flow[node] = 1
        if dist[node] > greatestDistance and dist[node]!=float("inf"):
            queue1 = collections.deque()
            incoming_flow = {}
            queue1.appendleft(node)
            greatestDistance = dist[node]
            incoming_flow[node] = 1

    # For each node, the incoming flow = 1 + outgoing flow
    while len(queue1) != 0:
        node = queue1.pop()
        visited.append(node)
        for key in dist:
            # Make sure to visit all nodes of a level before moving to a higher level
            if dist[key] == dist[node] and (key not in queue1) and (key!=node) and (key not in visited):
                queue1.appendleft(key)
        for parent in g[node]:
            # There is no flow between nodes of the same level
            if parent not in visited and dist[parent]!=dist[node]:
                if node not in incoming_flow:
                    incoming_flow[node] = 1
                flow_edge[frozenset([parent, node])] = incoming_flow[node] * float(paths[parent])/paths[node]
                if parent not in incoming_flow.keys():
                    incoming_flow[parent] = 1 + flow_edge[frozenset([parent, node])]
                    queue1.appendleft(parent)
                else:
                    incoming_flow[parent] = incoming_flow[parent] + flow_edge[frozenset([parent, node])]

    return flow_edge

A=bfs(g1,1)

print compute_flow(g1,A[0],A[1])



