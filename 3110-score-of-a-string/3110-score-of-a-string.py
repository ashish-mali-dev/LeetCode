class Solution:
    def scoreOfString(self, s: str) -> int:
        s=list(s)
        first=0
        second=1
        res=0

        while len(s)>second:
            res+=abs(ord(s[first])-ord(s[second]))
            first+=1
            second+=1
        
        return res

