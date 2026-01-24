class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        res=""

        for word in words:
            l=0
            r=len(word)-1
            is_palin=True

            while l<r:
                if word[l]!=word[r]:
                    is_palin=False
                    break
                l+=1
                r-=1
            if is_palin:
                return word
        return res