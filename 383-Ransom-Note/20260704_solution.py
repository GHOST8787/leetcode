# 題目：383. Ransom Note
# 給兩個字串：ransomNote（勒索信）和 magazine（雜誌）
# 判斷能不能用雜誌上剪下來的字母拼出勒索信
# 雜誌上的每個字母只能用一次
# 拼得出來回傳 True，拼不出來回傳 False
#
# 在下面寫你的思路：
# 信比雜誌長直接 False
# 把 magazine 字串拆成一個字一個字
# ransomNote 的第一個字儲存到 magazine 裡面找
# 把 ransomNote 第一個字 跟 magazine每一個字母依序比對
# 只要有比對到就劃掉 magazine中的該字
# 開始走 ransomNote 第二個字
# 依此類推沿路找下去
# 如果有沒找到的就回傳FALSE
# 都有找到回傳TRUE

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(magazine) < len(ransomNote):
            return False
        A = list(magazine)
        for letter in ransomNote:
            if letter in A:
                A.remove(letter)
            else:
                return False
        return True

