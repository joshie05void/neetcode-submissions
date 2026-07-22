class Solution:
    def isPalindrome(self, s: str) -> bool:
        j=0
        st = "".join(ch.lower() for ch in s if ch.isalnum())
        for i in range(len(st)-1,0,-1):
            if st[i] == st[j]:
                j+=1
            else:
                return False
        return True