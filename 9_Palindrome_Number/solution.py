# 出現負就先排除
# 把數值跟數值倒過來以LIST的形式看是否相等

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        original = x
        reversed_num = 0
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x = x // 10
        return original == reversed_num


        """
        :type x: int
        :rtype: bool
        """
