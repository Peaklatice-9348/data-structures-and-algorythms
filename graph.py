class Graph():
    def __init__(self,max):
        self.max = max
        self.list = []
        for i in range(max):
            node = []
            self.list.append(node)
    
    def add_edges(self,starting_node,ending_node):
        if ending_node in self.list[starting_node()]:
            return
        
        else:
            self.list[starting_node].append(ending_node)
            self.list[ending_node].append(starting_node)
    
graph = Graph(4)
graph.add_edges(1,2)
graph.add_edges(2,3)
graph.add_edges(3,1)
graph.add_edges(4,3)

print(graph.list)



    