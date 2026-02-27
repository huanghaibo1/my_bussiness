"""
题目12：合并多个字典
难度：⭐⭐ (Medium)
来源：Microsoft, Amazon
考点：字典合并、冲突处理

题目描述：
Merge multiple dictionaries. If a key appears in multiple dicts,
sum the values (assuming numeric values).

Example:
Input: [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 5}]
Output: {'a': 6, 'b': 5, 'c': 4}
"""
from collections import Counter

def merge_dictionaries(dicts):
    """
    Solution 12: 合并字典

    Time Complexity: O(n*m) where n is number of dicts, m is avg keys per dict
    Space Complexity: O(k) where k is total unique keys
    """
    result = {}

    for d in dicts:
        for key, value in d.items():
            result[key] = result.get(key, 0) + value

    return result

# Alternative: Using Counter
def merge_dictionaries_counter(dicts):
    """
    Alternative: Using Counter
    """
    result = Counter()
    for d in dicts:
        result.update(d)
    return dict(result)

# Test
def test_merge_dicts():
    dicts = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 5}]
    print("题目12 - 合并字典:")
    print(f"Input: {dicts}")
    print(f"Output: {merge_dictionaries(dicts)}")
    print()

if __name__ == "__main__":
    test_merge_dicts()
