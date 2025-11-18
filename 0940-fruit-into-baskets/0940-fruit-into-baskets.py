class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        low=0
        high=0
        res=0
        count = defaultdict(int)

        for high in range(len(fruits)):
            count[fruits[high]]+=1

            while(len(count)>2): #while information is wrong, we shrink to get correct info
                count[fruits[low]]-=1
                if(count[fruits[low]]==0):
                    del count[fruits[low]]
                low+=1
            
            size = high-low+1
            res = max(res, size)
        
        return res