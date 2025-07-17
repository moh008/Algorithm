"""
Medium 이었는데 사실은 훼이크였음
담날 내려가면 어차피 안사니까 그냥 profit을 누적방식으로 당장 전날보다 올라갔다면 더해주면 끝남
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_Profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_Profit += prices[i] - prices[i - 1]
        return max_Profit