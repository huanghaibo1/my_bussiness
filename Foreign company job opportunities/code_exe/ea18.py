"""
题目18：Fibonacci Number
难度：⭐ (Easy)
来源：基础算法题
考点：递归、动态规划

题目描述：
Calculate the nth Fibonacci number.
F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n > 1

Example:
Input: n = 6
Output: 8 (sequence: 0, 1, 1, 2, 3, 5, 8)
"""

def fibonacci(n):
    """
    Solution 18: 斐波那契数列 (迭代版)

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n <= 1:
        return n

    prev, curr = 0, 1

    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr

# Recursive with memoization (更接近面试问法)
def fibonacci_memo(n, memo={}):
    """
    Alternative: 递归 + 记忆化

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# Test
def test_fibonacci():
    n = 10
    print("题目18 - 斐波那契数列:")
    print(f"Input: n = {n}")
    print(f"Output (iterative): {fibonacci(n)}")
    print(f"Output (recursive): {fibonacci_memo(n, {})}")
    print()

if __name__ == "__main__":
    test_fibonacci()
