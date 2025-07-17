class Solution:
    def findMissingRanges(self, nums: List[int], lower:int, upper:int) -> List[List[int]]:
        res = []

        if not nums:                        #비어있는 list의 경우
            res.append([lower, upper])      #return 형태가 list의 list이기 때문에 [] 하나 더 씌워줘서 append
            return res
        
        if nums[0] > lower:                 #lower의 값이 첫번째 element보다 작을경우 그 전 range도 append
            res.append([lower, nums[0] - 1])

        for i in range(0, len(nums) - 1):   #바로 다음 element-1보다 현재 element가 작을 경우 element의 값 +1부터 
            if nums[i+1] - 1 > nums[i]:     #다음 element의 값-1까지 append
                res.append([nums[i] + 1, nums[i+1] - 1])
        
        if nums[-1] < upper:                #upper의 값이 마지막 element보다 클 경우 마지막 element+1부터 upper까지 append
            res.append([nums[-1]+1, upper])
        
        return res