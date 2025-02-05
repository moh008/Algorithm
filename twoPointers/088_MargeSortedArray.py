"""
Two Pointers 문제
더 긴 nums1의 배열에서 가장 마지막 element에 접근하는 포인터 last 를 설정, 두 list 중 마지막 element끼리 비교하여
num1[last]에 넣는다. 그리고나서 last pointer와 넣게된 각 list들의 포인터들을 하나씩 차감한다.
마지막에는 만약 nums2 리스트에 nums1 list에 넣을 element가 남아있다면 남은 개수만큼 넣어주고 마무리
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = m + n - 1
        while m > 0 and n > 0:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[last] = nums2[n - 1]
                n -= 1
            else:
                nums1[last] = nums1[m - 1]
                m -= 1
            last -= 1
        while n > 0:
            nums1[last] = nums2[n - 1]
            last, n = last - 1, n - 1