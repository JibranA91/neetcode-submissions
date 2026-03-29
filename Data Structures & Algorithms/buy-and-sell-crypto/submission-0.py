class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = [prices[0]]
        max_price = [prices[-1]]

        for p,q in zip(prices,prices[::-1]):
            min_price.append(min(p,min_price[-1]))
            max_price.append(max(q,max_price[-1]))
        
        max_price = max_price[::-1]
        
        return max(0, max([j-i for i,j in zip(min_price, max_price)]))