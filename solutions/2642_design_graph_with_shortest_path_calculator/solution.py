"""
title : 2642_design_graph_with_shortest_path_calculator.py
create : @tarickali 23/11/12
update : @tarickali 23/11/12
"""

import heapq
from collections import defaultdict


class Graph:
    def __init__(self, n: int, edges: list[list[int]]):
        self.nodes = set(range(n))
        self.graph = defaultdict(dict)
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: list[int]) -> None:
        u, v, c = edge
        self.graph[u][v] = c

    def shortestPath(self, node1: int, node2: int) -> int:
        maxint = int(10e6 + 1)
        dist = {}
        explored = set()
        for node in self.nodes:
            dist[node] = maxint
        dist[node1] = 0
        heap = [(c, u) for u, c in dist.items()]
        heapq.heapify(heap)

        while len(heap) != 0:
            c, u = heapq.heappop(heap)
            explored.add(u)

            for v in self.graph[u]:
                if v in explored:
                    continue
                alt = dist[u] + self.graph[u][v]
                if alt < dist[v]:
                    dist[v] = alt
            heap = [(c, u) for u, c in dist.items() if u not in explored]
            heapq.heapify(heap)

        return -1 if dist[node2] == maxint else dist[node2]
