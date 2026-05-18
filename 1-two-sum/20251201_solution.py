class Solution(object):
    def twoSum(self, nums, target):
        seen = {}  # 存數字: index

        for i, num in enumerate(nums):
            complement = target - num

            # 若 complement 在 seen 中，且 index 不同 → 找到答案
            if complement in seen:
                return [seen[complement], i]

            # 將目前 num 的 index 存入（若有重複只記第一個不會影響）
            seen[num] = i

        return None
