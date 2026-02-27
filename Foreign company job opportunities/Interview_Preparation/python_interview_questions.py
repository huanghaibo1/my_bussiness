#!/usr/bin/env python3
"""
外企数据岗位 Python 笔试题库
包含真实公司面试题和高频考点
适用于：Microsoft, Amazon, Accenture, 金融机构等
"""

"""
======================================================================================
题库结构
======================================================================================
1. 数据处理类 (Pandas/Numpy) - 数据岗位核心 ⭐⭐⭐⭐⭐
2. 字符串和列表操作 - 基础必考 ⭐⭐⭐⭐⭐
3. 字典和集合操作 - 高频考点 ⭐⭐⭐⭐
4. 算法基础 - LeetCode Easy/Medium ⭐⭐⭐⭐
5. 实际场景题 - ETL/数据清洗 ⭐⭐⭐⭐

每道题包含：
- 题目描述（中英文）
- 难度等级
- 真实公司来源
- 详细解答
- 时间复杂度
- 考点分析
"""


# ======================================================================================
# 第一部分：数据处理类（Pandas/Numpy）⭐⭐⭐⭐⭐
# 重要性：数据岗位最常考，占比40-50%
# ======================================================================================

"""
题目1：数据清洗 - 处理缺失值和重复值
难度：⭐⭐ (Medium)
来源：Microsoft, Accenture
考点：pandas基础操作、数据清洗

题目描述：
Given a DataFrame with missing values and duplicates, clean the data by:
1. Remove duplicate rows
2. Fill missing values in 'age' column with the mean
3. Drop rows where 'name' is missing
4. Return the cleaned DataFrame

Example:
Input:
   name   age  city
0  Alice  25.0  NYC
1  Bob    NaN  LA
2  Alice  25.0  NYC
3  NaN    30.0 SF
4  David  35.0 NaN

Output:
   name   age  city
0  Alice  25.0  NYC
1  Bob    30.0  LA
4  David  35.0  NaN
"""

import pandas as pd
import numpy as np

def clean_dataframe(df):
    """
    Solution 1: 数据清洗
    """
    # 1. Remove duplicates
    df = df.drop_duplicates()

    # 2. Fill missing age with mean
    mean_age = df['age'].mean()
    df['age'] = df['age'].fillna(mean_age)

    # 3. Drop rows where name is missing
    df = df.dropna(subset=['name'])

    # Reset index
    df = df.reset_index(drop=True)

    return df

# Test
def test_clean_dataframe():
    data = {
        'name': ['Alice', 'Bob', 'Alice', None, 'David'],
        'age': [25.0, np.nan, 25.0, 30.0, 35.0],
        'city': ['NYC', 'LA', 'NYC', 'SF', None]
    }
    df = pd.DataFrame(data)

    result = clean_dataframe(df)
    print("题目1 - 数据清洗:")
    print(result)
    print()


"""
题目2：数据分组聚合
难度：⭐⭐⭐ (Medium)
来源：Amazon, Goldman Sachs
考点：groupby, 聚合函数, 多列操作

题目描述：
Given a sales DataFrame, calculate:
1. Total revenue per product
2. Average price per category
3. Number of sales per product
Return a summary DataFrame with all three metrics

Example:
Input:
   product  category  price  quantity
0  iPhone   Electronics  1000  2
1  MacBook  Electronics  2000  1
2  iPhone   Electronics  1000  3
3  AirPods  Electronics  200   5
4  Desk     Furniture    500   2

Output:
   product  total_revenue  avg_price  num_sales
0  AirPods  1000          200.0      1
1  Desk     1000          500.0      1
2  iPhone   5000          1000.0     2
3  MacBook  2000          2000.0     1
"""

def analyze_sales(df):
    """
    Solution 2: 数据分组聚合
    """
    # Calculate revenue
    df['revenue'] = df['price'] * df['quantity']

    # Group by product and aggregate
    summary = df.groupby('product').agg({
        'revenue': 'sum',
        'price': 'mean',
        'product': 'count'  # Count occurrences
    }).reset_index()

    # Rename columns
    summary.columns = ['product', 'total_revenue', 'avg_price', 'num_sales']

    return summary.sort_values('product')

