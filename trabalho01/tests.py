import unittest
from romenia_map import ROMENIA
from bfs import BFS
from dfs import DFS
from custo import CustoSearch

class TestSearchAlgoritms(unittest.TestCase):
    def test_busca_em_profundidade_success(self):
        dfs = DFS(ROMENIA, start='Arad')
        self.assertEqual('Bucharest', dfs.search('Bucharest'))

    def test_busca_em_largura_success(self):
        bfs = BFS(ROMENIA, start='Arad')
        self.assertEqual('Bucharest', bfs.search('Bucharest'))

    def test_busca_de_custo_uniforme_success(self):
        custo = CustoSearch(ROMENIA, start='Arad')
        self.assertEqual('Bucharest', custo.search('Bucharest'))

if __name__ == '__main__':
    unittest.main()