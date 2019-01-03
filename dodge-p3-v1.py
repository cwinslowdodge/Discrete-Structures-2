#using Python 3

print('Please enter the vertices you would like in your set: ')
vertices = input().split(', ')
print('Please enter the relation on that set: ')
edges = input().split(', ')

#vertices = ['a','b','c','d']
#edges = ['(a,a)','(b,b)','(c,c)','(d,d)','(a,b)','(b,c)','(a,c)']

trans_edges = []
t_closure = []
for i in edges:
    if i[1] is not i[3]:
        trans_edges.append(i)

def reflexive(vertices, edges):
    reflexive_points = 0
    for vertex in vertices:

        for edge in edges:
            if edge[1] == vertex and edge[3] == vertex:
                reflexive_points += 1

    print('reflexive, ') if reflexive_points == len(vertices) else print('not reflexive, ')

    #if reflexive_points == len(vertices):
    #    print("reflexive")
    #else:
    #    print("not reflexive")

def symmetric(edges):
    symmetric_edges = 0
    not_loop = len(edges)

    for edge in edges:
        if edge[1] is edge[3]:
            not_loop-=1
    for edge1 in edges:
        for edge2 in edges:
            if edge1[1] is not edge1[3] and edge1[1] == edge2[3] and edge1[3] == edge2[1]:
                symmetric_edges+=1

    print("symmetric, ") if symmetric_edges == not_loop else print("not symmetric, ")

    #if symmetric_edges == not_loop:
    #    print("symmetric,")
    #else:
    #    print("not symmetric,")

def transitive(edges):
    n_trans = 0

    for edge1 in edges:

        for edge2 in edges:

            if edge1[3] == edge2[1] and edge1 is not edge2:

                for edge3 in edges:

                    if "(" + edge1[1] + "," + edge2[3] + ")" not in edges:
                        n_trans += 1

                    if edge3[1] == edge2[3] and (edge1 or edge2) is not edge3:

                        if edge1[1] == edge3[3]:
                            #n_trans += 1
                            t_closure.append("(" + edge3[1] + "," + edge1[3] + ")")
                            break

                    else:
                        t_closure.append("(" + edge1[1] + "," + edge2[3] + ")")



    print("not transitive") if n_trans > 0 else print("transitive")

    #print(t_closure)

    #if n_trans > 0:
    #    print("not transitive,")
    #else:
    #    print("transitive,")

def antisymmetric(edges):
    anti = 0
    for edge in edges:
        for edge1 in edges:
            if edge[1] == edge1[3] and edge[3] == edge1[1]:
                anti +=1

    print('not antisymmetric,') if anti > 0 else print('antisymmetric,')


def trans_closure():
    closure = []
    print(closure)



print("The set is ")
reflexive(vertices,edges)
symmetric(edges)
antisymmetric(trans_edges)
transitive(trans_edges)


t_closure = list(set(t_closure))
trans_edges = sorted(edges + t_closure)
trans_edges = sorted(list(set(trans_edges)))


print("Transitive closure: " + str(trans_edges))



