class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in range(len(strs)): # O(n)
            temp = ''.join(sorted(strs[i])) # O(nlogn)
            if temp not in dic: dic[temp] = [] # O(1)
            dic[temp].append(strs[i]) # O(1)
        strs[:] = []
        for i in dic: # O(n)
            strs.append(dic[i])
        return strs