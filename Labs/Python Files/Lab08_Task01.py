print("Muhammad Umair - 12093")

#Note: in this program A B C D E F G H are used as 1 2 3 4 5 6 respectively
def add_edge(adj, src, dest):
    adj[src].append(dest)
    adj[dest].append(src)
  
def BFS(adj, src, dest, v, pred, dist):
    queue = []
    visited = [False for i in range(v)]
  
    for i in range(v):
        dist[i] = 1000000
        pred[i] = -1

    visited[src] = True
    dist[src] = 0
    queue.append(src)
  
    while (len(queue) != 0):
        u = queue[0]
        queue.pop(0)
        for i in range(len(adj[u])):
         
            if (visited[adj[u][i]] == False):
                visited[adj[u][i]] = True
                dist[adj[u][i]] = dist[u] + 1
                pred[adj[u][i]] = u
                queue.append(adj[u][i])
  
                if (adj[u][i] == dest):
                    return True
    return False

def printShortestDistance(adj, s, dest, v):
    pred=[0 for i in range(v)]
    dist=[0 for i in range(v)]
    if (BFS(adj, s, dest, v, pred, dist) == False):
        print("Given source and destination are not connected")
  
    path = []
    crawl = dest
    crawl = dest
    path.append(crawl)
    while (pred[crawl] != -1):
        path.append(pred[crawl])
        crawl = pred[crawl]
  
    print("Shortest path length is : " + str(dist[dest]), end = '')
    
    print("\nPath between source and destination vertex is : ")
    for i in range(len(path)-1, -1, -1):
        print(path[i], end=' ')
 
# Main Function
vertex = 8

adj = [[] for i in range(vertex)]

add_edge(adj, 0, 1)
add_edge(adj, 0, 2)
add_edge(adj, 1, 3)
add_edge(adj, 1, 4)
add_edge(adj, 4, 7)
add_edge(adj, 2, 5)
add_edge(adj, 2, 6)
source = int(input("Enter Source Vertex: "))
dest = int(input("Enter Destination Vertex: "))
printShortestDistance(adj, source, dest, vertex)
