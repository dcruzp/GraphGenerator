
import graph
import random 

def checkiscorrectGraph (n,m):
    return m <= (n*(n-1))/2

def generate (n , m ):
    
    g = graph.Graph() 

    if not checkiscorrectGraph(n,m):
        return g 

    listvert = range (1,n +1 ) 
    for i in listvert:
        g.addvertex(graph.Vertex(i))

    count = 0 

    while count < m:
        r = random.sample(listvert , 2)
        
        if g.addedge(r[0] , r[1]):
            count = count + 1 
            print(r)
        else:
            print(str (r) + " could not be added because it was already in the graph ")
    
    return g 


g = generate(5,3) 

g.printGraph()
