# 外企数据岗位 Python 笔试题库 🐍

> 基于真实公司面试题 | Microsoft, Amazon, Accenture, Goldman Sachs等
> 包含22道高频题目 + 详细解答

---

## 📋 题库概览

| 类别 | 数量 | 重要性 | 占比 |
|------|------|--------|------|
| 数据处理 (Pandas/Numpy) | 5题 | ⭐⭐⭐⭐⭐ | 40-50% |
| 字符串和列表 | 5题 | ⭐⭐⭐⭐⭐ | 20-30% |
| 字典操作 | 3题 | ⭐⭐⭐⭐ | 15-20% |
| 算法基础 | 5题 | ⭐⭐⭐⭐ | 15-20% |
| 实际场景 | 4题 | ⭐⭐⭐⭐ | 20-25% |

---

## 🎯 学习策略

### 按公司类型准备

**科技公司 (Microsoft, Amazon, Apple)**:
- 重点：算法基础 + Pandas数据处理
- 难度：Medium为主
- 时间：45-60分钟实时编码

**咨询公司 (Accenture, Deloitte, PwC)**:
- 重点：数据清洗 + 实际场景
- 难度：Easy-Medium
- 时间：30-45分钟

**金融机构 (HSBC, Goldman Sachs, Citi)**:
- 重点：数据处理 + 数据验证
- 难度：Medium-Hard
- 时间：60分钟

### 刷题计划

```
Week 1: 数据处理 (5题) + 字符串列表 (前3题)
Week 2: 字符串列表 (后2题) + 字典 (3题)
Week 3: 算法基础 (5题)
Week 4: 实际场景 (4题) + 总复习
```

---

## 📚 第一部分：数据处理 (Pandas/Numpy) ⭐⭐⭐⭐⭐

### 题目1: 数据清洗 - 处理缺失值和重复值
**难度**: ⭐⭐ Medium
**来源**: Microsoft, Accenture
**考点**: pandas基础、数据清洗

**题目描述**:
```
Given a DataFrame with missing values and duplicates, clean the data by:
1. Remove duplicate rows
2. Fill missing values in 'age' column with the mean
3. Drop rows where 'name' is missing
4. Return the cleaned DataFrame

Input DataFrame:
   name   age  city
0  Alice  25.0  NYC
1  Bob    NaN   LA
2  Alice  25.0  NYC
3  NaN    30.0  SF
4  David  35.0  NaN
```

**解答**:
```python
import pandas as pd
import numpy as np

def clean_dataframe(df):
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
```

**关键点**:
- `drop_duplicates()` - 去重
- `fillna()` - 填充缺失值
- `dropna(subset=[])` - 删除特定列的缺失值
- `reset_index()` - 重置索引

**时间复杂度**: O(n)
**空间复杂度**: O(1) - in-place操作

---

### 题目2: 数据分组聚合
**难度**: ⭐⭐⭐ Medium
**来源**: Amazon, Goldman Sachs
**考点**: groupby、聚合函数

**题目描述**:
```
Given a sales DataFrame, calculate:
1. Total revenue per product
2. Average price per product
3. Number of sales per product

Input:
   product  category     price  quantity
0  iPhone   Electronics  1000   2
1  MacBook  Electronics  2000   1
2  iPhone   Electronics  1000   3
3  AirPods  Electronics  200    5
```

**解答**:
```python
def analyze_sales(df):
    # Calculate revenue
    df['revenue'] = df['price'] * df['quantity']

    # Group by product and aggregate
    summary = df.groupby('product').agg({
        'revenue': 'sum',
        'price': 'mean',
        'product': 'count'
    }).reset_index()

    # Rename columns
    summary.columns = ['product', 'total_revenue', 'avg_price', 'num_sales']

    return summary.sort_values('product')
```

**关键点**:
- `groupby()` - 分组
- `agg()` - 多种聚合函数
- `reset_index()` - 将索引变回列

**常见聚合函数**:
- `sum()`, `mean()`, `count()`, `min()`, `max()`
- `std()`, `var()`, `median()`

**时间复杂度**: O(n log n) - 因为有排序
**空间复杂度**: O(n)

---

### 题目3: 数据透视 (Pivot)
**难度**: ⭐⭐⭐ Medium-Hard
**来源**: Accenture, Deloitte
**考点**: pivot、数据重塑

