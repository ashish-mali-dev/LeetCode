class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res=0
        for i in range(low,high+1):
            s=str(i)
            
            if len(s)%2==1:
                continue
            
            mid = len(s)//2
            
            left = sum(int(c) for c in s[:mid])
            right = sum(int(c) for c in s[mid:])
            if left==right:
                res+=1
        return res
