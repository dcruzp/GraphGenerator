# Graph Generator

### Idea del Proyecto

    Es hacer un generador de grafos usando python como lenguaje de programacion 

#### Lenguage

    * python 

#### Desciption

* ### Files

    *  graph.py
        * represnt a graph instance 

    * graphGenerator.py
        * aqui hay varias funciones para crear un grafo pero existe una funcion que le pasas un conjunto de parametros y esta te crea una carpeta con una secuencia de grafos 

        * #### Parametros:
            + 1 - foldername
            + 2 - numberofGraph
            + 3 - limitofVertex
            + 4 - namefile
            + 5 - ext

        * #### Descripcion de los parametros 
            + 1- foldername
                + el nombre de la carpeta que quieres crear para guardar los grafos que vas a generar 
            + 2 -numberofGraph
                + La cantidad de grafos aleatorios que quieres generar 
            + 3 -limitofVertex
                + la cantidad maxima de vertices que puede tener un grafo generado por este metodo 
            + 4 - namefile
                + el nombre que quieres darle a los grafos que vas a generar dento de la carpeta -foldername-
                (aqui aclarar que esto lo que constituye el encabezado del nombre de los ficheros que contienen los grafos )
            +  5 - ext
                + la extencion con que se quieren guardar los fichero que contienen lo grafos 

* ### Ejemplo
    - Si llamamo a la fucion de la siguiente manera:
        + generateFolderofRandomGraph ('graph' , 10 , 10 , 'graph' , 'tex' ) 
        
        Se va a crear una carpeta en el directorio actual (donde se esta corriendo el .py ) y dentro va a contener 10 ficheros que dentro tienen la descripcion de un grafo

        Lo s nombre de los ficheros van a tener el siguiente formato:
        + graph + "numerodelgrafo" + .txt
    
* ### Nota 
    * La estuctura que van a tener los ficheros es la siguiente: 
        * 1ra linea (dos enteros ) n,m . el numero de vertices y el numero de aristas respectivamente 
        * restante lineas (descricion de las aristas del grafo ) 
            + por ejemplo si la arista i--j existe entonces una de esas lineas que estan en el fichero va a ser "i - j" separadas por un espacio 
    
#### link

* https://github.com/dcruzp/GraphGenerator