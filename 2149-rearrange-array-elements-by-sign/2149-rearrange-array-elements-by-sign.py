class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives=[]
        negatives=[]
        res=[]

        for num in nums:
            if num>0:
                positives.append(num)
            else:
                negatives.append(num)
        
        pos_idx=0
        neg_idx=0
        for i in range(len(nums)):
            if i%2==0:
                res.append(positives[pos_idx])
                pos_idx+=1
            else:
                res.append(negatives[neg_idx])
                neg_idx+=1
        return res
