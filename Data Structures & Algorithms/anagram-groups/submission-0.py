class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        # for word in strs:
        #     key = "".join(sorted(word))
        #     if key in groups:
        #         groups[key].append(word)
        #     else:
        #         groups[key] = [word]
        for word in strs:
            counts = [0] * 26
            for char in word:
                index = ord(char) - ord("a")
                counts[index] += 1
            tupleCounts = tuple(counts)
            if tupleCounts not in groups:
                groups[tupleCounts] = []
            groups[tupleCounts].append(word)
        return list(groups.values())
        