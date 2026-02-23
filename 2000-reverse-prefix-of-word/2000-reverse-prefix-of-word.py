class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        j = word.find(ch)

        if j == -1:
            return word

        res = list(word[:j+1])
        
        i = 0
        right = j
        while i < right:
            res[i], res[right] = res[right], res[i]
            i += 1
            right -= 1

        return "".join(res) + word[j+1:]