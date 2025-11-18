class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        low=0
        high=0
        longest=0
        count_zero=0

        for high in range(len(nums)):
            if(nums[high]==0):
                count_zero+=1

            while(count_zero>1): 
                if nums[low]==0:
                    count_zero-=1
                low+=1

            size = high-low # not +1 since we are removing one element
            longest = max(longest,size)
        return longest