# Test
def test_analyze_sales():
    data = {
        'product': ['iPhone', 'MacBook', 'iPhone', 'AirPods', 'Desk'],
        'category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Furniture'],
        'price': [1000, 2000, 1000, 200, 500],
        'quantity': [2, 1, 3, 5, 2]
    }
    df = pd.DataFrame(data)

    result = analyze_sales(df)
    print("题目2 - 数据分组聚合:")
    print(result)
    print()


"""
题目3：数据转换 - Pivot操作
难度：⭐⭐⭐ (Medium-Hard)
来源：Accenture, Deloitte
考点：pivot, reshape, 数据透视

题目描述：
Given a long-format DataFrame, convert it to wide format using pivot.
Each row should represent a date, and columns should be different products with their sales values.

Example:
Input:
   date       product  sales
0  2024-01-01  A        100
1  2024-01-01  B        200
2  2024-01-02  A        150
3  2024-01-02  B        250

Output:
date        A    B
2024-01-01  100  200
2024-01-02  150  250
"""

def pivot_sales_data(df):
    """
    Solution 3: 数据透视
    """
    pivoted = df.pivot(index='date', columns='product', values='sales')
    return pivoted

# Test
def test_pivot_sales():
    data = {
        'date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
        'product': ['A', 'B', 'A', 'B'],
        'sales': [100, 200, 150, 250]
    }
    df = pd.DataFrame(data)

    result = pivot_sales_data(df)
    print("题目3 - 数据透视:")
    print(result)
    print()


"""
题目4：时间序列处理
难度：⭐⭐⭐ (Medium)
来源：HSBC, JPMorgan
考点：datetime, resample, 时间窗口

题目描述：
Given a DataFrame with timestamps and values, calculate:
1. Daily average
2. 7-day rolling average
3. Month-over-month growth rate

Example:
Input:
   timestamp           value
0  2024-01-01 10:00:00  100
1  2024-01-01 14:00:00  150
2  2024-01-02 09:00:00  200
3  2024-01-02 15:00:00  180
...
"""

def analyze_timeseries(df):
    """
    Solution 4: 时间序列分析
    """
    # Convert to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.set_index('timestamp')

    # Daily average
    daily_avg = df.resample('D').mean()

    # 7-day rolling average
    daily_avg['rolling_7d'] = daily_avg['value'].rolling(window=7).mean()

    # Month-over-month growth
    monthly = df.resample('M').sum()
    monthly['mom_growth'] = monthly['value'].pct_change() * 100

    return daily_avg, monthly

# Test
def test_timeseries():
    dates = pd.date_range('2024-01-01', periods=30, freq='12H')
    data = {
        'timestamp': dates,
        'value': np.random.randint(100, 200, 30)
    }
    df = pd.DataFrame(data)

    daily, monthly = analyze_timeseries(df)
    print("题目4 - 时间序列分析:")
    print("Daily averages (first 5):")
    print(daily.head())
    print()


"""
题目5：数据合并 - Join操作
难度：⭐⭐⭐ (Medium)
来源：Microsoft, Amazon
考点：merge, join, 多表关联

题目描述：
Given three DataFrames (orders, customers, products),
join them to create a complete order report with customer names and product details.

Handle missing values appropriately.
"""

def merge_order_data(orders, customers, products):
    """
    Solution 5: 多表关联
    """
    # Merge orders with customers
    result = orders.merge(customers, on='customer_id', how='left')

    # Merge with products
    result = result.merge(products, on='product_id', how='left')

    # Select and rename columns
    result = result[['order_id', 'customer_name', 'product_name',
                     'quantity', 'price', 'order_date']]

    return result

