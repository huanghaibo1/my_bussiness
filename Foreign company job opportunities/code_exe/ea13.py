"""
题目13：字典排序
难度：⭐⭐ (Easy-Medium)
来源：All companies
考点：排序、字典操作

题目描述：
Sort a dictionary by:
1. Values (descending)
2. Keys (ascending) if values are equal

Example:
Input: {'apple': 3, 'banana': 1, 'cherry': 3, 'date': 2}
Output: [('apple', 3), ('cherry', 3), ('date', 2), ('banana', 1)]
"""

def sort_dictionary(d):
    """
    Solution 13: 字典排序

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    # Sort by value (desc), then by key (asc)
    sorted_items = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items

# Test
def test_sort_dict():
    d = {'apple': 3, 'banana': 1, 'cherry': 3, 'date': 2}
    print("题目13 - 字典排序:")
    print(f"Input: {d}")
    print(f"Output: {sort_dictionary(d)}")
    print()

if __name__ == "__main__":
    test_sort_dict()
