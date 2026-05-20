class Solution:
    def countKeyChanges(self, s: str) -> int:
        s=s.lower()
        res=0
        curr=s[0]
        
        for i in range(len(s)):
            if curr==s[i]:
                continue
            curr=s[i]
            res+=1
        return res
