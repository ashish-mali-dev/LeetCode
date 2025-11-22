class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if(len(bloomDay)<m*k):
            return -1
        
        low=min(bloomDay)
        high=max(bloomDay)

        while(low<high):
            mid=low+(high-low)//2

            if(self.check(bloomDay,m,k,mid)):
                high=mid
            else:
                low=mid+1
        return low
    
    def check(self, bloom: List[int], m: int, k: int, day: int):
        bouquets = 0
        run = 0
        for b in bloom:
            if b <= day:
                run += 1
                if run == k:
                    bouquets += 1
                    run = 0
            else:
                run = 0
            if bouquets >= m:   # early exit
                return True
        return False
