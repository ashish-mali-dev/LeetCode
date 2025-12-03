class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0

        for num in nums:
            temp=str(num)
            if(len(temp)%2==0):
                count+=1
        return count