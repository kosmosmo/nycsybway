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

    for i in range(len(path_train)):
        line = "at station "+path[i]+ " take train "
        if len(path_train[i]) > 1:
            for j in range(len(path_train[i])):
                line += (path_train[i])[j]
                if j != len(path_train[i]) - 1:
                    line += " or "
        else: line += (path_train[i])[0]
        line += " to station "
        line += path[i+1]
        line += ","
        info.append(line)
    info.append(path[-1])

    return info
#


def utest(n):

    for i in range(n):
        try:
            file_graph = open('graph.txt', 'r')
            file_map = open('map.txt', 'r')
            graph = ast.literal_eval(file_graph.read())
            map = ast.literal_eval(file_map.read())
            k = 0
            arr2 = list(graph)
            a = arr2[random.randint(0, len(arr2)-1)]
            b = arr2[random.randint(0, len(arr2)-1)]
            dijkstra(graph, map, a, b)
        except:
            print a, b


utest(5000)







