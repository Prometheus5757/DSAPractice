"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

The Constraints:
1. Time complexity should be linear O(n).
2. Try to solve this using a barebones dictionary first.

Example 1:
nums = [3, 2, 3]
Output: 3

Example 2:
nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2
"""

def majority_element(nums):
    elementcount = {}
    highestfrequency = 0
    for num in nums:
        elementcount[num] = elementcount.get(num, 0) + 1
        if elementcount[num] > highestfrequency:
            highestfrequency = elementcount[num]
            mostfrequent = num
    
    return mostfrequent

print(majority_element([3, 2, 3]))
print(majority_element([2, 2, 1, 1, 1, 2, 2]))