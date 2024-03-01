class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k = k%length
        if length > 1 :
            arr = []
            for i in range(length-k, length): arr.append(nums[i])
            for i in range(length-k): arr.append(nums[i])
            nums[:] = arr[:]
        