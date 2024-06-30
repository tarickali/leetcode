"""
title : 1535_find_the_winner_of_an_array_game.py
create : @tarickali 23/11/04
update : @tarickali 23/11/04
"""

from collections import deque


class Solution:
    def getWinner(self, players: list[int], k: int) -> int:
        if k == 1:
            return max(players[0], players[1])
        if k >= len(players):
            return max(players)

        players = deque(players)

        a = players.popleft()
        b = players.popleft()
        champion = max(a, b)

        win_cnt = 0
        while win_cnt < k:
            if a > b:
                winner = a
                players.append(b)
                b = players.popleft()
            else:
                winner = b
                players.append(a)
                a = players.popleft()

            if winner == champion:
                win_cnt += 1
            else:
                champion = winner
                win_cnt = 1

        return champion
