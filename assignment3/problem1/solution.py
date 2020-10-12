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
  
  print(f"Number of vertices: {num_vertices}")
  print(f"Number of edges:{num_edges}")
  print(edge_array)

main()