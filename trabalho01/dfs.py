class DFS(object):
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.stack = []
        self.visited = dict((e, False) for e in graph) # no node visited yet

    def push(self, node):
        self.stack.append(node)

    def pop(self):
        return self.stack.pop()

    def node_not_visited(self, node):
        return not self.visited[node]

    def neighbours(self, node):
        return self.graph[node]

    def visit(self, node):
        self.visited[node] = True

    def search(self, target):
        self.push(self.start)
        while self.stack:
            node = self.pop()
            if node == target:
                return node
            if self.node_not_visited(node):
                self.visit(node)
                for unvisited in self.neighbours(node):
                    self.push(unvisited)
        return '%s Not Found' % target
