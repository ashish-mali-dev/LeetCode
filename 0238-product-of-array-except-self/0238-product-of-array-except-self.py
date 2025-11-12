class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1

        # left pass: res[i] = product of all elements to the left of i
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        # right pass: multiply by product of elements to the right of i
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix  
            postfix *= nums[i]
        return res    

# We can do this by keeping left pass and right pass as separate passes and create res by multiplying them
# However, this will cause O(n) space, do achieve it in O(1) we use same res array after left pass