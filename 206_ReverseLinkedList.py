class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            tmp = curr.next         #현재 노드의 next 포인터의 방향을 변수에 저장
            curr.next = prev        #현재 노드의 next 포인터의 방향을 이전 노드방향으로 변경
            prev = curr             #prev 노드의 포인터를 curr 노드 포인터로 assign.  prev노드 포인터는 curr노드 포인터가 되고,
            curr = tmp              #curr 포인터는 tmp에 저장된 next 포인터의 방향이 됨
        return prev