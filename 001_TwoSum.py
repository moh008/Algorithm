"""
two pointer(?), hashmap
hash_map에 num[i]의 값과 인덱스를 저장한뒤, hash_map에서 nums[i] 인덱스값을 리턴하는 방식
"""

class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        hash_map = {}
        n = len(nums)

        for i in range(n):
            if nums[i] in hash_map:
                return [hash_map[nums[i]], i] 
            else:   
                hash_map[target - nums[i]] = i