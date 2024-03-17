# 给你一个非负整数数组nums ，你最初位于数组的第一个下标。数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个下标，如果可以，返回true ；否则，返回false 。
from typing import List


# 递归求解
# 优点：看起来比贪心算法高端
# 缺点：实际上时间和空间复杂度都不如贪心算法（笑）
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= len(nums) - 1 - i:
                if self.canJump(nums[0:(i + 1)]):
                    return True
                else:
                    return False
        return False


if __name__ == '__main__':
    arr = input("")
    sol = Solution()
    num = [int(n) for n in arr.split()]
    if sol.canJump(num):
        print("可到达最后下标")
    else:
        print("不可到达")
