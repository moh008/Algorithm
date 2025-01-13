"""
    nums = [2,  7,   11,   15] target = 9
indicies = {2:0 7:1  11:2  15:3}
enumerate(nums)로 indicies 맵에 인덱스와 value를 pair로 저장
"""

class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        #dictionary에 nums의 값과 인덱스를 저장
        indicies = {}
        for i, v in enumerate(nums):
            indicies[v] = i
        #dictionary에서 target - nums[i] 찾기
        for i,v in enumerate(nums):
            diff = target - v           #9 - 2 = 7
            if diff in indicies and indicies[diff] != i: #indicies map에 diff값인 7이 있는가? {2:0, "7:1", 11:2, 15:3} 7:1이 있음
                j = indices[diff]       #indicies[7] 값, 즉 nums array안에 7의 인덱스값을 j에 할당
                return [i, j]           #2의 인덱스값 1과 j(nums 7의 인덱스값 2) 즉 [1,2]가 리턴됨
                                        #마지막에 주의할점은 i 와 j가 같으면 안되므로, indicies[diff] != i 조건문을 추가해줘야함
                                        #ex) nums[3, 2, 4] target = 6 일때 [0, 0] 즉 3+3 = 6 으로 리턴될 수 있음