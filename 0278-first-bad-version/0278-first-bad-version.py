# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low=1
        high=n
        low_index=math.inf

        while(low<=high):
            n=low+(high-low)//2

            if(isBadVersion(n)):
                low_index=min(low_index,n)
                high=n-1
            else:
                low=n+1
        return low_index
