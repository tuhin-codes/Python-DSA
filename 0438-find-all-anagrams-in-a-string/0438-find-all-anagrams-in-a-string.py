class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(s) < len(p):
            return []

        ans = []
        pFreq = [0] * 26
        wFreq = [0] * 26

        # First window
        for i in range(len(p)):
            pFreq[ord(p[i]) - ord('a')] += 1
            wFreq[ord(s[i]) - ord('a')] += 1

        if pFreq == wFreq:
            ans.append(0)

        # Slide the window
        for i in range(len(p), len(s)):
            wFreq[ord(s[i]) - ord('a')] += 1
            wFreq[ord(s[i - len(p)]) - ord('a')] -= 1

            if wFreq == pFreq:
                ans.append(i - len(p) + 1)

        return ans