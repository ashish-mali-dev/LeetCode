class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count=0
        count=0

        for i in nums:
            if(i==0):
                max_count=max(count,max_count)
                count=0
            else:
                count+=1
        return max(count,max_count)
