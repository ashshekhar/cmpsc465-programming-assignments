def DFS(reverse_edge_array):

  return

def magic_order(num_vertices, num_edges, edge_array):

  reverse_edge_array = []
  
  for edge in edge_array:
    orig_u = edge[0]
    orig_v = edge[1]
    reverse_edge_array.append([orig_v, orig_u])

  print(f"Reversed order of edges: {reverse_edge_array}")

  DFS(reverse_edge_array)
  
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

main()