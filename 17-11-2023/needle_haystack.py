'''' if needle is in haystack(list) return 0, if needle is not in haystack return -1'''
class Solution:
    class Solution:
        def strStr(self, haystack: str, needle: str) -> int:
            if not needle:
                return 0
            if needle in haystack:
                return haystack.index(needle)
            else:
                return -1 
