class Graph:
    def __init__(self):
        self.adjancey_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjancey_list.keys():
            self.adjancey_list[vertex] = []
            return True
        return False

    def add_edge(self,vertex1, vertex2):
        if vertex1 in self.adjancey_list.keys() and vertex2 in self.adjancey_list.keys():
            self.adjancey_list[vertex1].append(vertex2)
        
        

# display graph
    def display_graph(self):
        for vertex in self.adjancey_list.keys():
            print(vertex, ":", self.adjancey_list[vertex])


graph = Graph()
# pass the numbr of the vertex
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')


graph.add_edge('A','B') 
graph.add_edge('A','C')     
graph.add_edge('A','D')
graph.add_edge('B','A')
graph.add_edge('B','E')
graph.add_edge('C','A')
graph.add_edge('C','D')
graph.add_edge('D','A')
graph.add_edge('D','E')
graph.add_edge('D','C')
graph.add_edge('E','D')
graph.add_edge('E','B')




graph.display_graph()
