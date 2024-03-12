# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans =[]

        def foo(cur):
            if cur.left is not None: foo(cur.left) # 왼쪽 노드
            ans.append(cur.val) # 배열에 저장
            if cur.right is not None: foo(cur.right) # 오른쪽 노드
        
        if root is not None:
            foo(root)
        
        return ans