# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        first = head
        second = None
        while first:
            dummy = first.next # 임시 저장
            first.next = second # 이전 노드와 연결
            second = first # 다음 노드로 이동
            first = dummy # 다음 노드로 이동
        return second # first는 None, 뒤집힌 노드의 head는 second
        