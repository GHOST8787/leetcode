# 在nums中尋找比 TARGET 小的第一個數字按數字大小編號
# 用TARGET - 比 TARGET 小的第一個數字 後再在nums中看產生的那個數值是否在裏頭
# 如果不在裏頭的話就重新找一次 但要排除已經找過的編號

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            need = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == need:
                    return [i, j]
