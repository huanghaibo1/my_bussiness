import pandas as pd
import numpy as np

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

def clean_dataframe(df):
    """
    Solution 1: 数据清洗
    """
    # 1. Remove duplicates
    df = df.drop_duplicates()
    print("去重后数据:")
    print(df)
    print()

    # 2. Fill missing age with mean
    mean_age = df['age'].mean()
    print(f"年龄的平均值: {mean_age}")
    df['age'] = df['age'].fillna(mean_age)
    print("填充缺失年龄后的数据:")
    print(df)
    print()

    # 3. Drop rows where name is missing
    df = df.dropna(subset=['name'])
    print("删除缺失姓名后的数据:")
    print(df)
    print()

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
    print("原始数据:")
    print(df)
    print()

    result = clean_dataframe(df)
    print("题目1 - 数据清洗:")
    print(result)
    print()

if __name__ == "__main__":
    test_clean_dataframe()