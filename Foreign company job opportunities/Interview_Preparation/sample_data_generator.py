#!/usr/bin/env python3
"""
样例数据生成器
用于Python面试题练习和测试
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import json


# ======================================================================================
# 1. 数据清洗样例数据
# ======================================================================================

def generate_dirty_dataframe():
    """
    生成包含缺失值和重复值的DataFrame
    用于练习数据清洗
    """
    data = {
        'name': ['Alice', 'Bob', 'Alice', None, 'David'],
        'age': [25.0, np.nan, 25.0, 30.0, 35.0],
        'city': ['NYC', 'LA', 'NYC', 'SF', None]
    }
    df = pd.DataFrame(data)
    return df


# ======================================================================================
# 2. 销售数据样例
# ======================================================================================

def generate_sales_data():
    """
    生成销售数据
    用于groupby和聚合练习
    """
    data = {
        'product': ['iPhone', 'MacBook', 'iPhone', 'AirPods', 'Desk'],
        'category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Furniture'],
        'price': [1000, 2000, 1000, 200, 500],
        'quantity': [2, 1, 3, 5, 2]
    }
    df = pd.DataFrame(data)
    return df


# ======================================================================================
# 3. 时间序列数据样例
# ======================================================================================

def generate_timeseries_data(days=30):
    """
    生成时间序列数据
    用于时间序列分析练习

    Args:
        days: 生成多少天的数据
    """
    dates = pd.date_range('2024-01-01', periods=days, freq='12H')
    data = {
        'timestamp': dates,
        'value': np.random.randint(100, 200, len(dates))
    }
    df = pd.DataFrame(data)
    return df


# ======================================================================================
# 4. 多表关联数据样例
# ======================================================================================

def generate_relational_data():
    """
    生成多个关联表的数据
    用于merge/join练习

    Returns:
        orders, customers, products: 三个DataFrame
    """
    # 订单表
    orders = pd.DataFrame({
        'order_id': [1, 2, 3, 4, 5],
        'customer_id': [101, 102, 101, 103, 102],
        'product_id': [1, 2, 1, 3, 2],
        'quantity': [2, 1, 3, 1, 2],
        'order_date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05']
    })

    # 客户表
    customers = pd.DataFrame({
        'customer_id': [101, 102, 103, 104],
        'customer_name': ['Alice', 'Bob', 'Charlie', 'David'],
        'email': ['alice@email.com', 'bob@email.com', 'charlie@email.com', 'david@email.com']
    })

    # 产品表
    products = pd.DataFrame({
        'product_id': [1, 2, 3, 4],
        'product_name': ['iPhone', 'MacBook', 'iPad', 'AirPods'],
        'price': [1000, 2000, 800, 200],
        'category': ['Electronics', 'Electronics', 'Electronics', 'Electronics']
    })

    return orders, customers, products


# ======================================================================================
# 5. 透视表样例数据
# ======================================================================================

def generate_pivot_data():
    """
    生成适合透视的长格式数据
    用于pivot练习
    """
    data = {
        'date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', '2024-01-03'],
        'product': ['A', 'B', 'A', 'B', 'A', 'B'],
        'sales': [100, 200, 150, 250, 120, 220]
    }
    df = pd.DataFrame(data)
    return df


# ======================================================================================
# 6. 用户行为数据样例
# ======================================================================================

def generate_user_behavior_data(num_users=100, num_days=30):
    """
    生成用户行为数据
    用于留存率、活跃度分析练习

    Args:
        num_users: 用户数量
        num_days: 天数
    """
    data = []
    start_date = datetime(2024, 1, 1)

    for user_id in range(1, num_users + 1):
        # 每个用户随机选择一些日期登录
        active_days = random.sample(range(num_days), k=random.randint(5, 20))
        for day in active_days:
            login_date = start_date + timedelta(days=day)
            data.append({
                'user_id': user_id,
                'login_date': login_date.strftime('%Y-%m-%d'),
                'sessions': random.randint(1, 5),
                'duration_minutes': random.randint(5, 120)
            })

    df = pd.DataFrame(data)
    return df


# ======================================================================================
# 7. 金融交易数据样例
# ======================================================================================

def generate_transaction_data(num_transactions=1000):
    """
    生成金融交易数据
    用于异常检测、聚合分析练习

    Args:
        num_transactions: 交易数量
    """
    np.random.seed(42)

    data = {
        'transaction_id': range(1, num_transactions + 1),
        'account_id': np.random.randint(1000, 2000, num_transactions),
        'transaction_date': [
            (datetime(2024, 1, 1) + timedelta(days=random.randint(0, 90))).strftime('%Y-%m-%d')
            for _ in range(num_transactions)
        ],
        'amount': np.random.lognormal(mean=5, sigma=1.5, size=num_transactions).round(2),
        'transaction_type': np.random.choice(['debit', 'credit'], num_transactions),
        'category': np.random.choice(['Food', 'Transport', 'Shopping', 'Bills', 'Entertainment'], num_transactions)
    }

    df = pd.DataFrame(data)
    return df


# ======================================================================================
# 8. 带异常值的数据样例
# ======================================================================================

def generate_data_with_outliers(num_rows=200):
    """
    生成包含异常值的数据
    用于异常检测和数据清洗练习

    Args:
        num_rows: 行数
    """
    np.random.seed(42)

    # 正常数据
    normal_data = np.random.normal(loc=100, scale=15, size=int(num_rows * 0.95))

    # 异常值
    outliers = np.random.choice([0, 300, -50, 500], size=int(num_rows * 0.05))

    # 合并
    all_data = np.concatenate([normal_data, outliers])
    np.random.shuffle(all_data)

    data = {
        'id': range(1, num_rows + 1),
        'value': all_data[:num_rows].round(2),
        'category': np.random.choice(['A', 'B', 'C'], num_rows)
    }

    df = pd.DataFrame(data)
    return df


# ======================================================================================
# 9. JSON格式数据样例
# ======================================================================================

def generate_json_data():
    """
    生成JSON格式的数据字符串列表
    用于JSON解析练习
    """
    json_strings = [
        '{"id": 1, "name": "Alice", "age": 25, "address": {"city": "NYC", "zip": "10001"}}',
        '{"id": 2, "name": "Bob", "age": 30, "address": {"city": "LA", "zip": "90001"}}',
        '{"id": 3, "name": "Charlie", "age": 35, "address": {"city": "SF", "zip": "94101"}}'
    ]
    return json_strings


# ======================================================================================
# 10. 数据验证样例
# ======================================================================================

def generate_invalid_data():
    """
    生成包含各种错误的数据
    用于数据验证练习
    """
    data = {
        'id': [1, 2, 3, 4, 5],
        'name': ['Alice', None, 'Charlie', 'David', 'Eve'],
        'email': ['alice@test.com', 'invalid_email', None, 'david@test.com', 'eve@'],
        'age': [25, 150, -5, 30, 28],
        'salary': [50000, 60000, None, 70000, 80000],
        'join_date': ['2024-01-01', 'invalid_date', '2024-03-01', None, '2024-05-01']
    }
    df = pd.DataFrame(data)
    return df


# ======================================================================================
# 11. 电商订单数据样例（完整场景）
# ======================================================================================

def generate_ecommerce_data():
    """
    生成完整的电商数据场景
    包含用户、订单、商品、评价等多个表
    """
    # 用户表
    users = pd.DataFrame({
        'user_id': range(1, 51),
        'username': [f'user_{i}' for i in range(1, 51)],
        'email': [f'user{i}@email.com' for i in range(1, 51)],
        'register_date': pd.date_range('2023-01-01', periods=50, freq='W').strftime('%Y-%m-%d').tolist(),
        'city': np.random.choice(['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen'], 50)
    })

    # 商品表
    products = pd.DataFrame({
        'product_id': range(1, 21),
        'product_name': [f'Product_{i}' for i in range(1, 21)],
        'category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home'], 20),
        'price': np.random.uniform(50, 500, 20).round(2),
        'stock': np.random.randint(0, 100, 20)
    })

    # 订单表
    num_orders = 200
    orders = pd.DataFrame({
        'order_id': range(1, num_orders + 1),
        'user_id': np.random.randint(1, 51, num_orders),
        'product_id': np.random.randint(1, 21, num_orders),
        'quantity': np.random.randint(1, 5, num_orders),
        'order_date': [
            (datetime(2024, 1, 1) + timedelta(days=random.randint(0, 90))).strftime('%Y-%m-%d')
            for _ in range(num_orders)
        ],
        'status': np.random.choice(['pending', 'completed', 'cancelled'], num_orders, p=[0.1, 0.8, 0.1])
    })

    return users, products, orders


# ======================================================================================
# 主函数 - 生成所有样例数据
# ======================================================================================

def generate_all_samples():
    """
    生成所有样例数据并打印预览
    """
    print("="*80)
    print("样例数据生成器 - Sample Data Generator")
    print("="*80)
    print()

    # 1. 数据清洗样例
    print("1. 数据清洗样例 (Dirty Data):")
    print("-"*80)
    df_dirty = generate_dirty_dataframe()
    print(df_dirty)
    print()

    # 2. 销售数据
    print("2. 销售数据样例 (Sales Data):")
    print("-"*80)
    df_sales = generate_sales_data()
    print(df_sales)
    print()

    # 3. 时间序列（前5行）
    print("3. 时间序列数据样例 (前5行):")
    print("-"*80)
    df_ts = generate_timeseries_data(30)
    print(df_ts.head())
    print()

    # 4. 关联表
    print("4. 多表关联数据样例:")
    print("-"*80)
    orders, customers, products = generate_relational_data()
    print("Orders:")
    print(orders.head())
    print("\nCustomers:")
    print(customers)
    print("\nProducts:")
    print(products)
    print()

    # 5. 透视数据
    print("5. 透视表数据样例:")
    print("-"*80)
    df_pivot = generate_pivot_data()
    print(df_pivot)
    print()

    # 6. 用户行为（前10行）
    print("6. 用户行为数据样例 (前10行):")
    print("-"*80)
    df_behavior = generate_user_behavior_data(num_users=50, num_days=30)
    print(df_behavior.head(10))
    print()

    # 7. 金融交易（前10行）
    print("7. 金融交易数据样例 (前10行):")
    print("-"*80)
    df_transaction = generate_transaction_data(100)
    print(df_transaction.head(10))
    print()

    # 8. 带异常值（统计信息）
    print("8. 带异常值的数据样例 (统计信息):")
    print("-"*80)
    df_outliers = generate_data_with_outliers(200)
    print(df_outliers.describe())
    print()

    # 9. JSON数据
    print("9. JSON格式数据样例:")
    print("-"*80)
    json_list = generate_json_data()
    for js in json_list:
        print(js)
    print()

    # 10. 无效数据
    print("10. 带验证错误的数据样例:")
    print("-"*80)
    df_invalid = generate_invalid_data()
    print(df_invalid)
    print()

    print("="*80)
    print("所有样例数据生成完成！")
    print("="*80)

    return {
        'dirty': df_dirty,
        'sales': df_sales,
        'timeseries': df_ts,
        'relational': (orders, customers, products),
        'pivot': df_pivot,
        'behavior': df_behavior,
        'transaction': df_transaction,
        'outliers': df_outliers,
        'json': json_list,
        'invalid': df_invalid
    }


# ======================================================================================
# 使用示例
# ======================================================================================

def example_usage():
    """
    展示如何使用这些生成器
    """
    print("\n" + "="*80)
    print("使用示例 - Example Usage")
    print("="*80)
    print()

    print("# 示例1: 生成数据清洗样例")
    print("-"*80)
    print("df = generate_dirty_dataframe()")
    print("print(df)")
    print()

    print("# 示例2: 生成销售数据")
    print("-"*80)
    print("df_sales = generate_sales_data()")
    print("# 然后可以练习 groupby 操作")
    print("result = df_sales.groupby('product')['quantity'].sum()")
    print()

    print("# 示例3: 生成多表数据并合并")
    print("-"*80)
    print("orders, customers, products = generate_relational_data()")
    print("# 练习 merge 操作")
    print("result = orders.merge(customers, on='customer_id')")
    print()

    print("# 示例4: 生成大量测试数据")
    print("-"*80)
    print("df = generate_user_behavior_data(num_users=1000, num_days=90)")
    print("# 用于性能测试和大数据处理练习")
    print()

    print("# 示例5: 导出数据到CSV")
    print("-"*80)
    print("df = generate_sales_data()")
    print("df.to_csv('sales_sample.csv', index=False)")
    print()


# ======================================================================================
# 快速生成函数 - 直接复制使用
# ======================================================================================

def quick_generate_dirty_df():
    """
    快速生成：包含缺失值和重复值的DataFrame
    可以直接复制这个函数到你的代码中使用
    """
    import pandas as pd
    import numpy as np

    data = {
        'name': ['Alice', 'Bob', 'Alice', None, 'David'],
        'age': [25.0, np.nan, 25.0, 30.0, 35.0],
        'city': ['NYC', 'LA', 'NYC', 'SF', None]
    }
    return pd.DataFrame(data)


def quick_generate_sales_df():
    """
    快速生成：销售数据DataFrame
    """
    import pandas as pd

    data = {
        'product': ['iPhone', 'MacBook', 'iPhone', 'AirPods', 'Desk'],
        'category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Furniture'],
        'price': [1000, 2000, 1000, 200, 500],
        'quantity': [2, 1, 3, 5, 2]
    }
    return pd.DataFrame(data)


# ======================================================================================
# 主程序入口
# ======================================================================================

if __name__ == "__main__":
    # 生成所有样例数据
    all_data = generate_all_samples()

    # 显示使用示例
    example_usage()

    print("\n" + "="*80)
    print("💡 提示:")
    print("="*80)
    print("1. 可以单独调用每个生成函数")
    print("2. 可以修改参数生成不同规模的数据")
    print("3. 可以导出为CSV用于练习")
    print("4. 快速生成函数可以直接复制到你的代码中")
    print()
    print("例如:")
    print("  df = generate_dirty_dataframe()  # 生成脏数据")
    print("  df = generate_sales_data()       # 生成销售数据")
    print("  df = generate_transaction_data(1000)  # 生成1000条交易数据")
    print()
