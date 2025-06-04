#二分查找
class Solution(object):
    def search(self, nums:list[int], target:[int]) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left,right = 0,len(nums)-1

        while left<=right:
            middle = left + (right-left)//2
            if nums[middle]>target:
                right = middle-1
            elif nums[middle]<target:
                left = middle+1
            else:
                return middle
        return -1

list1 = [-1,0,1,2,3,4,5]
target = 2


result = Solution().search(list1, target)
print(result)