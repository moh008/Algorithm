"""
두 링크드리스트를 더한다.
002와 비슷하지만 이번엔 Most Significant number가 제일 왼쪽으로옴
그래서 차라리 쉽게 LinkedList의 값들을 각자 int에 넣고, 그냥 더한다
그리고 string으로 바꿔서 길이값을 구한뒤, 하나씩 linkedlist에 넣는다. 끝
"""
class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        node = dummy = ListNode(-1)
        n1 = n2 = 0
        while l1:   #n1에 값을 넣으려는 방법은 가장 첫번쨰 LinkedList에서 val 넣어주고, 다음엔 10곱한뒤 두번쨰 노드를 더해주고 반복
            n1 = n1*10 + l1.val
            l1 = l1.next
        while l2:
            n2 = n2*10 + l2.val
            l2 = l2.next
        
        x = n1 + n2
        length = len(str(x))

        while length > 0:
            node.next = ListNode(x // 10**(length-1))   #새로운 LinkedList에 몫을 넣는다
            x %= 10**(length-1)                         #나머지만 챙기게두고 다음루프 준비
            length -= 1
            node = node.next                            #현재 노드값을 넣었다면 다음노드로 포인터 이동
        return dummy.next