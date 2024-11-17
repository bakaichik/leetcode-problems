import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_capital = []
        max_profit = []
        for i in range(len(capital)):
            heapq.heappush(min_capital, (capital[i], profits[i]))

        for _ in range(k):
            while min_capital and min_capital[0][0] <= w:
                c, p = heapq.heappop(min_capital)
                heapq.heappush(max_profit, -p)

            if not max_profit:
                break

            w += -heapq.heappop(max_profit)

        return w

solution = Solution()

print(solution.findMaximizedCapital(1, 0, [1, 1, 1], [0, 1, 1]))
