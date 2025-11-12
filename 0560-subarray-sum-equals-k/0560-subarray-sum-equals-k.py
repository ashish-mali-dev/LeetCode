class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        curSum = 0
        prefixSums = { 0:1 } # base case empty array

        for num in nums:
            curSum += num
            diff = curSum - k

            total += prefixSums.get(diff,0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum,0)
        
        return total

# Prefix Sum approach -  sum_0_to_a + sum_a_to_b  = total sum so far (curSum). We need a prefix that is sum_a_to_b to be equal to k. For that to hold true, replace sum_a_to_b with 'k'. Hence, sum_0_to_a + k  = curSum. Hence curSum - k = sum_0_to_a. And then since we have been storing all possible values of sum_0_to_a so far in the hashmap, curSum - k must exist in the hashmap as a key, and we can simply add the value from the hashmap to add number of prefixes from 0 to any index which equalled to curSum - k .
# Time and Space complexity - O(n)

# we cannot use two pointer approach as constraint states numbers can be negative as well (increasing window won't guarantee increased total)

# Brute force solution- O(n^2)
        # total = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i,len(nums)):
        #         sum += nums[j]
        #         if(sum == k):
        #             total += 1
        # return total