**题目描述**:
```
Convert long-format to wide-format data.

Input:
   date        product  sales
0  2024-01-01  A        100
1  2024-01-01  B        200
2  2024-01-02  A        150
3  2024-01-02  B        250

Output:
date        A    B
2024-01-01  100  200
2024-01-02  150  250
```

**解答**:
```python
def pivot_sales_data(df):
    pivoted = df.pivot(index='date', columns='product', values='sales')
    return pivoted

# 如果有重复值，使用 pivot_table
def pivot_with_duplicates(df):
    pivoted = df.pivot_table(
        index='date',
        columns='product',
        values='sales',
        aggfunc='sum'  # 或 'mean', 'count'
    )
    return pivoted
```

**关键点**:
- `pivot()` - 无重复时使用
- `pivot_table()` - 有重复时使用，需要指定聚合函数
- `index` - 行索引
- `columns` - 列名
- `values` - 填充的值

**时间复杂度**: O(n)
**空间复杂度**: O(n)

---

### 题目4: 时间序列处理
**难度**: ⭐⭐⭐ Medium
**来源**: HSBC, JPMorgan
**考点**: datetime、resample、滚动窗口

**题目描述**:
```
Given timestamps and values, calculate:
1. Daily average
2. 7-day rolling average
3. Month-over-month growth rate
```

**解答**:
```python
def analyze_timeseries(df):
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
```

**常用时间频率**:
- `'D'` - 天
- `'W'` - 周
- `'M'` - 月
- `'Q'` - 季度
- `'Y'` - 年
- `'H'` - 小时

**关键函数**:
- `pd.to_datetime()` - 转换为日期
- `resample()` - 重采样
- `rolling()` - 滚动窗口
- `pct_change()` - 百分比变化

---

### 题目5: 数据合并 (Join)
**难度**: ⭐⭐⭐ Medium
**来源**: Microsoft, Amazon
**考点**: merge、多表关联

**题目描述**:
```
Join three DataFrames (orders, customers, products)
to create a complete order report.
```

**解答**:
```python
def merge_order_data(orders, customers, products):
    # Merge orders with customers
    result = orders.merge(customers, on='customer_id', how='left')

    # Merge with products
    result = result.merge(products, on='product_id', how='left')

    # Select columns
    result = result[['order_id', 'customer_name', 'product_name',
                     'quantity', 'price', 'order_date']]

    return result
```

**Join类型**:
- `how='inner'` - 内连接（交集）
- `how='left'` - 左连接（保留左表所有记录）
- `how='right'` - 右连接（保留右表所有记录）
- `how='outer'` - 外连接（并集）

**时间复杂度**: O(n + m)
**空间复杂度**: O(n + m)

---

## 📚 第二部分：字符串和列表 ⭐⭐⭐⭐⭐

### 题目6: 字符串分析
**难度**: ⭐ Easy
**来源**: 基础题
**考点**: 字符串操作、列表推导式

**题目描述**:
```
Given a sentence, return:
1. Reversed sentence (word order)
2. Unique words (case-insensitive)
3. Word count

Input: "Hello World Hello Python"
Output:
- Reversed: "Python Hello World Hello"
- Unique: ['hello', 'world', 'python']
- Count: 4
```

**解答**:
```python
def analyze_sentence(sentence):
    words = sentence.split()

    # Reversed
    reversed_sentence = ' '.join(reversed(words))

    # Unique words
    unique_words = list(set(word.lower() for word in words))
    unique_words.sort()

    # Count
    word_count = len(words)

    return {
        'reversed': reversed_sentence,
        'unique': unique_words,
        'count': word_count
    }
```

**常用字符串方法**:
- `split()` - 分割
- `join()` - 连接
- `lower()`, `upper()` - 大小写转换
- `strip()` - 去除空白
- `replace()` - 替换

**时间复杂度**: O(n)
**空间复杂度**: O(n)

---

### 题目7: Top K 频率元素
**难度**: ⭐⭐ Easy-Medium
**来源**: Amazon, Microsoft
**考点**: Counter、哈希表

**题目描述**:
```
Find the top K most frequent elements.

Input: [1, 1, 1, 2, 2, 3], k=2
Output: [1, 2]
```

