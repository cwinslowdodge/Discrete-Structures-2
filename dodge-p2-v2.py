#using Python 3

print('Please enter the vertices you would like in your matrix: ')
vertices = input().split(', ')
print('Please enter the edges that connect the vertices: ')
edges = input().split(', ')

#vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#edges = ['a-c-7', 'a-b-1', 'b-c-2', 'c-d-3', 'c-e-8', 'd-e-4', 'e-f-5', 'e-g-9', 'f-g-6']

#vertices = ['a','b','c','d','e','f','g']
#edges = ['a-c-3','a-b-2','b-c-2','c-d-1','c-e-4','d-e-2','e-f-1','e-g-2','f-g-5','b-f-6']

#vertices = ['a','b','c','d','e','f','g','h']
#edges = ['a-b-2', 'a-c-1', 'b-d-3', 'c-d-5', 'd-e-4', 'e-f-6', 'e-g-7', 'f-h-8', 'g-h-9', 'c-g-10']

def print_path(origin, j):
    if origin[j] == -1:
        return
    print_path(origin, origin[j])

def print_solution(distance, origin, vertices):

    start = vertices[0]
    print("Dijkstra's shortest path from", start)
    for i in range(1, len(distance)):
        print("%s:%s\t%d" % (start, vertices[i], distance[i])),
        print_path(origin, i)

def min_dist(distance, queue):

    minimum = float("Inf")
    min_index = -1

    for i in range(len(distance)):
        if distance[i] < minimum and i in queue:
            minimum = distance[i]
            min_index = i
    return min_index

def dijkstra(matrix, start):

    m_row = len(matrix)
    m_col = len(matrix[0])
    distance = [float("Inf")] * m_row
    origin = [-1] * m_row
    distance[start] = 0
    queue = []

    for i in range(m_row):
        queue.append(i)

    while queue:

        u = min_dist(distance, queue)

        queue.remove(u)

        for i in range(m_col):

            if matrix[u][i] and i in queue:
                if distance[u] + matrix[u][i] < distance[i]:
                    distance[i] = distance[u] + matrix[u][i]
                    origin[i] = u

    print_solution(distance, origin, vertices)

adjMatrix = list(range(len(vertices)))
for i in range(0, len(vertices)):
    adjMatrix[i] = list(range(len(vertices)))

for i in range(0, len(vertices)):
    for j in range(0, len(vertices)):
        adjMatrix[i][j] = 0

for edge in edges:

    y = vertices.index(edge[0])
    x = vertices.index(edge[2])
    w = int(edge[4:])
    adjMatrix[y][x] = w

pedges = edges
def prim(vertices, pedges):
    current_vertex = vertices[0]

    path = []
    i = 0

    for v in vertices:
        current_vertex = v

        connected_nodes = []

        for e in pedges:
            if e[0] == current_vertex or e[2] == current_vertex:
                connected_nodes.append(e)
        connected_nodes.sort(key=lambda x: x[4])
        if len(connected_nodes) > 0 and connected_nodes[0] not in path:
            path.append(connected_nodes[0])
           # for e in pedges:
           #    if e == connected_nodes[0]:
           #        pedges.remove(e)
       #for e in pedges:
           #if e not in path:
               #print(e)
        path.sort(key= lambda x : x[4])
        #path = sorted(path)
    print('Prims minimum spanning tree: ' + str(path))

    return 0

dijkstra(adjMatrix, 0)

prim(vertices, pedges)


#for i in adjMatrix:
    #print(i)
#represented as adjacency list
'''
adjList = {}
start = vertices[0]
aux = []

for i in range(0, len(vertices)):
    adjList[vertices[i]] = []
    for j in range(0, len(edges)):
        if vertices[i] == edges[j][0] or vertices[i] == edges[j][2] and edges[j] not in aux:

            aux.append(edges[j])
            adjList[vertices[i]].append(edges[j])

for i in adjList:
    print(i, ' ', adjList[i])

dijkstra(adjList, start)
'''



