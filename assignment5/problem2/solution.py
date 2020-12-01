from collections import namedtuple

class Node:
  def __init__(self, data, parent, height):
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
    r_x = find(self)
    r_y = find(other)

    if r_x == r_y:
      return
    
    if(r_x.height > r_y.height):
      r_y.parent = r_x

    elif(r_x.height < r_y.height):
      r_x.parent = r_y

    else:
      r_y.parent = r_x
      r_x += 1


# def Kruskals(interval_list):

user_input = input().strip().split(" ")
num_vertices = int(user_input[0])
num_edges = int(user_input[1])

edges_list = []

for edge in range(num_edges):
  edge_input = input()
  edges = list(map(int, edge_input.strip().split(' ')))
  edges_list.append(edges)

edges_list.sort(key=lambda x:x[2])

print(num_vertices)
print(num_edges)
print(edges_list)
# print(Kruskals(edges_list))