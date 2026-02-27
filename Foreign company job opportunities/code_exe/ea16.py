"""
题目16：Maximum Subarray (Kadane's Algorithm)
难度：⭐⭐ (Easy-Medium)
来源：Microsoft, Amazon (LeetCode 53)
考点：动态规划、数组

题目描述：
Find the contiguous subarray which has the largest sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6 (subarray [4,-1,2,1])
"""

def max_subarray(nums):
    """
    Solution 16: 最大子数组和

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0

    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        # Either extend current subarray or start new
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Test
def test_max_subarray():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("题目16 - 最大子数组和:")
    print(f"Input: {nums}")
    print(f"Output: {max_subarray(nums)}")
    print()

if __name__ == "__main__":
    test_max_subarray()
