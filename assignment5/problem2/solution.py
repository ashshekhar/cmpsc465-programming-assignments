from collections import defaultdict

class Node:
  def __init__(self, data, parent, height):
    self.data = data
    self.parent = parent
    self.height = height


def make_set(x):
  x.height = 1
  x.parent = x

def find(x):
  while(x.parent != x):
    x = x.parent
  return x

def union(x, y):
  r_x = find(x)
  r_y = find(y)

  if r_x == r_y:
    return
  
  if(r_x.height > r_y.height):
    r_y.parent = r_x

  elif(r_x.height < r_y.height):
    r_x.parent = r_y

  else:
    r_y.parent = r_x
    r_x += 1


def kruskals(interval_list):

  for item in interval_list:
    print(item)

  for _ in range(num_vertices):
    make_set(Node())


user_input = input().strip().split(" ")
num_vertices = int(user_input[0])
num_edges = int(user_input[1])

graph = defaultdict(dict)

for edge in range(num_edges):
  edge_input = input()
  edges = list(map(int, edge_input.strip().split(' ')))
  graph[edges[0]] [edges[1]] = edges[2]

# Sort the graph by edge values

print(num_vertices)
print(num_edges)
print(graph)
# print(kruskals(graph))