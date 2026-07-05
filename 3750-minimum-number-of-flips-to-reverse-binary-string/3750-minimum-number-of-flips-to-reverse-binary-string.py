class Solution:
    def minimumFlips(self, n: int) -> int:
        s=bin(n)[2:]
        rev=s[::-1]

        ans=0
        for i in range(len(s)):
            if(s[i]!=rev[i]):
                ans+=1

        return ans
