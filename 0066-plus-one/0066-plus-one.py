class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1,-1,-1):
            if(digits[i]!=9):
                digits[i]+=1
                return digits
            else:
                digits[i]=0 # to handle 9 + 1, will first make all 0 then add 1 at start
        
        arr=[0]*(len(digits)+1)
        arr[0]=1
        return arr