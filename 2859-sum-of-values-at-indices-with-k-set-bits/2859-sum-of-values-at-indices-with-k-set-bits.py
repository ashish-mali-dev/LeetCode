class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res=0

        for i,num in enumerate(nums):
            c=0
            temp=i
            while temp>0:
                rem=temp%2
                temp=temp//2
                if rem==1:
                    c+=1
            if c==k:
                res+=num
        
        return res