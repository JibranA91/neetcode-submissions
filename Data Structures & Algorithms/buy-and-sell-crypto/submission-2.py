class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        import numpy as np
        min_price = [prices[0]]
        max_price = [prices[-1]]

        for i,j in zip(prices, prices[::-1]):
            min_price.append(min(i, min_price[-1]))
            max_price.append(max(j, max_price[-1]))
        
        max_price = max_price[::-1]

        return max(max([j-i for i,j in zip(min_price, max_price)]), 0)