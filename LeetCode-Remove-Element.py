'''
Remove Element:
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
'''


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        k = len(nums)
        for element in range(len(nums)):
            if nums[element] != val:
                nums[i] = nums[element]
                i+=1
            else:
                k-=1
        return k

        # while nums and i < len(nums):
        #     if nums[i] == val:
        #        del nums[i]
        #        i-=1
        #        print(nums)
        #        continue
        #     i+=1
