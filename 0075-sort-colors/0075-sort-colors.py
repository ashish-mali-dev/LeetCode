class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts={}

        for num in nums:
            if num==0:
                counts['red']=counts.get('red',0)+1
            elif num==1:
                counts['white']=counts.get('white',0)+1
            else:
                counts['blue']=counts.get('blue',0)+1
        
        for i in range(len(nums)):
            if 'red' in counts:
                nums[i]=0
                counts['red']-=1
                if counts['red']==0:
                    del counts['red']
            elif 'white' in counts:
                nums[i]=1
                counts['white']-=1
                if counts['white']==0:
                    del counts['white']
            else:
                nums[i]=2
                counts['blue']-=1
                if counts['blue']==0:
                    del counts['blue']