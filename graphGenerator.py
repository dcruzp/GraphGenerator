
import os
import sys 
import graph
import random 


def checkiscorrectGraph (n,m):
    return m <= (n*(n-1))/2

def generateGraph (n , m ):
    
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
            #print(r)
        else:
            #print(str (r) + " could not be added because it was already in the graph ")
            continue 
    
    return g

def generateRandomGraph (limitofVertex):
    n = random.randint(1, limitofVertex)
    m = random.randint(0, (int)(n*(n-1)/2))
    g = generateGraph(n,m)
    print( str (n) + ' ' + str (m))
    for key in sorted(list(g.vertices.keys())):
            #print(str(key) + ' ' + str( g.vertices[key].neighbor ) )
            for neighbor in g.vertices[key].neighbor:
                print ( str(key) + ' '  + str (neighbor))
    #g.printGraph()
    return g


def generateFolderofRandomGraph (folder , ngraph , limitOfVertex , namefile = 'graph', ext = 'txt'):
    
    path = os.path.join(os.getcwd(), folder)
    if os.path.exists(path):
        print (path + ' already exist')
        return None 
    else :
        os.makedirs(path)

    i = 1 
    while (i <= ngraph ):
        n = random.randint(2,limitOfVertex)
        m = random.randint(1, (int)(n*(n-1)/2))
        g = generateGraph(n,m)
        path = os.path.join (path , namefile + str (i) + '.'  + ext)
        baconFile = open (path , 'w')
        baconFile.write (str(n) + ' ' + str (m) + '\n') 
        baconFile.close() 

        baconFile = open (path , 'a')
        for key in sorted(list(g.vertices.keys())):
            for neighbor in g.vertices[key].neighbor:
                baconFile.write(str(key) + ' '+ str (neighbor) + '\n')
        baconFile.close()
        path = os.path.dirname (path) 
        i = i +1 
 

#foldername = "graph"
#numberofgraph = 100
#numberofVertex = 100 
#generateFolderofRandomGraph (foldername , numberofgraph , numberofVertex ) 


def clearFolder (folder):
    for folderName ,subFolders , fileNames  in os.walk(os.getcwd()):
        if os.path.basename (folderName ) == folder :
            #print ('The current Folder is : '  + folderName ) 

            for fileName in fileNames :
                if fileName.endswith('.txt'):
                    fullpath = os.path.join(folderName , fileName)
                    print('deleted :' +  fullpath)
                    os.unlink(fullpath)


if __name__ == '__main__':

    foldername = 'graph' 
    numberofGraph = 10
    limitofVertex = 20
    namefile = 'graph' 
    ext = 'txt'

    argv = [foldername , numberofGraph , limitofVertex , namefile , ext]

    i =0 
    for item in sys.argv[1:] :
        print (item)

    #print (foldername) 
    #print (numberofGraph)
    #print (limitofVertex)
    #print (namefile)
    #print (ext) 


