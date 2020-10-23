def Bellman_Ford():

  dist = [float('inf')] * num_vertices
  dist[source_vertex-1] = 0

  for k in range(1, num_vertices+1):
    for vertex in vertices_array:
      for egde_value in edge_array:
        v = egde_value[1]
      
        if(v == vertex):
          u = egde_value[0]
          l = egde_value[2]

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

edge_array = []
vertices_array = []

for edge in range(num_edges):
  edge_input = input()
  edges = list(map(int, edge_input.strip().split(' ')))
  edge_array.append(edges)

  if edges[0] not in vertices_array:
    vertices_array.append(edges[0])

  if edges[1] not in vertices_array:
    vertices_array.append(edges[1])

print(Bellman_Ford())