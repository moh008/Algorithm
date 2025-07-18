"""
가장 긴 연속된 숫자들의 리스트의 길이를 반환하는 문제
특이하게도 소거법으로 시퀀스의 처음 원소를 찾아가는데 i-1이 없을 경우에만 작동을 시작함
이중루프이긴하나, 바로 다음 원소만을 스캔해서 연속하는지만 보기때문에(내부루프가 각 1회씩만 실행되기때문에) O(n)이라 볼수있음
천재아님?
"""

class Solution:
  def longestConsecutive(self, nums: List[int]) -> List[int]:
    #set으로 변환해서 중복된 원소는 제거
    num_set = set(nums)
    max_length = 0

    for i in num_set:
      #소거법: i - 1이 존재하지 않으면 길이를 1로 설정, 만약 i - 1 원소가 존재한다면 아무것도 하지않음 마치 연속되는 시퀀스의 처음 원소를 찾기위해 큰숫자는 전부 건너뛴다는 느낌
      if i - 1 not in num_set:
        length = 1
        #i + length가 존재할때마다 길이를 1 늘림
        while i + length in num_set:
          length += 1
        max_length = max(length, max_length)
    return max_length