from collections import defaultdict

def Bellman_Ford():

  dist = [float('inf')] * num_vertices
  dist[source_vertex-1] = 0

  for k in range(1, num_vertices+1):
    for initial_vertex, sink_length_list in graph.items():
      for sink, length in sink_length_list.items():
        u = initial_vertex
        v = sink
        l = length

        if((dist[u-1] + l) < dist[v-1]):
          dist[v-1] = dist[u-1] + l
          if(k == num_vertices):
            return True

  return False

line_1 = input()
line_1 = line_1.strip().split(' ')

num_vertices = int(line_1[0])
num_edges = int(line_1[1])
source_vertex = int(line_1[2])

graph = defaultdict(dict)

for edge in range(num_edges):
  edge_input = input()
  edges = list(map(int, edge_input.strip().split(' ')))
  graph[edges[0]] [edges[1]] = edges[2]

print(Bellman_Ford())

