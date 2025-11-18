class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum=0
        low=0
        high=0
        best_min=math.inf

        if len(nums)==0:
            return 0

        for high in range(len(nums)):
            window_sum+=nums[high] #Add high to sum

            while(window_sum>=target): # We got one right, shrinking will give minimum
                size = high-low+1
                best_min = min(best_min, size) # Check current window
                window_sum-=nums[low] # Shrink window
                low+=1
        return 0 if best_min == math.inf else best_min
                