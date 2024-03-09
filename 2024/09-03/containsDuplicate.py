class Solution:
    def containsDuplicate(self, nums):
        Final_list = set()
        for num in nums:
            if num in Final_list:
                return True
            Final_list.add(num)

        return False
