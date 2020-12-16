from collections import defaultdict

def BFS(graph, s, t, path, visited, one_path):
  
  visited[s-1] = True
  path.append(s)

  if(s==t):
    current_path = path.copy()
    one_path.append(current_path)
    return

  else:
    for initial_vertex, sink_capacity_list in graph.items():
      for sink, capacity_flow in sink_capacity_list.items():
        if(initial_vertex==s and capacity_flow!=0):
          if(visited[sink-1]==False):
            BFS(graph, sink, num_vertices, path, visited, one_path)

  path.pop()
  visited[s-1] = False

def augment(graph, bottleneck, one_path):

  for initial_vertex, sink_capacity_list in graph.items():
    for sink, capacity_flow in sink_capacity_list.items():
      c = capacity_flow[0]
      f = capacity_flow[1]

      for i in range(len(one_path[0])-1):

        if(initial_vertex == one_path[0][i] and sink == one_path[0][i+1]):
          graph[initial_vertex][sink] = (c, f+bottleneck)
          residual_graph[initial_vertex][sink] = c-(f+bottleneck)
          residual_graph[sink][initial_vertex] = bottleneck
      
        elif(sink == one_path[0][i] and initial_vertex == one_path[0][i+1]):
          graph[sink][initial_vertex] = (c, f-bottleneck)
          residual_graph[initial_vertex][sink] = c-(f+bottleneck)
          residual_graph[sink][initial_vertex] = bottleneck

  return graph


def Ford_Fulkerson(graph, s, t):
  global max_flow
  global count

  print("Actual graph")
  print(graph)

  print("Residual graph")
  print(residual_graph)
  print("\n")

  visited = [False]*(num_vertices)
  path = []
  one_path = []
  print(f"Residual before BFS: {residual_graph}")
  BFS(residual_graph, s, t, path, visited, one_path)
  print(f"One path: {one_path}")

  if len(one_path) == 0:
    return max_flow

  capacities = []
  for initial_vertex, sink_capacity_list in residual_graph.items():
    for sink, capacity_flow in sink_capacity_list.items():
      for i in range(len(one_path[0])-1):
        if(initial_vertex == one_path[0][i] and sink == one_path[0][i+1]):
          capacities.append(capacity_flow)


  print(f"Capacities: {capacities}")
  bottleneck = min(capacities)
  max_flow += bottleneck
  print(f"Bottleneck: {bottleneck}")

  if(bottleneck != 0):
    Ford_Fulkerson(augment(graph, bottleneck, one_path), 1, num_vertices)


user_input = input().strip().split(" ")
num_vertices = int(user_input[0])
num_edges = int(user_input[1])

graph = defaultdict(dict)
residual_graph = defaultdict(dict)
max_flow = 0
count = 0 

for edge in range(num_edges):
  edge_input = input()
  edges = list(map(int, edge_input.strip().split(' ')))
  already_present = False

  if(not bool(graph)):
    graph[edges[0]] [edges[1]] = (edges[2], 0)
    residual_graph[edges[0]] [edges[1]] = edges[2]
    continue

  for initial_vertex, sink_capacity_list in graph.items():
    for sink, capacity_flow in sink_capacity_list.items():
      if(initial_vertex==edges[0] and sink==edges[1]):
        graph[edges[0]][edges[1]] = (edges[2]+capacity_flow[0], capacity_flow[1])
        residual_graph[edges[0]] [edges[1]] = edges[2]+capacity_flow[0]
        already_present = True
      break

  if(already_present == False):
    graph[edges[0]] [edges[1]] = (edges[2], 0)
    residual_graph[edges[0]] [edges[1]] = edges[2]

Ford_Fulkerson(graph, 1, num_vertices)
print(max_flow)