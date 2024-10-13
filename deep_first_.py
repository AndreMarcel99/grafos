def get_information(path):
    #
    #
    return nodes, edges

class Nodes:

    def __init__(self, node):
        self.node = node
        self.visited = False

class Graph:

    def __init__(self, size):
        self.size = size
        self.stack = []
        self.top = -1
        self.lst_Nodes = [None] * size
        self.adj_Matrix = [[0] * size for _ in range(size)]
        self.node_Count = 0
        self.initialize_adjMatrix(size)

    def initialize_adjMatrix(self, size):
        for i in range(size):
            for j in range(size):
                self.adj_Matrix[i][j] = 0

    def push(self, item):
        self.top += 1
        self.stack.append(item)

    def pop(self):
        item = self.stack[self.top]
        del self.stack[self.top]
        self.top -= 1
        return item

    def peek(self):
        return self.stack[self.top]

    def is_Stack_Empty(self):
        return self.top == -1

    def add_Node(self, name):
        node = Nodes(name)
        self.lst_Nodes[self.node_Count] = node
        self.node_Count += 1

    def addEdge(self, start, end):
        self.adj_Matrix[start][end] = 1
        self.adj_Matrix[end][start] = 1

    def displayNode(self, node_index):
        print(self.lst_Nodes[node_index].node)

    def getAdjUnvisitedVertex(self, nodeIndex):
        for i in range(self.node_Count):
            if self.adj_Matrix[nodeIndex][i] == 1 and not self.lst_Nodes[i].visited:
                return i
        return -1

    def depthFirstSearch(self, number):
        self.lst_Nodes[number].visited = True
        self.displayNode(number)
        self.push(number)
        while not self.is_Stack_Empty():
            unvisitedVertex = self.getAdjUnvisitedVertex(self.peek())
            if unvisitedVertex == -1:
                self.pop()
            else:
                self.lst_Nodes[unvisitedVertex].visited = True
                self.displayNode(unvisitedVertex)
                self.push(unvisitedVertex)
        for i in range(len(self.lst_Nodes)):
            self.lst_Nodes[i].visited = False

def main():
    path = ""
    nodes, edges = get_information(path)
    total_nodes = len(nodes)
    new_edges = []
    for edge in edges:
        edge = tuple(map(int, edge.split(',')))
        new_edges.append(edge)

    graph = Graph(total_nodes)
    for i in nodes:
        graph.add_Node(i)

    for i in new_edges:
        graph.addEdge(i[0], i[1])

    graph.depthFirstSearch(49)

main()