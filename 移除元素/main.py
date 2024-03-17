# 输入一个数组，移除数组中值为var的数，返回移除后数组长度
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        b = 0
        while a < len(nums):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
            a += 1

        return b


if __name__ == '__main__':
    var = int(input(""))
    arr = int(input(""))
    num = [int(n) for n in arr.split()]
    solution=Solution()
    result=solution.removeElement(num,var)
    print(result)
