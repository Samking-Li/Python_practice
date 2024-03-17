#给你一个整数数组prices ，其中prices[i] 表示某支股票第 i 天的价格。
#在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多只能持有一股股票。你也可以先购买，然后在同一天出售。
#返回你能获得的最大利润 。

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1,len(prices)):
            temp = prices[i]-prices[i-1]
            if temp>0:
                profit+=temp
        if profit>0:
            print(profit)
        else:
            print("不参与交易")

if __name__ == '__main__':
    sol=Solution()
    arr=input("")
    price = [int(n) for n in arr.split()]
    sol.maxProfit(price)
