from bfs import BFS
from romenia_map import ROMENIA

bfs = BFS(ROMENIA, start='Arad')
print bfs.search('Bucharest') == 'Bucharest'