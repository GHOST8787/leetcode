# 儲存第n個的數值(n從0開始)
# 判讀隔壁的數值是否相同
# 不同的話拉到n+1的位置，然後n=n+1
# 如果判讀結束就輸出 n = 長度
# 然後直接輸出排序好的LIST的長度

class Solution(object):
    def removeDuplicates(self, nums):
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1                  # n = n + 1
                nums[slow] = nums[fast]    # 拉到 n+1 的位置
        return slow + 1

