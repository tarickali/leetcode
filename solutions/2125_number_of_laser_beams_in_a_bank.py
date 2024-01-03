"""
title : 2125_number_of_laser_beams_in_a_bank.py
create : @tarickali 24/01/02
update : @tarickali 24/01/02
"""


class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        devices = [sum(int(c) for c in row) for row in bank]
        beams, prev, curr = 0, 0, 1
        while curr < len(devices):
            if devices[curr] > 0:
                beams += devices[curr] * devices[prev]
                prev = curr
            curr += 1

        return beams
