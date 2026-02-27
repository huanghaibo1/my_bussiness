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
import pandas as pd
import numpy as np

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
    print("原始数据:")
    print(df)   

    result = pivot_sales_data(df)
    print("题目3 - 数据透视:")
    print(result)
    print()

if __name__ == "__main__":
    test_pivot_sales()
