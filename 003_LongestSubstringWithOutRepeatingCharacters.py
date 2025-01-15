"""
Sliding Window 방법을 쓴다 
중복을 허용치 않는 set을 선언, start pointer와 end pointer가 s의 원소들을 하나씩 스캔해가며
1. end pointer가 가르키는 새 원소가 기존 set에 들어있지 않으면 
    end pointer가 가르키고 있던 element를 set에 넣고 end pointer를 하나 증가
2. end pointer가 가르키는 새 원소가 기존 set에 들어있다면, 
    start pointer가 가르키고 있던 element를 set에서 빼고 start pointer를 하나 증가
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start, end = 0, 0
        chars = set()
        while end < len(s):
            if s[end] in chars:
                chars.remove(s[start])
                start += 1
            else:
                chars.add(s[end])
                max_len = max(end - start + 1, max_len)
                end += 1                
        return max_len
