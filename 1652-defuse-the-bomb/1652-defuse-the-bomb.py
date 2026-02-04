class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        res=[0]*n

        if k==0:
            return res

        if k>0:
            start,end = 1,k
        else:
            start,end = k,-1

        window_sum=0
        for i in range(start,end+1):
            window_sum+=code[i%n]
        
        for i in range(n):
            res[i]= window_sum
            window_sum -=code[(i+start)%n]
            window_sum +=code[(i+end+1)%n]
        return res
        

        