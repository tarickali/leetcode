"""
title : 0933_number_of_recent_calls.py
create : @tarickali 23/05/16
update : @tarickali 23/05/16
"""


class RecentCounter:
    def __init__(self):
        self.stack = []

    def ping(self, t: int) -> int:
        self.stack.append(t)
        k = 1
        while k <= len(self.stack):
            if not (t - 3000 <= self.stack[-k] <= t):
                break
            k += 1
        return k - 1


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
