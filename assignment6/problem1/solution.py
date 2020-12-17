from collections import defaultdict
from collections import deque

def BFS(graph, s, t, visited, one_path):

  visited[s-1] = True
  one_path.append(s)

  if(s==t):
    return True

  for i in graph.keys():
    for j in graph[i].keys():
      if(i==s and graph[i][j] != 0 and visited[j-1] == False):
        if(BFS(graph, j, t, visited, one_path)):
          return True

  one_path.pop()
  return False
        
def augment(graph, bottleneck, one_path):

  for initial_vertex, sink_capacity_list in graph.items():
    for sink, capacity_flow in sink_capacity_list.items():
      c = capacity_flow[0]
      f = capacity_flow[1]

      for i in range(len(one_path)-1):

        if(initial_vertex == one_path[i] and sink == one_path[i+1]):
          graph[initial_vertex][sink] = (c, f+bottleneck)
          residual_graph[initial_vertex][sink] = c-(f+bottleneck)
          residual_graph[sink][initial_vertex] = f+bottleneck
      
        elif(sink == one_path[i] and initial_vertex == one_path[i+1]):
          graph[initial_vertex][sink] = (c, f-bottleneck)
          residual_graph[initial_vertex][sink] = c-(f-bottleneck)
          residual_graph[sink][initial_vertex] = f-bottleneck

  return graph


def Ford_Fulkerson(graph, s, t):
  global max_flow
  global count

  while(True):

    one_path.clear()
    visited = [False]*(num_vertices)
    BFS(residual_graph, s, t, visited, one_path)

    if len(one_path) == 0:
      return max_flow

    capacities = []
    for i in range(len(one_path)-1):
      capacities.append(residual_graph[one_path[i]][one_path[i+1]])
      
    bottleneck = min(capacities)
    max_flow += bottleneck
  
    augment(graph, bottleneck, one_path)


user_input = input().strip().split(" ")
num_vertices = int(user_input[0])
num_edges = int(user_input[1])

graph = defaultdict(dict)
residual_graph = defaultdict(dict)
max_flow = 0
count = 0 
one_path = deque()

for edge in range(num_edges):
  edge_input = input()
  edges = list(map(int, edge_input.strip().split(' ')))
  already_present = False

  if(not bool(graph)):
    graph[edges[0]] [edges[1]] = (edges[2], 0)
    residual_graph[edges[0]] [edges[1]] = edges[2]
    continue

  if(edges[1] in graph[edges[0]].keys()):
    graph[edges[0]][edges[1]] = (edges[2]+graph[edges[0]][edges[1]][0], graph[edges[0]][edges[1]][1])
    residual_graph[edges[0]] [edges[1]] = edges[2]+graph[edges[0]][edges[1]][0]
    already_present = True

  if(already_present == False):
    graph[edges[0]] [edges[1]] = (edges[2], 0)
    residual_graph[edges[0]] [edges[1]] = edges[2]

Ford_Fulkerson(graph, 1, num_vertices)
print(max_flow)