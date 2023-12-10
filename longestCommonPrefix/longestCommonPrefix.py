class Prefix:
    def __init__(self, strs: list[str]) -> None:
        self.strings = strs[0]
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""

        for c in strs[0]:
            for s in strs:
                if not s.startswith(prefix + c):
                    return prefix

            prefix += c

        return prefix
    
if __name__ == "__main__":
    strs = ['florida', 'flower', 'flow']
    print(Solution.longestCommonPrefix(strs))