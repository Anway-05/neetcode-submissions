class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        i,j=0,1
        while j<len(prices):
            profit=prices[j]-prices[i]
            max_profit=max(max_profit,profit)
            if prices[j]<prices[i]:
                i=j
            j+=1
        return max_profit
        