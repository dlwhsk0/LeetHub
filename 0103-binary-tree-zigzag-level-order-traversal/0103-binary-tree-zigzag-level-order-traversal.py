# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        ans = []
        left = True
        if root:
            q.append(root)
            while q:
                arr = deque()
                size = len(q)
                for i in range(size):
                    cur = q.popleft()
                    if cur.left: q.append(cur.left)
                    if cur.right: q.append(cur.right)
                    if left: arr.append(cur.val)
                    else: arr.appendleft(cur.val)
                ans.append(arr)
                left = not left
        return ans