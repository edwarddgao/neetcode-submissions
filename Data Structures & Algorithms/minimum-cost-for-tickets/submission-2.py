from bisect import bisect_left
from functools import cache

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def rec(i):
            if i >= len(days):
                return 0
            return min(
                costs[0] + rec(i + 1),
                costs[1] + rec(bisect_left(days, days[i] + 7)),
                costs[2] + rec(bisect_left(days, days[i] + 30))
            )
        
        return rec(0)