class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        list = [0 for i in range(3)]
        for i in range(len(nums)): # O(n)
            list[nums[i]] += 1
        idx = 0
        for i in range(3):
            for j in range(list[i]):
                nums[idx] = i
                idx += 1