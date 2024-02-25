class Solution(object):
    def removeDuplicates(self, nums):
        s = set(nums)  #O(n)
        k = len(s)  #O(2n)

        a = list(s)  #O(3n)
        h = sorted(a)  #O(nlogN)
        nums[:] = h  #O(4n) 

        return k