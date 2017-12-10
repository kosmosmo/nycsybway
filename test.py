import ast

file_graph= open('graph.txt','r')
graph = ast.literal_eval(file_graph.read())

station = []
for key,val in graph.items():
    station.append(key)

print station