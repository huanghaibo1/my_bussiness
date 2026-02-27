"""
题目9：列表去重并保持顺序
难度：⭐⭐ (Easy-Medium)
来源：Accenture, Deloitte
考点：集合、顺序保持

题目描述：
Remove duplicates from a list while preserving the original order.

Example:
Input: [1, 2, 3, 2, 4, 3, 5]
Output: [1, 2, 3, 4, 5]
"""

def remove_duplicates_preserve_order(lst):
    """
    Solution 9: 去重保序

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = set()
    result = []

    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

# Alternative: Using dict (Python 3.7+ maintains insertion order)
def remove_duplicates_dict(lst):
    """
    Alternative: Using dict.fromkeys()
    """
    return list(dict.fromkeys(lst))

# Test
def test_remove_duplicates():
    lst = [1, 2, 3, 2, 4, 3, 5, 1]
    print("题目9 - 去重保序:")
    print(f"Input: {lst}")
    print(f"Output: {remove_duplicates_preserve_order(lst)}")
    print()

if __name__ == "__main__":
    test_remove_duplicates()
