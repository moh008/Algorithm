#이게 왜 하드야
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()
        if len(nums1) % 2 == 0:
            pre = nums1[(len(nums1) // 2) - 1]
            post = nums1[(len(nums1) // 2)]
            return ((pre + post) / 2)
        else:
            return nums1[(len(nums1) // 2)]
