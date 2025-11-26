class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n=len(dist)

        ## Quick impossibility: even at infinite speed, you still need at least (n-1) whole hours for waits. e.g. for [1,3,2] you will need to wait 1 hour each after 1 and 3
        if(hour<=n-1):
            return -1
        
        low=1
        high=10000000

        while(low<high):
            mid = low+(high-low)//2

            if(self.ok(dist, hour, mid)):
                high=mid
            else:
                low=mid+1
        return low
    
    def ok(self, dist:List[int], hour:float, mid:int) -> bool:
        h=0.0

        for i in dist[:-1]:
            h+=ceil(i/mid)
            if(h>hour):
                return False
        
        h+=dist[-1]/mid # no need to wait as its last train, so we dont ceil

        return h<=hour