**解答**:
```python
from collections import Counter

def top_k_frequent(nums, k):
    counter = Counter(nums)
    top_k = [item for item, count in counter.most_common(k)]
    return top_k

# 方法2: 使用heap（大数据集更高效）
import heapq

def top_k_frequent_heap(nums, k):
    counter = Counter(nums)
    return heapq.nlargest(k, counter.keys(), key=counter.get)
```

**关键点**:
- `Counter()` - 统计频率
- `most_common(k)` - 获取前k个
- `heapq.nlargest()` - 堆实现

**时间复杂度**:
- Counter方法: O(n log n)
- Heap方法: O(n log k) - 更优

**空间复杂度**: O(n)

---

### 题目8: 合并区间
**难度**: ⭐⭐⭐ Medium
**来源**: Amazon (LeetCode 56)
**考点**: 排序、区间处理

**题目描述**:
```
Merge overlapping intervals.

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
```

**解答**:
```python
def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        if current[0] <= last[1]:  # Overlapping
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged
```

**关键思路**:
1. 先按起始位置排序
2. 遍历，检查当前区间是否与上一个重叠
3. 重叠则合并，否则添加新区间

**时间复杂度**: O(n log n) - 排序主导
**空间复杂度**: O(n)

---

### 题目9: 去重保持顺序
**难度**: ⭐⭐ Easy-Medium
**来源**: Accenture, Deloitte
**考点**: 集合、顺序保持

**题目描述**:
```
Remove duplicates while preserving order.

Input: [1, 2, 3, 2, 4, 3, 5]
Output: [1, 2, 3, 4, 5]
```

**解答**:
```python
# 方法1: 使用set和list
def remove_duplicates(lst):
    seen = set()
    result = []

    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

# 方法2: 使用dict (Python 3.7+保序)
def remove_duplicates_dict(lst):
    return list(dict.fromkeys(lst))
```

**时间复杂度**: O(n)
**空间复杂度**: O(n)

---

### 题目10: Flatten嵌套列表
**难度**: ⭐⭐ Medium
**来源**: Microsoft, Goldman Sachs
**考点**: 递归、列表操作

**题目描述**:
```
Flatten a nested list of arbitrary depth.

Input: [1, [2, 3, [4, 5]], 6, [7]]
Output: [1, 2, 3, 4, 5, 6, 7]
```

**解答**:
```python
def flatten_list(nested_list):
    result = []

    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))  # Recursive
        else:
            result.append(item)

    return result

# 方法2: 使用generator（内存高效）
def flatten_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_generator(item)
        else:
            yield item

# 使用: list(flatten_generator(nested_list))
```

**时间复杂度**: O(n) - n是总元素数
**空间复杂度**: O(d) - d是最大深度（递归栈）

---

## 📚 第三部分：字典操作 ⭐⭐⭐⭐

### 题目11: 字典反转
**难度**: ⭐⭐ Easy-Medium
**来源**: Accenture
**考点**: 字典操作

**题目描述**:
```
Reverse dictionary keys and values.
If multiple keys have same value, collect them in a list.

Input: {'a': 1, 'b': 2, 'c': 1, 'd': 3}
Output: {1: ['a', 'c'], 2: ['b'], 3: ['d']}
```

**解答**:
```python
def reverse_dictionary(d):
    reversed_dict = {}

    for key, value in d.items():
        if value not in reversed_dict:
            reversed_dict[value] = []
        reversed_dict[value].append(key)

    return reversed_dict

# 方法2: 使用defaultdict
from collections import defaultdict

def reverse_dict_defaultdict(d):
    reversed_dict = defaultdict(list)
    for key, value in d.items():
        reversed_dict[value].append(key)
    return dict(reversed_dict)
```

**时间复杂度**: O(n)
**空间复杂度**: O(n)

---

### 题目12: 合并多个字典
**难度**: ⭐⭐ Medium
**来源**: Microsoft, Amazon
**考点**: 字典合并、值累加

**题目描述**:
```
Merge dictionaries and sum values for duplicate keys.

Input: [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 5}]
Output: {'a': 6, 'b': 5, 'c': 4}
```

**解答**:
```python
def merge_dictionaries(dicts):
    result = {}

    for d in dicts:
        for key, value in d.items():
            result[key] = result.get(key, 0) + value

    return result

# 方法2: 使用Counter
from collections import Counter

def merge_dicts_counter(dicts):
    result = Counter()
    for d in dicts:
        result.update(d)
    return dict(result)
```

