# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = l1.val + l2.val
        ans = ListNode(temp%10)
        flag = int(temp/10)
        cur1 = l1.next
        cur2 = l2.next
        cur = ans

        while cur1 or cur2: # O(n)
            num1 = cur1.val if cur1 else 0
            num2 = cur2.val if cur2 else 0
            temp = num1 + num2 + flag
            flag = int(temp/10)
            cur.next = ListNode(temp%10)
            cur = cur.next
            if cur1: cur1 = cur1.next
            if cur2: cur2 = cur2.next
        
        if flag: cur.next = ListNode(1)

        return ans