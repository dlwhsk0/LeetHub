class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in nums: # O(n)
            if i not in dic: dic[i] = True
            else: return True
        return False