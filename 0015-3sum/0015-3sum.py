class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            # Early stop
            if nums[i] > 0:
                break

            # Skip duplicate i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            low = i + 1
            high = n - 1
            target = -nums[i]

            while low < high:
                s = nums[low] + nums[high]

                if s == target:
                    res.append([nums[i], nums[low], nums[high]])

                    # Move both pointers
                    low += 1
                    high -= 1

                    # Skip duplicate low
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1

                    # Skip duplicate high
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1

                elif s < target:
                    low += 1
                else:
                    high -= 1

        return res
