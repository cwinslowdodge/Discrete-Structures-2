# Python version 3.5
from random import shuffle
print('Please enter the vertices you would like in your graph: ')
vertices = input().split(', ')
print('Please enter the edges that connect the vertices: ')
edges = input().split(', ')

#vertices = ['a','c','b','d']
#edges = ['a-b','b-c','c-d','d-a']

#vertices = ['e','b','c','d','a']
#edges = ['a-b','c-a','b-c','a-d','e-a','d-e']

#vertices = ['e','b','c','d','a','f','g','h']
#edges = ['c-b','c-a','b-a','a-d','e-a','d-e','d-f','f-g','g-h','c-h','c-g','d-g']

#vertices = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
#edges = ['a-b','b-d','d-g','g-b','f-b','f-g','a-f','c-e','a-c','e-a','f-e','e-h','g-j','l-h','k-h','i-j','k-l','j-m','l-j','h-i','l-m']

#vertices = ['a','b','c','d','e','f','g','h']
#edges = ['a-b','b-c','a-f','b-d','d-f','b-e','e-g','c-g','f-g','f-h','g-h']

#vertices = ['a','b','d','c','e','f']
#edges = ['a-b','a-c','a-f','b-d','b-e','c-e','d-f','e-f']

print('There are ' + str(len(vertices)) + ' vertices: ' + str(vertices))
print('There are ' + str(len(edges)) + ' edges: ' + str(edges))

#print("Sorted edges: ", sorted(edges))

vertex_degree = {}
walk = []

# calculates degree sequence
def degree_seq(vert, edges):
    degree_sequence = []

    for vertex in vert:
        count = 0
        for edge in edges:
            if edge.find(vertex) != -1:
                count += 1
        degree_sequence.append(count)
        vertex_degree[vertex] = count

    return sorted(degree_sequence, reverse=True)

print('The degree sequence is: ' + str(degree_seq(vertices, edges)))

#returns largest degree vertex
def starting_vert(vert_degree):
    start = max(vert_degree, key=vert_degree.get)
    return start

start = (starting_vert(vertex_degree))

# if any vertex has a degree that is not even, returns not Eulerian
def eulerian(degrees):
    for degree in degrees:
        if degree % 2 != 0:
            return ' not'
    return ''

print('This graph is' + eulerian(degree_seq(vertices, edges)) + ' Eulerian')

# if it is Eulerian, give a working trail that proves this
def eulerian_circuit(edges):
    c = []
    i = 0
    j = 0

    current_vertex = start
    if current_vertex == 'f':
        current_vertex = 'g'

    #sorted(edges)
    while len(edges) > 1:

        for edge in edges:

            if edge[0] == current_vertex or edge[2] == current_vertex:
                c.append(edge)

                if edge[0] == current_vertex:
                    current_vertex = edge[2]
                else:
                    current_vertex = edge[0]

                edges.remove(edge)

    c.append(edges[0])

    while i < (len(c) - 1):
        if (c[i][0] == c[i+1][0] or c[i][0] == c[i+1][2]):
            walk.append(c[i][2])
            i+=1
        else:
        #elif (c[i][2] == c[i+1][0] or c[i][2] == c[i+1][2]):
            walk.append(c[i][0])
            i+=1

    if walk[0] == c[len(c)-1][0]:
        walk.append(c[len(c)-1][2])
        walk.append(c[len(c)-1][0])
    else:
        walk.append(c[len(c)-1][0])
        walk.append(c[len(c)-1][2])


    return walk

    #if current vertex == edge[0] or edge[2] go to the next edge in edges

    #x=0
    #print(len(edges))
    #while x < (len(edges) - 1):
#
    #    for edge in edges:
#
    #        if len(c) == 0:
    #            c.append(edge)
    #            # edges.remove(edge)
#
    #        else:
    #            #print("c[x][0]: ", c[x][0])
    #            #print("c[x][2]: ", c[x][2])
    #            #print("edge[0]: ", edge[0])
    #            #print("edge[2]: ", edge[2])
    #            print(c)
    #            if (c[x][2] == (edge[0] or edge[2])) and edge not in c:
    #                c.append(edge)
    #                x+=1
                    # edges.remove(edge)

    #for e in edges:
    #    if ((edge[2]) == e[0] or (edge[2]) == e[2]) and e not in c:
    #        #if len(c) > 1 and ((e[0] or e[2]) == (c[j-2][0] or c[j-2][2])):
    #        #    print(c)
    #        #    remaining.append(e)
    #        #    edges.remove(e)
    #        #else:
    #        #print(c)
    #        c.append(e)
    #        j+=1
    #        edges.remove(e)

    #creates walk based on edge path

#prints the cuircuit if it is Eulerian
if eulerian(degree_seq(vertices, edges)) == '':
    print('Eulerian circuit: ', eulerian_circuit(edges))

# if every vertex can be a different color to all adjacent vertices
def bipartite(c):

    if len(c) != 0:
        for v in c:
            j=1
            count = 1
            while v != c[j]:

                count += 1
                j += 1

            if count%2 != 0:
                return 'is not'

    return 'is'


print("The graph " + bipartite(walk) + " bipartite")


#bp = eulerian_circuit(edges)


# draw it out
def bipartite_rendering(walk):
    v1 = []
    v2 = []
    for v in walk:

        if walk.index(v)%2 == 0 and v not in v1:
            v1.append(v)
        if walk.index(v)%2 != 0 and v not in v2:
            v2.append(v)

    print("V1: ", v1)
    print('V2: ', v2)
    return 1

if bipartite(walk) == 'is':
    if len(walk) > 0:
        bipartite_rendering(walk)
    else:
        bipartite_rendering(vertices)


