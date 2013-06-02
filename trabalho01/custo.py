from operator import itemgetter

class CustoSearch(object):
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.costs = []

    def pop(self):
        return self.costs.pop(0)[0]

    def queue(self, node):
        self.costs.append(node)

    def neighbours(self, node):
        return self.graph[node].items()

    def sort_costs(self):
        sorted(self.costs, key=itemgetter(1))

    def initial_status(self):
        for node in self.neighbours(self.start):
            self.queue(node)
        self.sort_costs()

    def search(self, target):
        self.initial_status()
        while self.costs:
            current = self.pop()
            if current == target:
                return current
            for node in self.neighbours(current):
                self.queue(node)
            self.sort_costs()
        return '%s Not Found' % target