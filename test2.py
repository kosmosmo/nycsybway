import ast
import linecache
import random
import unittest
from time import sleep



def dijkstra(graph,map,start,goal):
    shortest_dis = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 999999
    path = []
    path_train = ['poop']
    info = []
    for node in unseenNodes:
        shortest_dis[node] = infinity
    # set start node as 0, the others as infinity
    shortest_dis[start] = 0
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_dis[node] < shortest_dis[minNode]:
                # find the min weight of all nodes
                minNode = node
        for childNode,weight in graph[minNode].items():
            if weight + shortest_dis[minNode] < shortest_dis[childNode]:
                shortest_dis[childNode] = weight + shortest_dis[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('path not reachable')
            break
    path.insert(0,start)
    start,end = 0 , len(path)

    while start + 1 < end:
        path_train.append(list(set(map[path[start]])&set(map[path[start+1]])))
        start += 1
    path_train = path_train[1:]



    print path
    print path_train


file_graph = open('graph.txt', 'r')
file_map = open('map.txt', 'r')
graph = ast.literal_eval(file_graph.read())
map = ast.literal_eval(file_map.read())
dijkstra(graph,map,'80 Street(A)','75 Avenue(EF)')