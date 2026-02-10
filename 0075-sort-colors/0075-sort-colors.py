class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Dutch National Flag - T(O(n)) S(O(1))
        i=0
        j=len(nums)-1
        k=0

        while(k<=j):
            if nums[k]==1:
                k+=1
            elif nums[k]==2:
                nums[k],nums[j] = nums[j],nums[k]
                j-=1
            else:
                nums[k],nums[i] = nums[i],nums[k]
                i+=1
                k+=1