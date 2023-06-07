"""
title : 2336_smallest_number_in_infinite_set.py
create : @tarickali 23/06/07
update : @tarickali 23/06/07
"""


class SmallestInfiniteSet:
    def __init__(self):
        self.minimum = 1
        self.removed = set()
        self.readded = set()

    def popSmallest(self) -> int:
        num = 0
        if len(self.readded) == 0:
            num = self.minimum
            self.removed.add(num)
            self.minimum += 1
        else:
            num = min(self.readded)
            self.readded.remove(num)
            self.removed.add(num)
        return num

    def addBack(self, num: int) -> None:
        if num not in self.removed:
            return
        self.removed.remove(num)
        self.readded.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
