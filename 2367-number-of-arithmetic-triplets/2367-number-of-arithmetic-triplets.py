class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        res=0
        check=set(nums)

        for num in nums:
            if(num+diff) in check and (num+(2*diff)) in check:
                res+=1
        return res