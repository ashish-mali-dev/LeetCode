class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Approach 1
        # res=[]

        # for num in nums:
        #     res.append(num*num)
        # res.sort()
        # return res
        # O(n.logn) since sorting

        # Approach 2
        left=0
        right=len(nums)-1
        res=[0]*len(nums)
        i=len(nums)-1

        while(left<=right):
            if(abs(nums[left])>nums[right]):
                res[i]=nums[left]*nums[left]
                left+=1
            else:
                res[i]=nums[right]*nums[right]
                right-=1
            i-=1
        return res

        # O(n)