"""
Using Sieve of Eratosthenes
i를 iterate하면서 n 전까지 i값들의 배수들을 filter하는게 포인트
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        #Since 0, 1 are not a prime number, set those to False meanwhile set True for all
        numbers = [False, False] + [True]*(n-2) #numbers[0], numbers[1]을 False로 초기화하고 나머지는 True로 initiate

        #We care about multiple numbers from 2 to sqrt of n
        for i in range(2, int(sqrt(n)) + 1):
            if numbers[i]:  #IMPORTANT, we don't consider False set values when iterating (this reduces processing time)
                for multiple in range(i**2, n, i):  #if True numbers were multiple of "multiple" variable, set it False to filter out
                    numbers[multiple] = False
        return sum(numbers)     #sum those True numbers which are prime numbers