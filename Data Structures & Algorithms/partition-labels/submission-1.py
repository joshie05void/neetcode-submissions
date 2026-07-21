class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = {char:i for i,char in enumerate(s)}
        result = []
        start = 0
        end = 0
        for i,char in enumerate(s):
            end = max(end,last_seen[char])
            if i==end:
                result.append(end-start+1)
                start = i+1
        return result