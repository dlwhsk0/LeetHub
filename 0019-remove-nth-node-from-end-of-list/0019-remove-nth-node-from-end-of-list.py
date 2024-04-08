# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head
        # 두 노드 사이의 n만큼의 갭을 만듬
        for i in range(n): second = second.next
        # second가 none이면 가장 첫 번째 노드를 삭제해야함
        if not second: return head.next
        # second가 끝에 닿을 때까지 두 노드 이동
        while second.next:
            first = first.next
            second = second.next
        # 노드 삭제
        first.next = first.next.next
        return head