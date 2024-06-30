"""
title : 0841_keys_and_rooms.py
create : @tarickali 23/05/27
update : @tarickali 23/05/27
"""


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        seen = set()

        def recurse(i: int) -> None:
            if len(seen) == len(rooms) or i in seen:
                return
            seen.add(i)
            for j in rooms[i]:
                recurse(j)

        recurse(0)
        return len(seen) == len(rooms)
