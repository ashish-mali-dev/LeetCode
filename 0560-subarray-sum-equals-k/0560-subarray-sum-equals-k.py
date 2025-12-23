class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum=0 # prefix_sum[i] is sum from 0 to i
        # we want 2 subarrays sum = k like two sum for each subrray sum we can check if k-subarray sum exist
        count=0
        freq={0:1} # imp as subarray starting at idx 0
        # prefix_sum[j] - prefix_sum[i] = k Then subarray (i+1 → j) has sum k. prefix_sum[i] = prefix_sum[j] - k


        for num in nums:
            prefix_sum+=num

            if prefix_sum-k in freq:
                count+=freq[prefix_sum-k]
            freq[prefix_sum] = freq.get(prefix_sum,0)+1
        return count
