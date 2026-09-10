class Graph:
    def __init__(self, vertices):  # takes imput as per number of the vertices
        self.vertices = vertices

    # create a matrix
        self.matrix = [[0] * vertices for _ in range(vertices)]
        # matrix=[[]] #for o(n)
        #  for in range (len(vertices)):
        #     for j in range(len(vertices))
        #         matrix[i][j]=0

    def display(self):
        print("\nAdjacency matrix")
        for row in self.matrix:
            print(row)

    def add_edge(self, vertex1, vertex2):
        self.matrix[vertex1][vertex2] = 1


graph = Graph(5)

graph.add_edge(0, 1)
graph.add_edge(0, 3)
graph.add_edge(0, 2)
graph.add_edge(1, 0)
graph.add_edge(1, 4)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 0)
graph.add_edge(3, 2)
graph.add_edge(3, 4)
graph.add_edge(4, 1)

graph.display()

# edges = int (input("enter the number of the edges"))

# for i in range(edges):
#     v1,v2 = map(int, input("enter the edge(u v)").split())
#     graph.add_edge(v1,v2)
