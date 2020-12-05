class Node:
  def __init__(self, data, height=0):
    self.data = data
    self.parent = self
    self.height = height

  def make_set(self):
    self.height = 1
    self.parent = self

  def find(self):
    while(self.parent != self):
      self = self.parent
    return self

  def union(self, other):
    r_x = Node.find(self)
    r_y = Node.find(other)

    if r_x == r_y:
      return
    
    if(r_x.height > r_y.height):
      r_y.parent = r_x

    elif(r_x.height < r_y.height):
      r_x.parent = r_y

    else:
      r_y.parent = r_x
      r_x.height += 1


def Kruskals(edges_list, vertices):

  visited_edges = []
  vertex_node = []

  for vertex in vertices:
    v = Node(vertex)
    Node.make_set(v)
    vertex_node.append(v)

  for edge in edges_list:
    def condition(x, y): return x.data == edge[y]
    def find_node(x): return [idx for idx, element in enumerate(vertex_node) if condition(element, x)]

    r_u = Node.find(vertex_node[find_node(0)[0]])
    r_v = Node.find(vertex_node[find_node(1)[0]])

    if(r_u != r_v):
      visited_edges.append(edge)
      Node.union(r_u, r_v)

  min_cost = 0
  for edge in visited_edges:
    min_cost += edge[2]
  return min_cost

user_input = input().strip().split(" ")
num_vertices = int(user_input[0])
num_edges = int(user_input[1])

edges_list = []
vertices = set()

for edge in range(num_edges):
  edge_input = input()
  edges = list(map(int, edge_input.strip().split(' ')))
  vertices.add(edges[0])
  vertices.add(edges[1])
  edges_list.append(edges)

edges_list.sort(key=lambda x:x[2])
list(vertices)
print(Kruskals(edges_list, vertices))