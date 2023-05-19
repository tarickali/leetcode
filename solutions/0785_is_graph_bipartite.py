"""
title : 0785_is_graph_bipartite.py
create : @tarickali 23/05/19
update : @tarickali 23/05/19
"""


class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        from queue import Queue

        explored = set()

        def bfs_color(s: int) -> bool:
            nonlocal explored

            q = Queue()
            colors = {}

            q.put(s)
            colors[s] = True

            while not q.empty():
                x = q.get()
                for y in graph[x]:
                    if y in explored:
                        if colors[x] == colors[y]:
                            return False
                    else:
                        q.put(y)
                        colors[y] = not colors[x]
                        explored.add(y)
            return True

        for x, ys in enumerate(graph):
            if x in explored:
                continue
            if not bfs_color(x):
                return False
        return True
