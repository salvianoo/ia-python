import unittest
from dfs import DFS
from romenia_map import ROMENIA

class TestDepthFirstSearch(unittest.TestCase):

    def setUp(self):
        self.dfs = DFS(ROMENIA, start='Arad')

    def test_dfs_search_success(self):
        self.assertEqual('Bucharest', self.dfs.search('Bucharest'))

    def test_dfs_search_failure(self):
        target = 'Catalao'
        self.assertEqual('{0} Not Found'.format(target), self.dfs.search(target))

    def test_get_path_success(self):
        path_expected = ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti',
                        'Craiova', 'Dobreta', 'Mehadia', 'Lugoj', 'Timisoara']
        self.dfs.search('Bucharest')
        self.assertEqual(path_expected, self.dfs.get_path())

    def test_get_cost_success(self):
        self.dfs.search('Bucharest')
        self.assertEqual(9, self.dfs.cost())


if __name__ == '__main__':
    unittest.main()
