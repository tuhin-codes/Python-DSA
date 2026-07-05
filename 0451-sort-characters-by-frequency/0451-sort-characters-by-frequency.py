from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:

        freq = Counter(s)

        result = []

        for ch, count in freq.most_common():

            result.append(ch * count)

        return "".join(result)