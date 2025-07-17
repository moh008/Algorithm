"""
문자열 처음부터 loop으로 인덱스 중심으로 start 와 end포인터를 지정하며 
만약 str[start], str[end]가 같지않다면 인덱스를 하나씩 오른쪽으로 이동한다

        여보안경안보여
start   0
        
end                6
        
max_start = 0
max_end   = 6

인덱스 중심부터 start, end를 지정하여 start - 1, end + 1로 포인터를 확장해나감
물론 start가 왼쪽으로 확장해나가는 범위는 0보다 같거나 커야함, 마찬가지로 end는 문자열의 최대길이- 1 까지만 확장돼야함
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_start, max_end = 0, 0
        
        for i in range(len(s)):
            start, end = i, i
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if max_end - max_start < end - start:
                    max_start, max_end = start, end
                start, end = start - 1, end + 1
            
            start, end = i, i + 1                                     #연속된 짝수개의 문자가 palindrome 일때 
            while start >= 0 and end < len(s) and s[start] == s[end]: #로직은 위와 같음
                if max_end - max_start < end - start:
                    max_start, max_end = start, end
                start, end = start - 1, end + 1
        return s[max_start : max_end + 1] #파이썬 substring 로직, s[max_start]부터 s[max_end-1]까지 떼오기때문에 max_end + 1을 해야 max_end 인덱스 글자까지 따옴