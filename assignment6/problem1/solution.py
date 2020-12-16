from collections import defaultdict

def build_residual(graph):
  for initial_vertex, sink_capacity_list in graph.items():
    for sink, capacity_flow in sink_capacity_list.items():
      u = initial_vertex
      v = sink
      c = capacity_flow[0]
      f = capacity_flow[1]

      residual_graph[u][v] = c-f
      residual_graph[v][u] = f

  return residual_graph

def Ford_Fulkson(graph, s, t):
  print("Actual graph")
  print(graph)
  print("Residual graph")
  print(build_residual(graph))

user_input = input().strip().split(" ")
num_vertices = int(user_input[0])
num_edges = int(user_input[1])
vertices = set()

graph = defaultdict(dict)
residual_graph = defaultdict(dict)

for edge in range(num_edges):
  edge_input = input()
  edges = list(map(int, edge_input.strip().split(' ')))
  graph[edges[0]] [edges[1]] = (edges[2], 0)
  
  vertices.add(edges[0])
  vertices.add(edges[1])

print(Ford_Fulkson(graph, 1, vertices))