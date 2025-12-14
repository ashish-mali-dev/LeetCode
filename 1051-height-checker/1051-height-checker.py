class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = [-1]*len(heights)

        for i in range(len(heights)):
            res[i]=heights[i]
        
        res.sort()
        print(res)

        count=0
        for j in range(len(heights)):
            if (heights[j] != res[j]):
                count+=1

        return count