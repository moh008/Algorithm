"""
배열내에서 두 원소의 합이 k보다 작지만 가장 큰 합을 구하는문제
정렬을 한다면 nlog(n)으로 해결 가능
n 은 정렬때문에 log(n)은 left right 포인터가 각각 중앙을 향해가므로(binary search)
"""
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        max_sum = -1
        while left < right:
            if nums[left] + nums[right] < k:
                max_sum = max(nums[left] + nums[right], max_sum)
                left += 1
            else:
                right -= 1
        return max_sum