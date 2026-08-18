# Problem: Two Sum II - Input Array Is Sorted
# LeetCode: 167
#
# Pattern: Two Pointers
#
# Approach:
# Since the array is sorted, I use two pointers:
# one at the beginning and one at the end.
#
# If the sum is too small, move the left pointer.
# If the sum is too large, move the right pointer.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1

        while left<right:
            total=numbers[left]+numbers[right]
            if total==target:
                return [left+1,right+1]
            elif total>target:
                right-=1
            else:
                left+=1
