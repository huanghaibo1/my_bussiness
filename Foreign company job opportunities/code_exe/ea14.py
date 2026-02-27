"""
题目14：Two Sum
难度：⭐ (Easy)
来源：Amazon, Microsoft (LeetCode 1)
考点：哈希表、双指针

题目描述：
Given an array of integers and a target, return indices of two numbers
that add up to the target.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1] (because nums[0] + nums[1] = 9)
"""

def two_sum(nums, target):
    """
    Solution 14: Two Sum

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []

# Test
def test_two_sum():
    nums = [2, 7, 11, 15]
    target = 9
    print("题目14 - Two Sum:")
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {two_sum(nums, target)}")
    print()

if __name__ == "__main__":
    test_two_sum()
