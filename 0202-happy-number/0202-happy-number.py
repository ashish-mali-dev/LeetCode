class Solution:
    def isHappy(self, n: int) -> bool:
        if(n==1 or n==7):
            return True
        elif(n<10):
            return False
        else:
            total =0
            while(n>0):
                temp = n%10
                total += temp*temp
                n= n//10
            return self.isHappy(total) 
        
