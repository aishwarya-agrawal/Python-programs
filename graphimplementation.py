from collections import defaultdict
graph =defaultdict(list)
'''{ "a":["b","c"],
          "b" :["d","e"],
          "c" : ["d","e"],
          "d" : ["e","f"],
          "e" : ["f","a"],
          "f" : []}
'''
def addedge(graph,v,u):
    graph[v].append(u)
def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node,neighbour))
    return edges

print(generate_edges(graph))
