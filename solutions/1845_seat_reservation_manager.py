"""
title : 1845_seat_reservation_manager.py
create : @tarickali 23/11/05
update : @tarickali 23/11/05
"""

import heapq


class SeatManager:
    def __init__(self, n: int):
        self.last = 1
        self.heap = []

    def reserve(self) -> int:
        seat = None
        if self.heap != []:
            seat = heapq.heappop(self.heap)
        else:
            seat = self.last
            self.last += 1
        return seat

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
