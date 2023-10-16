List = [2, 7, 11, 15]
target = 9


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numslist = {}
        for index, number in enumerate(nums):
            difference = target - number
            if difference in numslist:
                return [numslist[difference], index]
            else:
                numslist[number] = index
                