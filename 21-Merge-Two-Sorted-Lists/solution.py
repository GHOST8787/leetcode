# 兩列已經從小到大排好的撲克牌，你要把它們合併成一列
# 把兩行的撲克牌從第一張打開
# (迴圈) 比大小比較小的塞到LIST中再翻開同一行的撲克牌


# LeetCode 網站上平台會先定義好 ListNode，本機要自己補，檔案才跑得起來
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val      # 這張牌的數字
        self.next = next    # 指向下一張牌


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2
        return dummy.next