**时间复杂度**: O(n×m) - n个字典，平均m个键
**空间复杂度**: O(k) - k个唯一键

---

### 题目13: 字典排序
**难度**: ⭐⭐ Easy-Medium
**来源**: 通用题
**考点**: 排序

**题目描述**:
```
Sort dictionary by values (descending), then keys (ascending).

Input: {'apple': 3, 'banana': 1, 'cherry': 3, 'date': 2}
Output: [('apple', 3), ('cherry', 3), ('date', 2), ('banana', 1)]
```

**解答**:
```python
def sort_dictionary(d):
    # Sort by value (desc), then key (asc)
    sorted_items = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items
```

**时间复杂度**: O(n log n)
**空间复杂度**: O(n)

---

## 📚 第四部分：算法基础 ⭐⭐⭐⭐

### 题目14: Two Sum
**难度**: ⭐ Easy
**来源**: Amazon, Microsoft (LeetCode 1)
**考点**: 哈希表

**题目描述**:
```
Find two numbers that add up to target.

Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
```

**解答**:
```python
def two_sum(nums, target):
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []
```

**时间复杂度**: O(n)
**空间复杂度**: O(n)

---

### 题目15: 有效括号
**难度**: ⭐ Easy
**来源**: Microsoft, Goldman Sachs (LeetCode 20)
**考点**: 栈

**题目描述**:
```
Check if parentheses are valid.

Input: "([)]"
Output: False

Input: "()[]{}"
Output: True
```

**解答**:
```python
def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:  # Closing bracket
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:  # Opening bracket
            stack.append(char)

    return len(stack) == 0
```

**关键思路**:
- 遇到左括号，入栈
- 遇到右括号，检查栈顶是否匹配
- 最后栈必须为空

**时间复杂度**: O(n)
**空间复杂度**: O(n)

---

### 题目16: 最大子数组和 (Kadane's Algorithm)
**难度**: ⭐⭐ Easy-Medium
**来源**: Microsoft, Amazon (LeetCode 53)
**考点**: 动态规划

**题目描述**:
```
Find the maximum sum of a contiguous subarray.

Input: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6 (subarray [4,-1,2,1])
```

**解答**:
```python
def max_subarray(nums):
    if not nums:
        return 0

    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        # Either extend or start new
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum
```

**关键思路**:
- 每个位置选择：要么加入当前子数组，要么重新开始
- `current_sum = max(num, current_sum + num)`

**时间复杂度**: O(n)
**空间复杂度**: O(1)

---

### 题目17: 二分查找
**难度**: ⭐⭐ Easy
**来源**: 基础算法
**考点**: 二分搜索

**题目描述**:
```
Find target in sorted array using binary search.

Input: nums = [1, 3, 5, 7, 9, 11], target = 7
Output: 3
```

**解答**:
```python
def binary_search(nums, target):
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
```

**时间复杂度**: O(log n)
**空间复杂度**: O(1)

---

### 题目18: 斐波那契数列
**难度**: ⭐ Easy
**来源**: 基础题
**考点**: 递归、DP

**题目描述**:
```
Calculate nth Fibonacci number.

Input: n = 6
Output: 8
```

**解答**:
```python
# 方法1: 迭代（推荐）
def fibonacci(n):
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr

# 方法2: 递归 + 记忆化
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]
```

**时间复杂度**:
- 迭代: O(n)
- 递归+memo: O(n)
- 纯递归: O(2^n) - 不推荐

**空间复杂度**:
- 迭代: O(1)
- 递归+memo: O(n)

---

## 📚 第五部分：实际场景 ⭐⭐⭐⭐

### 题目19: 解析JSON
**难度**: ⭐⭐ Medium
**来源**: Microsoft, Amazon
**考点**: JSON处理、数据扁平化

**题目描述**:
```
Parse JSON strings and flatten nested structure into DataFrame.

Input:
[
  '{"id": 1, "name": "Alice", "address": {"city": "NYC", "zip": "10001"}}',
  '{"id": 2, "name": "Bob", "address": {"city": "LA", "zip": "90001"}}'
]

Output DataFrame:
   id  name  city  zip
0  1   Alice NYC   10001
1  2   Bob   LA    90001
```

