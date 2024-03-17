# 投票法求数组中过半的元素

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = nums[0]
        for num in nums:
            if candidate == num:
                count+=1
            else:
                count-=1
                if count<0:
                    candidate =num
                    count = 0
        if count>0:
            print(candidate)
        else:
            print("无过半元素")


if __name__=='__main__':
    sol = Solution()
    arr = input("")
    num = [int(n) for n in arr.split()]
    sol.majorityElement(num)

