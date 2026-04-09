class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        low=0

        for i in range(1,len(nums)):
            if nums[i]!=nums[low]:
                low+=1
                nums[low]=nums[i]

        return low+1