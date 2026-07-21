class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        used = []

        for i in range(len(strs)):
            if i in used:
                continue

            temp = [strs[i]]
            used.append(i)

            for j in range(i + 1, len(strs)):
                if j not in used and sorted(strs[i]) == sorted(strs[j]):
                    temp.append(strs[j])
                    used.append(j)

            final.append(temp)
        return final