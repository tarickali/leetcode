"""
title : 1235_maximum_profit_in_job_scheduling.py
create : @tarickali 24/01/06
update : @tarickali 24/01/06
"""

import heapq


class Solution:
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:
        heap = []
        curr, best = 0, 0
        for s, e, p in sorted(zip(startTime, endTime, profit)):
            while heap and heap[0][0] <= s:
                curr = max(curr, heapq.heappop(heap)[1])
            heapq.heappush(heap, (e, curr + p))
            best = max(best, curr + p)
        return best
