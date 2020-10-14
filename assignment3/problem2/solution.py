from queue import PriorityQueue 

def Dijkstra(numVertices, sourceVertex, edges):
    dist = [float('inf')]*numVertices
    PQ = PriorityQueue()

    for vertex in range(1, numVertices+1):
        PQ.put((float('inf'), vertex))

    dist[sourceVertex-1] = 0
    PQ.put((0, sourceVertex))

    while not PQ.empty():
        item = PQ.get()
        u = item[1]
        for edge in edges:
            if(edge[0] == u):
                if(dist[edge[1]-1] > dist[u-1] + edge[2]):
                    dist[edge[1]-1] = dist[u-1] + edge[2]
                    PQ.put((dist[edge[1]-1], edge[1]))

    for value in range(len(dist)):
        if dist[value] == float('inf'):
            dist[value] = -1
        print(dist[value])      

firstLine = input().split(" ")
numVertices = int(firstLine[0])
numEdges = int(firstLine[1])
sourceVertex = int(firstLine[2])
edges = []

for lines in range (numEdges):
    line = [int(i) for i in input().split(" ")]
    edges.append(line)


Dijkstra(numVertices, sourceVertex, edges)
