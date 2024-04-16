class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = set(nums1)
        b = set(nums2)
        s = a & b # 교집합
        ans = []
        for num in s:
            count = min(nums1.count(num), nums2.count(num))
            ans.extend([num] * count) # 개수를 세서 그만큼 배열에 추가

        return ans