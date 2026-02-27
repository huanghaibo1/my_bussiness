"""
题目17：Binary Search
难度：⭐⭐ (Easy)
来源：所有公司基础题
考点：二分查找、算法基础

题目描述：
Given a sorted array, find the index of a target value using binary search.
Return -1 if not found.

Example:
Input: nums = [1, 3, 5, 7, 9, 11], target = 7
Output: 3
"""

def binary_search(nums, target):
    """
    Solution 17: 二分查找

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Test
def test_binary_search():
    nums = [1, 3, 5, 7, 9, 11]
    target = 7
    print("题目17 - 二分查找:")
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {binary_search(nums, target)}")
    print()

if __name__ == "__main__":
    test_binary_search()
