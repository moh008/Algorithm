"""
추가적인 메모리를 사용하지 않고, 리스트 내부에서 값만 바꿔서 unique한 element의 개수만 리턴
문제가 좀 이상함
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j