# Test
def test_merge_data():
    orders = pd.DataFrame({
        'order_id': [1, 2, 3],
        'customer_id': [101, 102, 101],
        'product_id': [1, 2, 1],
        'quantity': [2, 1, 3],
        'order_date': ['2024-01-01', '2024-01-02', '2024-01-03']
    })

    customers = pd.DataFrame({
        'customer_id': [101, 102, 103],
        'customer_name': ['Alice', 'Bob', 'Charlie']
    })

    products = pd.DataFrame({
        'product_id': [1, 2, 3],
        'product_name': ['iPhone', 'MacBook', 'iPad'],
        'price': [1000, 2000, 800]
    })

    result = merge_order_data(orders, customers, products)
    print("题目5 - 数据合并:")
    print(result)
    print()


# ======================================================================================
# 第二部分：字符串和列表操作 ⭐⭐⭐⭐⭐
# 重要性：基础必考，占比20-30%
# ======================================================================================

"""
题目6：字符串反转和去重
难度：⭐ (Easy)
来源：所有公司基础题
考点：字符串操作、列表推导式

题目描述：
Write a function that takes a sentence and returns:
1. Reversed sentence (word order)
2. Unique words (case-insensitive)
3. Word count

Example:
Input: "Hello World Hello Python"
Output:
- Reversed: "Python Hello World Hello"
- Unique: ['hello', 'world', 'python']
- Count: 4
"""

def analyze_sentence(sentence):
    """
    Solution 6: 字符串分析

    Time Complexity: O(n) where n is length of sentence
    Space Complexity: O(n)
    """
    words = sentence.split()

    # Reversed sentence
    reversed_sentence = ' '.join(reversed(words))

    # Unique words (case-insensitive)
    unique_words = list(set(word.lower() for word in words))
    unique_words.sort()

    # Word count
    word_count = len(words)

    return {
        'reversed': reversed_sentence,
        'unique': unique_words,
        'count': word_count
    }

# Test
def test_analyze_sentence():
    result = analyze_sentence("Hello World Hello Python")
    print("题目6 - 字符串分析:")
    print(result)
    print()


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
import heapq

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


"""
题目8：合并区间
难度：⭐⭐⭐ (Medium)
来源：Amazon (LeetCode 56)
考点：排序、区间合并

题目描述：
Given a collection of intervals, merge all overlapping intervals.

Example:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
"""

def merge_intervals(intervals):
    """
    Solution 8: 区间合并

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        # If overlapping, merge
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged

# Test
def test_merge_intervals():
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print("题目8 - 区间合并:")
    print(f"Input: {intervals}")
    print(f"Output: {merge_intervals(intervals)}")
    print()


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


# ======================================================================================
# 第三部分：字典操作 ⭐⭐⭐⭐
# 重要性：高频考点，占比15-20%
# ======================================================================================

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
from collections import defaultdict

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
from collections import Counter

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


# ======================================================================================
# 第四部分：算法基础 ⭐⭐⭐⭐
# 重要性：部分公司必考（Microsoft, Amazon），占比15-20%
# ======================================================================================

"""
题目14：Two Sum
难度：⭐ (Easy)
来源：Amazon, Microsoft (LeetCode 1)
考点：哈希表、双指针

题目描述：
Given an array of integers and a target, return indices of two numbers
that add up to the target.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1] (because nums[0] + nums[1] = 9)
"""

def two_sum(nums, target):
    """
    Solution 14: Two Sum

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []

# Test
def test_two_sum():
    nums = [2, 7, 11, 15]
    target = 9
    print("题目14 - Two Sum:")
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {two_sum(nums, target)}")
    print()


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


# ======================================================================================
# 第五部分：实际场景题（ETL/数据清洗）⭐⭐⭐⭐
# 重要性：数据岗位核心，占比20-25%
# ======================================================================================

"""
题目19：解析JSON并提取字段
难度：⭐⭐ (Medium)
来源：Microsoft, Amazon, Accenture
考点：JSON处理、数据提取

题目描述：
Given a list of JSON strings representing user data, extract and flatten
specific fields into a DataFrame.

Example:
Input:
[
  '{"id": 1, "name": "Alice", "address": {"city": "NYC", "zip": "10001"}}',
  '{"id": 2, "name": "Bob", "address": {"city": "LA", "zip": "90001"}}'
]

Output DataFrame:
   id  name  city   zip
0  1   Alice NYC    10001
1  2   Bob   LA     90001
"""

