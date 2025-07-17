"""
Given an integer array nums, find the 
subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

nums 리스트에서 loop를 활용해 iterate를 하는데
dp 라는 누적합의 리스트를 따로만든다.
nums[i]를 읽을때
nums[i-1] + nums[i]가 nums[i]보다 큰 경우, 새로운 누적합을 갱신하고
nums[i-1] + nums[i]가 nums[i]보다 작을 경우, 기존 누적합을 이어간다
                ________
nums = [-2,1,-3,4,-1,2,1,-5,4]
1. dp[0] = -2
2. dp[1] = 1
3. dp[2] = -2
4. dp[3] = 4
5. dp[4] = 3
6. dp[5] = 5
7. dp[6] = 6  <-- 최대 subarray값 dp[6]에는 4, -1, 2, 1 의 합이 들어있음
8. dp[7] = 1
9. dp[8] = 5
"""

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range (1, len(nums)):
      dp[i] = max(nums[i], dp[i-1] + nums[i]) #nums[i]는 새로운 nums element값, dp[i-1]+nums[i]는 누적합과 새로운 nums element를 더한 누적합값
    return max(dp)                            #dp 중에서 가장 큰 element를 반환하는 max함수 파이썬은 이런식으로 가능한건가..