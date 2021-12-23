class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        bought = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            profit = prices[i] - bought
            
            if profit > max_profit:
                max_profit = profit
                
            if bought > prices[i]:
                bought = prices[i]
                
        return max_profit
