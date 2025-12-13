class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        slow=0
        fast=0

        while(fast<len(nums)):
            if nums[fast]%2==0:
                nums[slow],nums[fast] = nums[fast],nums[slow]
                slow+=1
            fast+=1
        return nums