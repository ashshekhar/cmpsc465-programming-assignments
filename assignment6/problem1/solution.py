from collections import defaultdict

def BFS(graph, s, t, path, visited, all_path):

  visited[s-1] = True
  path.append(s)

  if(s==t):
    current_path = path.copy()
    all_path.append(current_path)

  else:
    for initial_vertex, sink_capacity_list in graph.items():
      for sink, capacity_flow in sink_capacity_list.items():
        if(initial_vertex==s):
          if(visited[sink-1]==False):
            BFS(graph, sink, num_vertices, path, visited, all_path)

  path.pop()
  visited[s-1] = False
  return all_path

def build_residual(graph):
  for initial_vertex, sink_capacity_list in graph.items():
    for sink, capacity_flow in sink_capacity_list.items():
      u = initial_vertex
      v = sink
      c = capacity_flow[0]
      f = capacity_flow[1]

      if((c-f) != 0):
        residual_graph[u][v] = c-f

      if(f!=0):
        residual_graph[v][u] = f

  return residual_graph

def Ford_Fulkerson(graph, s, t):
  max_flow = 0
  print("Actual graph")
  print(graph)
  print("Residual graph")
  print(build_residual(graph))

  visited = [False]*(num_vertices)
  path = []
  all_path = []
  print("All paths")
  print(BFS(build_residual(graph), s, t, path, visited, all_path))

  if len(all_path) == 0:
    return 0

  for path in all_path:
    capacities = []
    for initial_vertex, sink_capacity_list in residual_graph.items():
      for sink, capacity_flow in sink_capacity_list.items():
         for i in range(len(path)):
           if(initial_vertex == path[i] and sink == path[i+1]):
            capacities.append(capacity_flow)
    print(f"Capacities: {capacities}")
    bottle_neck = min(capacities)
    print(f"Bottleneck: {bottle_neck}")

user_input = input().strip().split(" ")
num_vertices = int(user_input[0])
num_edges = int(user_input[1])

graph = defaultdict(dict)
residual_graph = defaultdict(dict)
adjacent_set = set()

for edge in range(num_edges):
  edge_input = input()
  edges = list(map(int, edge_input.strip().split(' ')))
  already_present = False

  if(not bool(graph)):
    graph[edges[0]] [edges[1]] = (edges[2], 0)
    continue

  for initial_vertex, sink_capacity_list in graph.items():
    for sink, capacity_flow in sink_capacity_list.items():
      if(initial_vertex==edges[0] and sink==edges[1]):
        graph[edges[0]][edges[1]] = (edges[2]+capacity_flow[0], capacity_flow[1])
        already_present = True
      break

  if(already_present == False):
    graph[edges[0]] [edges[1]] = (edges[2], 0)
  
print(Ford_Fulkerson(graph, 1, num_vertices))