"""
题目10：Flatten嵌套列表
难度：⭐⭐ (Medium)
来源：Microsoft, Goldman Sachs
考点：递归、列表操作

题目描述：
Flatten a nested list of arbitrary depth.

Example:
Input: [1, [2, 3, [4, 5]], 6, [7]]
Output: [1, 2, 3, 4, 5, 6, 7]
"""

def flatten_list(nested_list):
    """
    Solution 10: 展平嵌套列表

    Time Complexity: O(n) where n is total number of elements
    Space Complexity: O(d) where d is maximum depth
    """
    result = []

    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))  # Recursive call
        else:
            result.append(item)

    return result

# Alternative: Using generator
def flatten_list_generator(nested_list):
    """
    Alternative: Using generator for memory efficiency
    """
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_list_generator(item)
        else:
            yield item

# Test
def test_flatten():
    nested = [1, [2, 3, [4, 5]], 6, [7]]
    print("题目10 - 展平嵌套列表:")
    print(f"Input: {nested}")
    print(f"Output: {flatten_list(nested)}")
    print()

if __name__ == "__main__":
    test_flatten()
