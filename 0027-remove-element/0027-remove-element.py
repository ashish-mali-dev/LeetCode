class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        low=0
        high=len(nums)-1

        while low<=high:
            if(nums[low]==val):
                nums[low],nums[high] = nums[high],nums[low]
                high-=1
            else:
                low+=1
        return low