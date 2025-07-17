"""
원래 단순하게 nested loop를 만들어 각 인덱스마다 나머지 element와 비교하였으나 
test set의 크기가 커질수록 비효율적인 O(n^2)의 time complex를 보임
각 price마다 최소 price를 산출하여, 각 element들과 차이값을 profit으로 정해 max_profit을 업데이트하고
앞에 나올 element중에 더 작은값이 있다면 min을 사용하여 min_price를 업데이트하여 max_profit을 찾는다.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0          
        min_price = prices[0]   #min_price는 제일 처음의 prices값

        for price in prices:    #각 element를 순회
            max_profit = max(price - min_price, max_profit) #가장 큰 profit은 현재 element에서 min_price를 뺀값
            min_price = min(price, min_price)               # min_price는 순회하면서 만난 더 작은값
        return max_profit