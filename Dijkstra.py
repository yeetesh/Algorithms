graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],[4, 0, 8, 0, 0, 0, 0, 11, 0],[0, 8, 0, 7, 0, 4, 0, 0, 2],[0, 0, 7, 0, 9, 14, 0, 0, 0],[0, 0, 0, 9, 0, 10, 0, 0, 0],[0, 0, 4, 14, 10, 0, 2, 0, 0],[0, 0, 0, 0, 0, 2, 0, 1, 6],[8, 11, 0, 0, 0, 0, 1, 0, 7],[0, 0, 2, 0, 0, 0, 6, 7, 0]];
  
def minimum(dist,visited):
    least = 9999
    index = -1
    for i in range(len(graph)):
        if i not in visited and dist[i] < least:
            least = dist[i]
            index = i
    return index
            
def dijkstra(source):
    visited = set()
    distance = []
    for i in range(len(graph)):
        distance.append(9999)
    distance[source] = 0 
    for i in range(len(graph)):
        u = minimum(distance,visited)
        visited.add(u)
        for j in range(len(graph)):
            if j not in visited and graph[u][j] > 0: 
                if distance[u]+graph[u][j] < distance[j]:
                    distance[j] = distance[u] + graph[u][j]
    for i in range(len(graph)):
        print(i,distance[i])

dijkstra(0)

    