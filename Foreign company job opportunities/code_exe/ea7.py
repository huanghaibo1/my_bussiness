"""
题目7：找出列表中出现次数最多的元素
难度：⭐⭐ (Easy-Medium)
来源：Amazon, Microsoft
考点：Counter, 哈希表

题目描述：
Given a list of elements, find the top K most frequent elements.

Example:
Input: [1, 1, 1, 2, 2, 3], k=2
Output: [1, 2]
"""
from collections import Counter
import heapq

def top_k_frequent(nums, k):
    """
    Solution 7: Top K 频率元素

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    # Count frequencies
    counter = Counter(nums)

    # Get top k
    top_k = [item for item, count in counter.most_common(k)]

    return top_k

# Alternative solution using heap (more efficient for large k)
def top_k_frequent_heap(nums, k):
    """
    Alternative: Using heap
    Time Complexity: O(n log k)
    """
    counter = Counter(nums)
    return heapq.nlargest(k, counter.keys(), key=counter.get)

# Test
def test_top_k():
    nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
    print("题目7 - Top K频率元素:")
    print(f"Input: {nums}, k=2")
    print(f"Output: {top_k_frequent(nums, 2)}")
    print()

if __name__ == "__main__":
    test_top_k()
