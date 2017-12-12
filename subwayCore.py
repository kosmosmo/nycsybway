from PySide.QtGui import *
from PySide.QtCore import *
from subwayUi import subwayUi

import sys
import ast



class subwayCore(subwayUi):
    file_graph = open('graph.txt', 'r')
    file_map = open('map.txt', 'r')
    graph = ast.literal_eval(file_graph.read())
    map = ast.literal_eval(file_map.read())
    stations = []
    info = []

    for key, val in graph.items():
        stations.append(key)

    def __init__(self):
        super(subwayCore,self).__init__()
        self.build_start_list()
        self.build_goal_list()

        self.start_search_line_edit.textChanged.connect(self.build_start_list)
        self.goal_search_line_edit.textChanged.connect(self.build_goal_list)
        self.find_button.clicked.connect(self.build_info)





    def build_start_list(self):
        self.start_list_widget.clear()
        search_pattern = self.start_search_line_edit.text().lower()
        for station in self.stations:
            name = station
            if search_pattern in name.lower():
                item = QListWidgetItem(name)
                item.setData(32, station)
                self.start_list_widget.addItem(item)
        self.start_list_widget.sortItems()

    def build_goal_list(self):
        self.goal_list_widget.clear()
        search_pattern = self.goal_search_line_edit.text().lower()
        for station in self.stations:
            name = station
            if search_pattern in name.lower():
                item = QListWidgetItem(name)
                item.setData(32, station)
                self.goal_list_widget.addItem(item)
        self.goal_list_widget.sortItems()

    def build_info(self):
        self.info_text_edit.clear()
        text = ''
        file_graph = open('graph.txt', 'r')
        a = ast.literal_eval(file_graph.read())
        infos = self.dijkstra(a, str(self.start_list_widget.currentItem().text()), str(self.goal_list_widget.currentItem().text()))
        for info in infos:
            for i in info.split():
                self.info_text_edit.insertPlainText(i + ' ')
                self.info_text_edit.setStyleSheet("QLineEdit { background-color: yellow }")
            self.info_text_edit.appendPlainText(' ')






    def dijkstra(self, graph, start, goal):
        print start,goal
        shortest_dis = {}
        predecessor = {}
        unseenNodes = graph
        infinity = 999999
        path = []
        info = []
        path_train = ['poop']
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
            for childNode, weight in graph[minNode].items():
                if weight + shortest_dis[minNode] < shortest_dis[childNode]:
                    shortest_dis[childNode] = weight + shortest_dis[minNode]
                    predecessor[childNode] = minNode
            unseenNodes.pop(minNode)
        currentNode = goal
        while currentNode != start:
            try:
                path.insert(0, currentNode)
                currentNode = predecessor[currentNode]
            except KeyError:
                print('NOPE!')
                break
        path.insert(0, start)
        start, end = 0, len(path)

        while start + 1 < end:
            path_train.append(list(set(self.map[path[start]]) & set(self.map[path[start + 1]])))
            start += 1
        path_train = path_train[1:]


        for i in range(len(path_train)):
            line = path[i] + ":   "
            if len(path_train[i]) > 1:
                for j in range(len(path_train[i])):
                    line += (path_train[i])[j]
                    if j != len(path_train[i]) - 1:
                        line += " or "
            else:
                line += (path_train[i])[0]
            info.append(line)
        info.append(path[-1])
        info.append("Waiting time is " + str(shortest_dis[goal]) + " min")

        return info







app = QApplication(sys.argv)
panel = subwayCore()
panel.show()
app.exec_()