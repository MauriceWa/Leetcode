class Solution:
    def containsDuplicate(self, nums):
        counted = set()

        for num in nums:
            if num in counted:
                return True

            counted.add(num)

        return False






