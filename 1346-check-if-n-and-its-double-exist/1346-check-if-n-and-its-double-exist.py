class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        checked = set()
        
        for num in arr:
            if(num*2 in checked or (num/2 in checked and num%2==0)):
                return True
            checked.add(num)
        return False
