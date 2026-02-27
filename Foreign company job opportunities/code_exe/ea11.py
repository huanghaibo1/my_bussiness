"""
题目11：字典反转
难度：⭐⭐ (Easy-Medium)
来源：Accenture, Consulting firms
考点：字典操作、数据转换

题目描述：
Given a dictionary, reverse keys and values.
If multiple keys have the same value, collect them in a list.

Example:
Input: {'a': 1, 'b': 2, 'c': 1, 'd': 3}
Output: {1: ['a', 'c'], 2: ['b'], 3: ['d']}
"""
from collections import defaultdict

def reverse_dictionary(d):
    """
    Solution 11: 字典反转

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    reversed_dict = {}

    for key, value in d.items():
        if value not in reversed_dict:
            reversed_dict[value] = []
        reversed_dict[value].append(key)

    return reversed_dict

# Alternative: Using defaultdict
def reverse_dictionary_defaultdict(d):
    """
    Alternative: Using defaultdict
    """
    reversed_dict = defaultdict(list)
    for key, value in d.items():
        reversed_dict[value].append(key)
    return dict(reversed_dict)

# Test
def test_reverse_dict():
    d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
    print("题目11 - 字典反转:")
    print(f"Input: {d}")
    print(f"Output: {reverse_dictionary(d)}")
    print()

if __name__ == "__main__":
    test_reverse_dict()
