class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = [nums[0]] # Base
        
        for i in range(1,len(nums)):
            runningSum.append(runningSum[i-1] + nums[i])
        
        return runningSum

# Time and Space Complexity - O(n)