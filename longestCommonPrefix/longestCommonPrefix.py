class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        prefix = ""
        for c in strs[0]:
            for s in strs:
                if not s.startswith(prefix + c):
                    return prefix
            prefix += c
        return prefix
    
if __name__ == "__main__":
    s = ["florida","flower","flow"]
    print(Solution.longestCommonPrefix(s))