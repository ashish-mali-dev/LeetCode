class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_frequency = {}
        majority_frequency = len(nums)//2
        for num in nums:
            frequency = 1 + num_frequency.get(num,0) # Gets element if exist or given default (0)
            if frequency> majority_frequency:
                return num
            num_frequency[num]= frequency

# Store frequency in hashmap and return for frequency more than half