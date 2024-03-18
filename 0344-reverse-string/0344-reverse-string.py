class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = len(s) - 1
        for i in range(int(l/2)+1):
            s[i] , s[l-i] = s[l-i], s[i] # 투포인터