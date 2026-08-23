class Solution:
    def maxProfit(self, prices: List[int]):
        
        curr_profit=0
        max_profit=0
        i=j=0
        while j<len(prices):
            if prices[j]>prices[i]:
                curr_profit=prices[j]-prices[i]
                max_profit=max(max_profit,curr_profit)
            else:
                i=j
            j+=1
        return max_profit 





