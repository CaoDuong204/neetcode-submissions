class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(min(len(s) for s in strs)):
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0][:min(len(s) for s in strs)]