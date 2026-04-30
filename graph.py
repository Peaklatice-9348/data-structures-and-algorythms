class Graph():
    def __init__(self,max):
        self.max = max
        self.list = []
        for i in range(max):
            node = []
            self.list.append(node)
    
    def add_edges(self,starting_node,ending_node):   
        self.list[starting_node-1].append(ending_node)
        self.list[ending_node-1].append(starting_node)
            
    def bfs(self,source_node):
        visited = [False,False,False,False]
        queue = [source_node]
        result = []
        visited[source_node-1] = True
        while len(queue) > 0:
            s = queue[0]
            queue.pop(0)
            result.append(s) 
            for node in self.list[s-1]:
                if visited[node-1] == False:
                    queue.append(node)
                    visited[node-1] = True
        return result


graph = Graph(4)
graph.add_edges(1,2)
graph.add_edges(2,3)
graph.add_edges(3,1)
graph.add_edges(4,3)
print(graph.bfs(1))
print(graph.list)



    