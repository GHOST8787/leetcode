# 一邊往後看一邊記兩個數字：
# 1. low = 目前為止看過的最低價（買入候選）
# 2. profit = 目前為止算出過的最大利潤
# 每天先算「今天價格 - low」有沒有比 profit 大，有就更新 profit
# 再看今天價格有沒有比 low 低，有就更新 low
# 全部一直跌的話 profit 從頭到尾都是 0，不用另外特判

class Solution(object):
    def maxProfit(self, prices):
        low = prices[0]      # 目前看過的最低價
        profit = 0           # 目前最大利潤

        for price in prices:
            if price - low > profit:   # 今天賣比較賺 → 更新最大利潤
                profit = price - low
            if price < low:            # 今天更便宜 → 更新最低價
                low = price

        return profit
