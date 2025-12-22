class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        if numRows == 0:
            return res
        
        res.append([1]) #Add first row

        for i in range(1,numRows):
            prev_row = res[i-1]
            current_row = [1]

            for j in range(1,i):
                current_row.append(prev_row[j-1]+prev_row[j])
            
            current_row.append(1)
            res.append(current_row)
        return res