**解答**:
```python
import json
import pandas as pd

def parse_json_to_dataframe(json_strings):
    data = []

    for json_str in json_strings:
        obj = json.loads(json_str)

        # Flatten
        flat_obj = {
            'id': obj['id'],
            'name': obj['name'],
            'city': obj['address']['city'],
            'zip': obj['address']['zip']
        }
        data.append(flat_obj)

    return pd.DataFrame(data)
```

**关键点**:
- `json.loads()` - 解析JSON字符串
- 手动扁平化嵌套结构
- 创建DataFrame

**时间复杂度**: O(n×m) - n条记录，m个字段
**空间复杂度**: O(n×m)

---

### 题目20: 数据验证
**难度**: ⭐⭐⭐ Medium
**来源**: Consulting firms, Financial companies
**考点**: 数据质量检查

**题目描述**:
```
Validate DataFrame and return error report:
1. Check null values in required columns
2. Validate email format
3. Validate age range (0-120)
```

**解答**:
```python
import re

def validate_data(df):
    errors = {
        'null_values': {},
        'invalid_email': [],
        'invalid_age': []
    }

    # Check nulls
    required_cols = ['name', 'email']
    for col in required_cols:
        null_indices = df[df[col].isnull()].index.tolist()
        if null_indices:
            errors['null_values'][col] = null_indices

    # Validate email
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    for idx, email in df['email'].items():
        if pd.notna(email) and not re.match(email_pattern, str(email)):
            errors['invalid_email'].append(idx)
        elif pd.isna(email):
            errors['invalid_email'].append(idx)

    # Validate age
    for idx, age in df['age'].items():
        if pd.notna(age) and (age < 0 or age > 120):
            errors['invalid_age'].append(idx)

    return errors
```

**关键点**:
- 正则表达式验证格式
- 范围检查
- 返回详细错误报告

---

### 题目21: SQL结果转换
**难度**: ⭐⭐ Medium
**来源**: 数据工程岗位
**考点**: 数据转换

**题目描述**:
```
Convert SQL query result (list of tuples) to:
1. List of dictionaries
2. Dictionary grouped by a key

Input: [('Alice', 'Sales', 5000), ('Bob', 'IT', 6000)]
Columns: ['name', 'department', 'salary']
```

**解答**:
```python
def convert_sql_result(rows, columns):
    # 1. List of dicts
    list_of_dicts = [dict(zip(columns, row)) for row in rows]

    # 2. Grouped by department
    grouped = {}
    for row in rows:
        dept = row[1]  # department
        if dept not in grouped:
            grouped[dept] = []
        grouped[dept].append({
            'name': row[0],
            'salary': row[2]
        })

    return list_of_dicts, grouped
```

**关键技巧**:
- `zip()` 配对列名和值
- `dict()` 创建字典
- 列表推导式

---

### 题目22: 批量文件处理
**难度**: ⭐⭐⭐ Medium-Hard
**来源**: Real ETL scenarios
**考点**: 文件处理、错误处理

**题目描述**:
```
Process multiple CSV files in a directory:
1. Read all CSV files
2. Validate and clean data
3. Combine into one DataFrame
4. Handle errors gracefully
```

**解答**:
```python
import os
import pandas as pd
from pathlib import Path

def process_csv_files(directory):
    all_data = []
    errors = []

    # Get all CSV files
    csv_files = Path(directory).glob('*.csv')

    for file_path in csv_files:
        try:
            # Read file
            df = pd.read_csv(file_path)

            # Validate
            required_cols = ['id', 'date', 'value']
            if not all(col in df.columns for col in required_cols):
                errors.append(f"{file_path}: Missing required columns")
                continue

            # Clean
            df = df.dropna(subset=required_cols)
            df['file_source'] = file_path.name

            all_data.append(df)

        except Exception as e:
            errors.append(f"{file_path}: {str(e)}")
            continue

    # Combine all
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        return combined_df, errors
    else:
        return None, errors
```

**关键点**:
- `Path.glob()` - 匹配文件
- `try-except` - 错误处理
- `pd.concat()` - 合并多个DataFrame

---

## 🎯 面试技巧

### 1. 解题步骤

