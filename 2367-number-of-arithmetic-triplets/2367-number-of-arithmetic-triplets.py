class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        res=0
        check=set(nums)

        for num in nums:
            if(num+diff) in check and (num+(2*diff)) in check:
                res+=1
        return res

#i < j < k,
#nums[j] - nums[i] == diff means nums[j] = diff + nums[i]
#nums[k] - nums[j] == diff replace above in thus nums[k] - (diff + nums[i])= diff
# i.e. nums[k] = diff+diff+nums[i] ~ nums[k] = nums[i]+  2* diff
# if we get correct num then we can check for j,k inclusion