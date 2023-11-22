class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        number = len(s)
        for index in range(1, number//2 + 1):
            if number % index == 0:
                substring = s[:index]
                if substring * (number // index) == s:
                    return True
        return False