"""
题目15：Valid Parentheses
难度：⭐ (Easy)
来源：Microsoft, Goldman Sachs (LeetCode 20)
考点：栈、字符串处理

题目描述：
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

Example:
Input: "([)]"
Output: False

Input: "()[]{}"
Output: True
"""

def is_valid_parentheses(s):
    """
    Solution 15: 有效括号

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            # Closing bracket
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            # Opening bracket
            stack.append(char)

    return len(stack) == 0

# Test
def test_valid_parentheses():
    test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    print("题目15 - 有效括号:")
    for s in test_cases:
        print(f"Input: {s}, Valid: {is_valid_parentheses(s)}")
    print()

if __name__ == "__main__":
    test_valid_parentheses()
