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
import pandas as pd
import numpy as np

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

if __name__ == "__main__":
    test_merge_data()
