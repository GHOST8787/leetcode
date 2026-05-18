# 看到括號 尋找另一遍 如果只有單邊就輸出 FALSE
# 按照順序用LIST記得括號 後進先出 違反的話FALSE

class Solution(object):
    def isValid(self, s):
        stack = []
        match = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if stack == [] or stack[-1] != match[c]:
                    return False
                stack.pop()
        return stack == []

sol = Solution()
print(sol.isValid("()"))       # True
print(sol.isValid("([])"))     # True
print(sol.isValid("(]"))       # False
print(sol.isValid("([)]"))     # False
print(sol.isValid(""))         # True
