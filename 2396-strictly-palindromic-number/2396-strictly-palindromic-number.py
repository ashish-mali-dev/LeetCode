class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
    # To convert a number n to base b, repeatedly divide n by b and
    # collect the remainders (n % b). The remainders read in reverse
    # form the base-b representation.

    # For strictly palindromic numbers:
    # For any n >= 4, in base (n - 2),
    # n = 1*(n - 2) + 2 → representation is always "12",
    # which is not a palindrome.
    # Since constraints guarantee n >= 4, the answer is always False.
    
        return False