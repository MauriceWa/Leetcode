class Solution:
    def containsDuplicate(self, nums):
# print hij num list
# itereer door list en check voor duplicate
# return true of false

        for num in range(len(nums) - 1):
            if list[nums] == range(nums):
                print("True")





def containsDuplicate(nums):

    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False


result = containsDuplicate([1, 2, 3, 4, 1])
print(result)