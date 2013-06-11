class BFS(object):
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.visited = []

    def search(self, target):
        self._queue(self.start)
        while self.visited:
            node_explored = self._next_node()
            if node_explored == target:
                return node_explored
            for node in self._neighbours(node_explored):
                if self._node_not_explored:
                    self._queue(node)
        return '%s Not Found' % target

    def _next_node(self):
        return self.visited.pop(0)

    def _node_not_explored(self, node):
        return node not in self.visited

    def _queue(self, node):
        self.visited.append(node)

    def _neighbours(self, node):
        return self.graph[node]