```
1. 澄清需求 (1-2分钟)
   - 输入格式和范围
   - 输出要求
   - Edge cases
   - 性能要求

2. 说明思路 (2-3分钟)
   - 用英文讲解approach
   - 分析时间空间复杂度
   - 讨论trade-offs

3. 编写代码 (10-15分钟)
   - 边写边讲解
   - 写clean code
   - 使用有意义的变量名

4. 测试验证 (3-5分钟)
   - 走一遍正常case
   - 检查edge cases
   - 考虑优化
```

### 2. 英文表达

**开场**:
- "Let me make sure I understand the problem..."
- "Can I clarify a few things?"
- "Here's my approach..."

**分析**:
- "The time complexity would be O(n)"
- "We can optimize this by using a hash table"
- "The trade-off here is..."

**编码中**:
- "First, I'll handle the edge case..."
- "Let me add a helper function for..."
- "This variable represents..."

**检查**:
- "Let me walk through an example"
- "I should check for null values here"
- "One optimization could be..."

### 3. 常见错误

❌ **不要做**:
- 直接开始写代码
- 沉默不语
- 写完不测试
- 忽略edge cases
- 变量名太随意

✅ **要做**:
- Think out loud
- 写清晰的代码
- 考虑边界情况
- 讨论优化方案
- 测试你的代码

---

## 📝 练习计划

### Week 1: 数据处理基础
**目标**: 掌握Pandas核心操作

| 日期 | 题目 | 时间 |
|------|------|------|
| Day 1 | 题目1 - 数据清洗 | 30分钟 |
| Day 2 | 题目2 - 分组聚合 | 30分钟 |
| Day 3 | 题目3 - 数据透视 | 45分钟 |
| Day 4 | 题目4 - 时间序列 | 45分钟 |
| Day 5 | 题目5 - 数据合并 | 30分钟 |
| Day 6-7 | 复习+LeetCode Pandas题 | 2小时 |

### Week 2: 字符串和字典
**目标**: 熟练基础数据结构

| 日期 | 题目 | 时间 |
|------|------|------|
| Day 1-2 | 题目6-10 (字符串列表) | 各30分钟 |
| Day 3-4 | 题目11-13 (字典) | 各30分钟 |
| Day 5 | 综合练习 | 1小时 |
| Day 6-7 | 复习+额外题目 | 2小时 |

### Week 3: 算法基础
**目标**: 掌握基础算法

| 日期 | 题目 | 时间 |
|------|------|------|
| Day 1-5 | 题目14-18 (算法) | 各45分钟 |
| Day 6-7 | LeetCode Easy题10道 | 3小时 |

### Week 4: 实战模拟
**目标**: 综合应用

| 日期 | 任务 | 时间 |
|------|------|------|
| Day 1-3 | 题目19-22 (实际场景) | 各1小时 |
| Day 4-5 | 模拟完整面试 | 各1.5小时 |
| Day 6-7 | 复习薄弱环节 | 3小时 |

---

## 💻 推荐资源

### 在线刷题平台
- **LeetCode** - Pandas题目 + 算法题
- **HackerRank** - Python + SQL
- **StrataScratch** - 真实公司数据题
- **DataLemur** - 数据分析师题库

### 学习资源
- **书籍**:
  - 《Python for Data Analysis》 - Wes McKinney
  - 《Pandas Cookbook》

- **课程**:
  - DataCamp - Pandas课程
  - Coursera - Python for Data Science

### Mock Interview
- **Pramp** - 免费peer interview
- **interviewing.io** - 技术面试练习

---

## 🚀 最后的话

**重点准备顺序**:
1. Pandas数据处理 (40-50%面试内容)
2. 基础算法 (Two Sum, 字符串等)
3. 实际场景题 (ETL, 数据清洗)
4. 练习英文表达

**每天练习**:
- 工作日: 1-2道题 (1-1.5小时)
- 周末: 3-5道题 (2-3小时)
- 4周可以准备充分

**面试前**:
- 快速过一遍所有题目
- 练习英文讲解思路
- 准备3-5个常见题的模板

**Good luck with your Python interviews! 💪🐍**

---

## 📁 相关文件

- [python_interview_questions.py](./python_interview_questions.py) - 完整代码
- [INTERVIEW_QUICK_GUIDE.md](./INTERVIEW_QUICK_GUIDE.md) - 面试总指南
- [interview_prep_complete.json](./interview_prep_complete.json) - 完整准备材料
