# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
        2 -> 4 -> 3
+       5 -> 6 -> 4
-------------------
        7 -> 0 -> 8
carry:  0    1    0


        9 -> 9 -> 9 -> 9 -> 9 -> 9 -> 9
+       9 -> 9 -> 9 -> 9
    ----------------------------------- extended node
        8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1
carry:  1    1    1    1    1    1    1    0

"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      node = dummy = ListNode(-1)
      carry = 0

      while l1 and l2:                                       #l1, l2 둘다 길이가 맞는 부분까지만
        carry, digit = divmod(l1.val + l2.val + carry, 10)  #divmod로 몫과 나머지를 동시에 산출 각각 carry와 digit에 할당
        node.next = ListNode(digit)                         #결과노드를 연장하여 다음으로
        l1, l2, node = l1.next, l2.next, node.next          #l1, l2, 결과 노드들 모두 다음으로 이동
      
      #링트리스트의 길이가 균형하지 않을때 어느쪽이든 더 긴 리스트가 l로 할당
      l = l1 or l2
      while l:                                              #더 긴 리스트 기준
        carry, digit = divmod(l.val + carry, 10)            
        node.next = ListNode(digit)
        l, node = l.next, node.next
        
      if carry:                                             #두 링트리스트가 끝에 다다랐는데 캐리값이 남아있을경우
        node.next = ListNode(carry)                         #캐리값을 위한 노드 하나 연장
      return dummy.next                                          #더미노드 다음부터 차례로 반환 (결과값이 역순으로 나옴)
