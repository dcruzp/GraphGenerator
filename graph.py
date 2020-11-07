# 
# File defines Vertex and Graph Objects
# 

class Vertex (object):    # Represents a vertex and its neighbors
    
    def __init__(self, n):
        self.name = n
        self.neighbors = []  # list of neighbor vertices

    # this adds neighbors to our vertex
    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()
            return True
        return False


class Graph (object):
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex):
            self.vertices[vertex.name] = vertex
            return True
        return False

    def add_edge(self, u, v):  # adds an edge/connection between vertices
        if u in self.vertices and v in self.vertices:
            return self.vertices[u].add_neighbor(v) and self.vertices[v].add_neighbor(u)
        return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(str(key) + ' ' + str(self.vertices[key].neighbors))


if __name__ == '__main__':
    g = Graph()

    for i in range(1, 6):
        g.add_vertex(Vertex(i))

    borders = ['53', '54', '31', '35', '41',
              '42', '45', '12', '13', '14', '21', '24']

    for b in borders:
        g.add_edge(int(b[:1]), int(b[1:]))

    g.print_graph()
