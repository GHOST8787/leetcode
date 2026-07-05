# 題目：125. Valid Palindrome
# 給一個字串 s，判斷它是不是「回文」（正著讀跟反著讀一樣）
# 但比對前要先整理字串：
#   1. 只留下字母和數字（空格、逗號、冒號這些符號全部丟掉）
#   2. 大寫全部變小寫
# 整理完之後，正著讀 = 反著讀 → True，不一樣 → False
#
# 例子 1："A man, a plan, a canal: Panama"
#   整理後 → "amanaplanacanalpanama" → 正反一樣 → True
# 例子 2："race a car"
#   整理後 → "raceacar" → 正讀 r 開頭、反讀 r 開頭但第二個字不同 → False
# 例子 3：" "（只有一個空格）
#   整理後 → ""（空字串）→ 空字串算回文 → True
#
# 在下面寫你的思路：
# 先去掉標點符號
# 閱讀第一個字跟最後一個字是否相等，記錄現在的總字數的字數位置
# 閱讀第二個字根倒數第二個字是否相等，記錄現在的總字數的字數位置(迴圈)
# 若有任何不相等回傳FLASE
# 一樣就繼續讀，若字數倒數位置減正數位置小於等於零 回傳TRUE
# 如果甚麼都讀不到回傳TRUE

class Solution(object):
    def isPalindrome(self, s):
        A = []
        for letter in s:
            if letter.isalnum():
                A.append(letter.lower())
        left = 0
        right = len(A)-1
        while left < right:
            if A[left] != A[right]:
                return False
            left = left+1
            right = right-1
        return True

