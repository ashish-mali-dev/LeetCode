class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n= len(nums)

        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        
        pos=0

        for i in range(len(nums)):
            if nums[i]!=0:
                nums[pos]=nums[i]
                pos+=1
        
        while pos<n:
            nums[pos]=0
            pos+=1
        
        return nums