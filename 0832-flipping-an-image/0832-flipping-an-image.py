class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res=[]
        
        for i in range(len(image)):
            j=len(image[i])-1
            curr = image[i]
            next_ele=[]
            while(j>=0):
                if curr[j]==1:
                    next_ele.append(0)
                else:
                    next_ele.append(1)
                j-=1
            res.append(next_ele)
        return res
