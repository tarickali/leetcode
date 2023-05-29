"""
title : 0547_number_of_provinces.py
create : @tarickali 23/05/29
update : @tarickali 23/05/29
"""

from queue import Queue


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        def search(s: int):
            q = Queue()
            q.put(s)

            while not q.empty():
                x = q.get()
                seen.add(x)
                for y in graph[x]:
                    if y in seen:
                        continue
                    q.put(y)

        graph = {
            i: [
                k
                for k in range(len(isConnected[i]))
                if k != i and isConnected[i][k] == 1
            ]
            for i in range(len(isConnected))
        }
        seen = set()

        provinces = 0
        for i in range(len(isConnected)):
            if i in seen:
                continue
            search(i)
            provinces += 1
        return provinces
