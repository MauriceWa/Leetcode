class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        index, j = 0, 0
        while index < len(g) and j < len(s):
            if s[j] >= g[index]:
                index += 1
            j += 1
        return index