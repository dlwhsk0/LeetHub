class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() # 소문자 변환 # O(n)
        s = ''.join(c for c in s if c.isalnum()) # 알파벳과 숫자 남기기 # O(n)
        start = 0
        end = len(s)-1
        while start < end: # O(n/2)
            if s[start] != s[end]: return False
            start += 1
            end -= 1
        return True