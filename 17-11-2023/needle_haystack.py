'''' if needle is in haystack(list) return 0, if needle is not in haystack return -1'''
class Solution:
    def strStr(self, haystack: str, needle: str):
        if needle in haystack:
            return 0
        else:
            return -1


