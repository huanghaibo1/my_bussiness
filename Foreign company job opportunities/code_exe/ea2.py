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
import pandas as pd
import numpy as np

def analyze_sales(df):
    """
    Solution 2: 数据分组聚合
    """
    # Calculate revenue
    df['revenue'] = df['price'] * df['quantity']
    print("计算收入后的数据:")
    print(df)
    print()

    # Group by product and aggregate
    summary = df.groupby('product').agg({
        'revenue': 'sum',
        'price': 'mean',
        'category': 'count'  # Count occurrences
    }).reset_index()
    print("分组聚合后的数据:")
    print(summary)
    print()

    # Rename columns
    summary.columns = ['product', 'total_revenue', 'avg_price', 'num_sales']
    print("重命名列后的数据:")
    print(summary)      

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

if __name__ == "__main__":
    test_analyze_sales()    