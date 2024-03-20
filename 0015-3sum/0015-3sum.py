class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) < 3: return res
        else: 
            nums.sort() # O(nlogn)
            for i, num in enumerate(nums):
                if i > 0 and num == nums[i - 1]: continue # 중복된 값 넘어가기
                left, right = i + 1, len(nums) - 1 # 왼 오 인덱스를 양 끝(i번째 이후 수들 중)으로 저장
                while left < right:
                    sum3 = num + nums[left] + nums[right] # 세 수의 합계
                    if sum3 > 0: right -= 1 # 양수면 right를 당기기
                    elif sum3 < 0: left += 1 # 양수면 left를 당기기
                    else: # 합계가 0일 때,
                        res.append([num, nums[left], nums[right]]) # 정답 배열에 수 저장
                        left += 1 # left를 당기기
                        while nums[left] == nums[left-1] and left < right: left += 1 # 중복된 값 넘어가기
                        
            return res