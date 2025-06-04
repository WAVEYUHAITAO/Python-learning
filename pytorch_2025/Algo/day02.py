#移除元素
from typing import List

#双指针方法
class Solution:
    def removeElement(self, nums: List[int], val: int)->(int, List[int]):
        slow = 0
        fast = 0
        size = len(nums)
        list=[]
        while fast<size:
            if nums[fast]!=val:
                # nums[slow] = nums[fast]
                list.append(nums[fast])
                slow+=1
            fast+=1
        return slow, list
list1 = [2,1,2,2,3,0,4,2]
out = Solution().removeElement(list1, 2)
print(out)
