import ast

file_graph= open('graph.txt','r')
graph = ast.literal_eval(file_graph.read())

station = []
for key,val in graph.items():
    station.append(key)

print station


149 Street-Grand Concourse 96 Street(BC)
103 Street(BC) 233 Street(25)
116 Street(23) 103 Street(BC)
96 Street(BC) West Farms Square-East Tremont Avenue
103 Street(BC) 170 Street(BD)
Cathedral Parkway (110 Street)(BC) 157 Street(1)
233 Street(25) 86 Street(BC)
3 Avenue-149 Street 103 Street(BC)
23 Street(6) Cathedral Parkway (110 Street)(BC)
Cathedral Parkway (110 Street)(BC) 137 Street-City College
86 Street(BC) Fordham Road(4)
Cathedral Parkway (110 Street)(BC) 96 Street(123)
86 Street(BC) 116 Street(6)
174 Street(25) 86 Street(BC)
3 Avenue-149 Street 81 Street-Museum of Natural History(ABCD)
Morris Park 86 Street(BC)
Cathedral Parkway (110 Street)(BC) Court Sq
Mosholu Parkway(4) Cathedral Parkway (110 Street)(BC)
