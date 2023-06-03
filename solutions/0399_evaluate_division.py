"""
title : 0399_evaluate_division.py
create : @tarickali 23/06/03
update : @tarickali 23/06/03
"""

from collections import defaultdict


class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val
            graph[u][u] = 1.0
            graph[v][v] = 1.0

        def traverse(u, v) -> float:
            seen = {u}
            stack = [u]
            vals = {u: 1.0}

            while len(stack) != 0:
                x = stack.pop()

                for y in graph[x]:
                    if y in seen:
                        continue
                    stack.append(y)
                    seen.add(x)
                    vals[y] = vals[x] * graph[x][y]

            return vals.get(v, -1)

        results = []
        for u, v in queries:
            if u not in graph or v not in graph:
                results.append(-1.0)
            else:
                results.append(traverse(u, v))
        return results
