class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        low=0
        high=len(s)-1
        s=list(s)

        while low<high:
            if s[low]!=s[high]:
                if ord(s[low])<ord(s[high]):
                    s[high]=s[low]
                else:
                    s[low]=s[high]
            low+=1
            high-=1
        
        return "".join(s)
