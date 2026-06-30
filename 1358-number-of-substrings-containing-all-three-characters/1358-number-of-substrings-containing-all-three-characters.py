class Solution:
    def numberOfSubstrings(self, s):

        left = 0
        n = len(s)

        freq = {'a':0, 'b':0, 'c':0}

        count = 0

        for right in range(n):

            freq[s[right]] += 1

            while freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:

                count += n - right

                freq[s[left]] -= 1
                left += 1

        return count