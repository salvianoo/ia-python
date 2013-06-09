class DFS(object):
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.stack = []
        self.path = []
        self.visited = dict((e, False) for e in graph)

    def get_path(self):
        return self.path

    def cost(self):
        return len(self.path)

    def search(self, target):
        self._push(self.start)
        while self.stack:
            node = self._pop()
            if node == target:
                return node
            if self._node_not_visited(node):
                self._visit(node)
                self._add_path(node)
                for unvisited in self._neighbours(node):
                    self._push(unvisited)
        return '%s Not Found' % target

    def _push(self, node):
        self.stack.append(node)

    def _pop(self):
        return self.stack.pop()

    def _add_path(self, node):
        self.path.append(node)

    def _node_not_visited(self, node):
        return not self.visited[node]

    def _neighbours(self, node):
        return self.graph[node]

    def _visit(self, node):
        self.visited[node] = True