import json

def parse_json_to_dataframe(json_strings):
    """
    Solution 19: JSON解析

    Time Complexity: O(n*m) where n is number of records, m is avg fields
    Space Complexity: O(n*m)
    """
    data = []

    for json_str in json_strings:
        obj = json.loads(json_str)

        # Flatten nested structure
        flat_obj = {
            'id': obj['id'],
            'name': obj['name'],
            'city': obj['address']['city'],
            'zip': obj['address']['zip']
        }
        data.append(flat_obj)

    return pd.DataFrame(data)

# Test
def test_parse_json():
    json_strings = [
        '{"id": 1, "name": "Alice", "address": {"city": "NYC", "zip": "10001"}}',
        '{"id": 2, "name": "Bob", "address": {"city": "LA", "zip": "90001"}}'
    ]

    result = parse_json_to_dataframe(json_strings)
    print("题目19 - JSON解析:")
    print(result)
    print()


"""
题目20：数据验证和错误处理
难度：⭐⭐⭐ (Medium)
来源：Consulting firms, Financial companies
考点：数据验证、异常处理

题目描述：
Validate a DataFrame and return a report of errors:
1. Check for null values in required columns
2. Check if email format is valid
3. Check if age is within valid range (0-120)
4. Return a summary of all errors found

Example:
Input DataFrame:
   id  name     email           age
0  1   Alice    alice@test.com  25
1  2   None     invalid_email   150
2  3   Charlie  None            -5

Output:
{
  'null_values': {'name': [1], 'email': [2]},
  'invalid_email': [1, 2],
  'invalid_age': [1, 2]
}
"""

import re

def validate_data(df):
    """
    Solution 20: 数据验证

    Time Complexity: O(n*m) where n is rows, m is columns
    Space Complexity: O(k) where k is number of errors
    """
    errors = {
        'null_values': {},
        'invalid_email': [],
        'invalid_age': []
    }

    # Check null values in required columns
    required_cols = ['name', 'email']
    for col in required_cols:
        null_indices = df[df[col].isnull()].index.tolist()
        if null_indices:
            errors['null_values'][col] = null_indices

    # Validate email format
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    for idx, email in df['email'].items():
        if pd.notna(email) and not re.match(email_pattern, str(email)):
            errors['invalid_email'].append(idx)
        elif pd.isna(email):
            errors['invalid_email'].append(idx)

    # Validate age range
    for idx, age in df['age'].items():
        if pd.notna(age) and (age < 0 or age > 120):
            errors['invalid_age'].append(idx)

    return errors

# Test
def test_validate_data():
    data = {
        'id': [1, 2, 3],
        'name': ['Alice', None, 'Charlie'],
        'email': ['alice@test.com', 'invalid_email', None],
        'age': [25, 150, -5]
    }
    df = pd.DataFrame(data)

    errors = validate_data(df)
    print("题目20 - 数据验证:")
    print("Errors found:")
    for error_type, details in errors.items():
        if details:
            print(f"  {error_type}: {details}")
    print()


"""
题目21：处理CSV文件并生成报表
难度：⭐⭐⭐ (Medium-Hard)
来源：Real-world scenario
考点：文件处理、数据清洗、聚合

题目描述：
Read a CSV file, clean the data, and generate a summary report:
1. Remove rows with missing critical data
2. Convert data types appropriately
3. Calculate summary statistics
4. Export cleaned data to new CSV

This simulates a real ETL task.
"""

