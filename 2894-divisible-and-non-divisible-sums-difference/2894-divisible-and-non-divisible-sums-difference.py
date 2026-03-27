class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum_div=0
        sum_nondiv=0

        for i in range(1,n+1):
            if i%m==0:
                sum_div+=i
            else:
                sum_nondiv+=i
        return sum_nondiv-sum_div