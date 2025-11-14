class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=0
        left=0
        right=0
        
        for num in nums:
            total+=num

        for i in range(len(nums)):
            right = total - nums[i]-left
            if(left==right):
                return i
            left+=nums[i]
        return -1

# Total Sum = left_sum + nums[i] + right_sum
# Total Sum - left_sum - nums[i] = right

# Time Complexity O(n) and space O(1) 
# Another approach
# total = sum(nums) # use of in built function
#         left = 0

#         for i, num in enumerate(nums):
#             # right = total - left - num
#             # pivot condition: left == right  <=>  2*left + num == total
#             if 2 * left + num == total:
#                 return i
#             left += num

#         return -1