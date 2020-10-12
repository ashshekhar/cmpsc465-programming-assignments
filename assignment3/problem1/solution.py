clock = 0
pre = []
post = []
postlist = []
visited = []
vertex = []

def explore (num_vertices, num_edges, edge_array, i, visit_vertex):
  global clock
  count = 0

  print(f"Clock: {clock}")
  print(clock)
  pre.append(clock)

  clock += 1
  visited[i] = 1

  print(visited)

  for edge in edge_array:
    print(f"Visit vertex in explore {visit_vertex}")
    if(edge[0] == visit_vertex):
      vertex_j = edge[1]
      count += 1

  if (count != 0): 
    for edge in edge_array:
      if(visited[vertex.index(vertex_j)] == 0):
        print(f"Vertex j: {vertex_j}")
        explore (num_vertices, num_edges, edge_array, vertex.index(vertex_j), vertex_j)

  post.insert(i, clock)
  clock += 1
  postlist.append(visit_vertex)

  print(f"Postlist: {postlist}")

  return


def DFS(num_vertices, num_edges, edge_array):

  global clock
  clock = 1

  print(f"Number of vertices in DFS: {num_vertices}")
  for i in range(num_vertices):
    vertex.append(i+1) 
    visited.append(0)
  
  for i in range(num_vertices):
    if(visited[i] == 0):
      print(f"Enter explore to explore {vertex[i]}")
      explore(num_vertices, num_edges, edge_array, i, vertex[i])

def magic_order(num_vertices, num_edges, edge_array):

  reverse_edge_array = []
  
  for edge in edge_array:
    orig_u = edge[0]
    orig_v = edge[1]
    reverse_edge_array.append([orig_v, orig_u])

  print(f"Reversed order of edges: {reverse_edge_array}")

  DFS(num_vertices, num_edges, reverse_edge_array)

  return

def main():

  line_1 = input()
  line_1 = line_1.strip().split(' ')
  
  num_vertices = int(line_1[0])
  num_edges = int(line_1[1])

  edge_array = []

  for edge in range(num_edges):
    edge_input = input()
    edges = list(map(int, edge_input.strip().split(' ')))
    edge_array.append(edges)
  
  print(f"Original: {edge_array}")

  magic_order(num_vertices, num_edges, edge_array)
  
  print(f"Number of vertices: {num_vertices}")
  print(f"Number of edges:{num_edges}")
  print(edge_array)
  print(f"Final postlist: {postlist}")

main()