def process_csv_file(input_file, output_file):
    """
    Solution 21: CSV处理和报表生成

    This would be a complete ETL pipeline in real scenario
    """
    # Read CSV
    df = pd.read_csv(input_file)

    # Data cleaning
    # 1. Remove duplicates
    df = df.drop_duplicates()

    # 2. Handle missing values
    df = df.dropna(subset=['id', 'date'])  # Required fields

    # 3. Convert data types
    df['date'] = pd.to_datetime(df['date'])
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

    # 4. Remove outliers (example: amounts outside 3 std devs)
    mean = df['amount'].mean()
    std = df['amount'].std()
    df = df[(df['amount'] >= mean - 3*std) & (df['amount'] <= mean + 3*std)]

    # Generate summary report
    summary = {
        'total_records': len(df),
        'date_range': f"{df['date'].min()} to {df['date'].max()}",
        'total_amount': df['amount'].sum(),
        'avg_amount': df['amount'].mean(),
        'categories': df['category'].value_counts().to_dict()
    }

    # Export cleaned data
    df.to_csv(output_file, index=False)

    return summary

# Note: This is a template. In real interview, you'd discuss approach rather than full implementation


"""
题目22：SQL结果转Python数据结构
难度：⭐⭐ (Medium)
来源：Data engineering positions
考点：数据转换、字典操作

题目描述：
Given a list of tuples (simulating SQL query result),
convert it to different Python data structures:
1. List of dictionaries
2. Dictionary grouped by a key
3. Pivot table structure

Example:
Input: [('Alice', 'Sales', 5000), ('Bob', 'IT', 6000), ('Charlie', 'Sales', 5500)]
Columns: ['name', 'department', 'salary']

Output 1 (list of dicts):
[
  {'name': 'Alice', 'department': 'Sales', 'salary': 5000},
  {'name': 'Bob', 'department': 'IT', 'salary': 6000},
  ...
]

Output 2 (grouped by department):
{
  'Sales': [{'name': 'Alice', 'salary': 5000}, {'name': 'Charlie', 'salary': 5500}],
  'IT': [{'name': 'Bob', 'salary': 6000}]
}
"""

def convert_sql_result(rows, columns):
    """
    Solution 22: SQL结果转换
    """
    # 1. List of dictionaries
    list_of_dicts = [dict(zip(columns, row)) for row in rows]

    # 2. Grouped by department
    grouped = {}
    for row in rows:
        dept = row[1]  # department column
        if dept not in grouped:
            grouped[dept] = []
        grouped[dept].append({
            'name': row[0],
            'salary': row[2]
        })

    return list_of_dicts, grouped

# Test
def test_convert_sql():
    rows = [('Alice', 'Sales', 5000), ('Bob', 'IT', 6000), ('Charlie', 'Sales', 5500)]
    columns = ['name', 'department', 'salary']

    list_result, grouped_result = convert_sql_result(rows, columns)

    print("题目22 - SQL结果转换:")
    print("\nList of dicts:")
    for item in list_result:
        print(f"  {item}")

    print("\nGrouped by department:")
    for dept, employees in grouped_result.items():
        print(f"  {dept}: {employees}")
    print()


# ======================================================================================
# 运行所有测试
# ======================================================================================

def run_all_tests():
    """
    Run all test cases
    """
    print("="*80)
    print("外企数据岗位 Python 笔试题库 - 测试运行")
    print("="*80)
    print()

    # Part 1: Pandas/Numpy
    print("第一部分：数据处理 (Pandas)")
    print("-"*80)
    test_clean_dataframe()
    test_analyze_sales()
    test_pivot_sales()
    test_timeseries()
    test_merge_data()

    # Part 2: Strings and Lists
    print("\n第二部分：字符串和列表")
    print("-"*80)
    test_analyze_sentence()
    test_top_k()
    test_merge_intervals()
    test_remove_duplicates()
    test_flatten()

    # Part 3: Dictionaries
    print("\n第三部分：字典操作")
    print("-"*80)
    test_reverse_dict()
    test_merge_dicts()
    test_sort_dict()

    # Part 4: Algorithms
    print("\n第四部分：算法基础")
    print("-"*80)
    test_two_sum()
    test_valid_parentheses()
    test_max_subarray()
    test_binary_search()
    test_fibonacci()

    # Part 5: Real-world scenarios
    print("\n第五部分：实际场景")
    print("-"*80)
    test_parse_json()
    test_validate_data()
    test_convert_sql()

    print("="*80)
    print("所有测试完成!")
    print("="*80)


if __name__ == "__main__":
    run_all_tests()
