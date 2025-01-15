class Solution:
    def removeNthFromEnd(self, head: ListNode, n:int) -> ListNode:
        dummy = ListNode(0, head) #node의 val은 0, next pointer는 head로 초기화
        
        left, right = dummy, head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        #delete the nth node
        left.next = left.next.next #현재 노드의 next 노드로 가서 그 노드의 next포인터에 접근할떄 .next.next를 씀
        
        return dummy.next