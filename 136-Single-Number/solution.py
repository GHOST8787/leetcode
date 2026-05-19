# 遇到相同的數字先是正的第二次遇到相同的成以負號
# 最後相加
# return最終數值


class Solution(object):
    def singleNumber(self, nums):
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for num in count:
            if count[num] == 1:
                return num

        """
        :type nums: List[int]
        :rtype: int
        """
