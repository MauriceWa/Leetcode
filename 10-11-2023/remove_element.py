class Solution():
    def removeElement(self, nums, val):
        position = 0
        for num in nums:
            if num != val:
                nums[position] = num
                position += 1
        return position

