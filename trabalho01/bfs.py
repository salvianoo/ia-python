class BFS(object):
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.visited = []

    def next_node(self):
        return self.visited.pop(0)

    def node_not_explored(self, node):
        return node not in self.visited

    def queue(self, node):
        self.visited.append(node)

    def neighbours(self, node):
        return self.graph[node]

    def search(self, target):
        self.queue(self.start)
        while self.visited:
            node_explored = self.next_node()
            if node_explored == target:
                return node_explored
            for node in self.neighbours(node_explored):
                if self.node_not_explored:
                    self.queue(node)
        return '%s Not Found' % target
