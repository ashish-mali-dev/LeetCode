class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        res=math.inf
        nums.sort()
        n=len(nums)
        
        for i in range(n//2+1):
            avg=(nums[i]+nums[n-i-1])/2
            res=min(res,avg)
        return res
