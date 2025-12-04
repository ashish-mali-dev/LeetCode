class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        zeros = 0

        # Count how many zeros can be duplicated
        # without exceeding array bounds.
        i = 0
        while i + zeros < n:
            if arr[i] == 0:
                # If this zero is exactly at the last place we can write,
                # it must be handled specially as a single zero.
                if i + zeros == n - 1:
                    arr[n-1] = 0
                    n -= 1     # reduce effective length
                    break
                zeros += 1
            i += 1

        # Now i is the last index we should read from.
        read = i - 1
        write = n - 1

        # Copy backwards
        while read >= 0:
            if arr[read] == 0:
                arr[write] = 0
                write -= 1
                arr[write] = 0
                write -= 1
            else:
                arr[write] = arr[read]
                write -= 1
            read -= 1
