timing = 0
num_cc = 0

postlist = []
visited = []
vertex = []

magic_visited = []

num_vertices = 0
num_edges = 0

def DFS(edge_array):
  global num_vertices
  global timing
  timing = 1

  for i in range(num_vertices):
    if(visited[i] == 0):
      explore(edge_array, i, vertex[i])


def explore (edge_array, i, visit_vertex):
  global timing
  count = 0

  timing += 1
  visited[i] = 1

  for edge in edge_array:
    if(edge[0]==visit_vertex and visited[vertex.index(edge[1])]==0):
      explore(edge_array, vertex.index(edge[1]), edge[1])

  timing += 1
  postlist.append(visit_vertex)


def magic_DFS(edge_array):
  global num_cc
  num_cc = 0

  for vertex in postlist:
    if(magic_visited[vertex-1] == 0):
      num_cc += 1
      magic_explore(edge_array, vertex-1, vertex)


def magic_explore(edge_array, i, visit_vertex):
  magic_visited[i] = num_cc
  count = 0

  for edge in edge_array:
    if(edge[0] == visit_vertex and magic_visited[edge[1]-1]==0 ):
       magic_explore(edge_array, edge[1]-1, edge[1])

line_1 = input()
line_1 = line_1.strip().split(' ')

num_vertices = int(line_1[0])
num_edges = int(line_1[1])

edge_array = []
reverse_edge_array = []

for edge in range(num_edges):
  edge_input = input()
  edges = list(map(int, edge_input.strip().split(' ')))
  edge_array.append(edges)
  reverse_edge_array.append([edges[1],edges[0]])

for i in range(num_vertices):
  vertex.append(i+1) 
  visited.append(0)
  magic_visited.append(0)

DFS(reverse_edge_array)
postlist.reverse()
magic_DFS(edge_array)

print(num_cc)