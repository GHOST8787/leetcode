# 題目：242. Valid Anagram
# 給兩個字串 s 和 t，判斷 t 是不是把 s 的字母重新排列組成的
# 是就回傳 True，不是就回傳 False
#
# 在下面寫你的思路：
# 我的思路是把兩個的每一個字都拆開
# 在t的列表中尋找s中的字母
# 先用s的第一個字幕對t
# 如果t有的話就下一輪
# 用第二個s的字母對t
# 沒有的話直接回傳FALSE
# 如果全部隊玩都有的畫回傳TRUE



class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):    # 門口保安：長度不同直接不是
            return False

        B = list(t)
        for letter in s:        # 字串可以直接 for，連 list(s) 都可以省
            if letter in B:
                B.remove(letter)    # 找到 → 劃掉，才不會被重複用
            else:
                return False        # 找不到 → 直接回答不是

        return True             # 全部對完都在 → 是
