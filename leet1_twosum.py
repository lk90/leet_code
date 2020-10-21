"""
Given an array of integers nums and an integer target, return indices of
the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you
may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

"""
# List=[2,7,11,13]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums=[2,7,11,13]
        """
        mapp = dict()
        for i,x in enumerate(nums):
            #diff = target- x
            if x in mapp:return [mapp[x], i]
            mapp[target-x] = i
        return
        """
        """
        mapp = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff not in mapp:
                mapp[nums[i]] = i
            else:
                return [mapp[diff],i]
        """
        """
        for i in range(len(nums)):
            x= target-nums[i]
            if x==nums[i] in nums[i+1:]:
                continue
            if x in nums:
                break
        return [i,nums.index(x)]
        """
        mapp = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in mapp:
                mapp[nums[i]] = i
            else:
                return [mapp[diff], i]