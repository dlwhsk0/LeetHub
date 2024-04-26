class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        ds = {}
        dt = {}
        l = max(len(s), len(t))
        for i in range(l):
            if len(s) > i and s[i] not in ds: ds[s[i]] = 0
            ds[s[i]] += 1
            if len(t) > i and t[i] not in dt: dt[t[i]] = 0
            dt[t[i]] += 1
        
        for d in ds:
            if d not in dt or ds[d] != dt[d]: return False
        
        return True