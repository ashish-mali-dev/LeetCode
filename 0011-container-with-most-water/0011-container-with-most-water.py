class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        l=0
        r=len(height)-1

        while l<r:
            area = (r-l) * min(height[l],height[r]) # width * height
            res=max(res,area)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res

#Bruteforce
        # res=0

        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         area = (j-i) * min(height[i],height[j]) # width * height
        #         res=max(res,area)
        # return res