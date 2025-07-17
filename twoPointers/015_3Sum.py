"""
3 element의 합이 0인 3 element 조합들을 리턴
먼저 정렬을 하여 합이 0보다 클땐 right pointer를 왼쪽으로, 합이 0보다 작을땐 left 포인터를 오른쪽으로 이동
같을땐 각 element들을 list로 합쳐서 append하며 left pointer를 오른쪽으로 이동 (물론 left < right 일때만)
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()                                                 #정렬
        result = []                                                 #빈 리스트
        for i in range(n-2):                                        #i는 마지막 element-2까지만 증가
            if i > 0 and nums[i] == nums[i - 1]:                    #두번쨰 element가 첫번째 element와 같을때
                continue                                            #두번째 process는 생략
            left = i + 1                                            #left, right pointer 세팅
            right = n - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:     #합이 0보다 클땐 정렬된 list이므로 right pointer 왼쪽으로
                    right -= 1  
                elif sum < 0:   #합이 0보다 작을땐 left pointer 오른쪽으로
                    left += 1
                else:           #합이 0 일때 3개 element들을 리스트로 append
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1   #역시 left pointer를 오른쪽으로
                    while nums[left] == nums[left-1] and left < right:
                        left += 1   #만약 움직인 pointer가 가리키는 element가 또 같은값일때 한칸더 오른쪽으로, 물론 left<right일때만
        return result