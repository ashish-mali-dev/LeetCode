class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)

        while(low<high):
            mid=low+(high-low)//2

            if(self.canEat(piles,h,mid)):
                high=mid
            else:
                low=mid+1
        return low

    def canEat(self,piles:List[int],h:int,mid:int)->bool:
        totalHours=0

        for i in range(len(piles)):
            totalHours+= (piles[i]+mid-1)//mid # same as ceil()
        
        return totalHours<=h

# she eats from one pile per hour (up to speed bananas), then continues on that same pile next hour if needed. So the correct model is per-pile ceil(pile / speed)