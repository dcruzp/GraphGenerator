
from os import close
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


#g = generate(5,3) 

#g.printGraph()

import os 

def generateFolderofGraph (name , ngraph):
    
    path = os.path.join(os.getcwd(), name)
    if os.path.exists(path):
        print (path + ' already exist')
    else :
        os.makedirs(path)

    file , ext  = "graph" , "txt"

    i = 1 
    while (i <= ngraph ):
        path = os.path.join (path , file + str (i) + '.'  + ext)
        print (path) 
        baconFile = open (path , 'w')
        baconFile.close() 
        path = os.path.dirname (path) 
        i = i +1 

    
    

foldername = "graph"
generateFolderofGraph (foldername , 100 ) 


def clearFolder (folder):
    for folderName ,subFolders , fileNames  in os.walk(os.getcwd()):
        if os.path.basename (folderName ) == folder :
            #print ('The current Folder is : '  + folderName ) 

            for fileName in fileNames :
                if fileName.endswith('.txt'):
                    fullpath = os.path.join(folderName , fileName)
                    print('deleted :' +  fullpath)
                    os.unlink(fullpath)
                    
            #print ("ES AQUI _______________________________________________________")

        #for subFolder in subFolders : 
        #    print ('SUBFOLDER OF : ' + folderName + ' : ' + subFolder)

        #for fileName in fileNames: 
        #    print ('FILE INSIDE ' + folderName + ': ' + fileName)
        
        #print (' ') 

clearFolder ('graph') 
       