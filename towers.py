def find_min(visited,distance):
    least_distance = 9999
    least_index = -1
    for i in range(len(distance)):
        if i not in visited and distance[i] < least_distance:
            least_distance = distance[i]
            least_index = i    
    return least_index

def dijkstra(source,matrix):
    visited = set()
    distance = [9999] * len(matrix)
    distance[source] = 0
    for j in range(len(distance)):
        current = find_min(visited,distance)
        visited.add(current)
        print(visited)
        for i in range(len(distance)):
            if i not in visited and matrix[current][i] > 0 and distance[i] > matrix[current][i] + distance[current]:
                distance[i] = matrix[current][i] + distance[current]
    return distance[-1]
matrix = [[1,1,1,0,0],[0,1,1,1,1],[0,0,1,1,0],[0,0,0,1,1],[0,0,0,0,1]]

def do_dfs(source,destination,visited,k):
    print(visited)
    if source == destination:
        print(k)
        return
    for i in range(1,len(matrix)):
        if matrix[source][i] == 1:
            if i not in visited:
                visited.add(i)
                do_dfs(i,destination,visited,k + 1)
                visited.remove(i)


def dfs(source,destination):
    steps = len(matrix) + 1
    visited = set()
    visited.add(source)
    do_dfs(source,destination,visited,0)
    
dfs(0,4)
    

    

#print(dijkstra(0,matrix))

        

