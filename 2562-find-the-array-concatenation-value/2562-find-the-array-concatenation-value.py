class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res=0
        temp=""
        low=0
        high =len(nums)-1

        while low<high:
            temp=str(nums[low])+str(nums[high])
            low+=1
            high-=1
            res=res+int(temp)
        if len(nums)%2==1:
            res+=nums[low]
        return res

