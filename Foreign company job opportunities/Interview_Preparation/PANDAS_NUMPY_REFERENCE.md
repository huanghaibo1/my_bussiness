# Pandas & Numpy 函数速查手册 📚

> 基于 python_interview_questions.py 中的真实面试题整理
> 专为外企数据岗位面试准备

---

## 目录

1. [Pandas DataFrame 基础操作](#1-pandas-dataframe-基础操作)
2. [数据清洗函数](#2-数据清洗函数)
3. [数据分组和聚合](#3-数据分组和聚合)
4. [数据转换和重塑](#4-数据转换和重塑)
5. [时间序列处理](#5-时间序列处理)
6. [数据合并和关联](#6-数据合并和关联)
7. [文件读写](#7-文件读写)
8. [数据验证](#8-数据验证)
9. [Numpy 常用函数](#9-numpy-常用函数)

---

## 1. Pandas DataFrame 基础操作

### 1.1 pd.DataFrame()

**功能**: 创建 DataFrame

**语法**:
```python
pd.DataFrame(data, index=None, columns=None)
```

**参数**:
- `data`: 字典、列表、numpy数组等
- `index`: 行索引
- `columns`: 列名

**示例**:
```python
import pandas as pd
import numpy as np

# 从字典创建
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'SF']
}
df = pd.DataFrame(data)

# 从列表创建
data = [['Alice', 25], ['Bob', 30]]
df = pd.DataFrame(data, columns=['name', 'age'])

# 从numpy数组创建
arr = np.array([[1, 2], [3, 4]])
df = pd.DataFrame(arr, columns=['A', 'B'])
```

**面试要点**:
- 最常用的数据结构创建方式
- 了解如何从不同数据源创建DataFrame
- 注意列名和索引的设置

---

### 1.2 df.reset_index()

**功能**: 重置DataFrame的索引

**语法**:
```python
df.reset_index(drop=False, inplace=False)
```

**参数**:
- `drop`: 是否删除原索引列 (True/False)
- `inplace`: 是否原地修改 (True/False)

**示例**:
```python
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
}, index=[10, 20, 30])

# drop=False: 保留原索引作为列
df_reset = df.reset_index()
#    index    name  age
# 0     10   Alice   25
# 1     20     Bob   30
# 2     30 Charlie   35

# drop=True: 删除原索引
df_reset = df.reset_index(drop=True)
#       name  age
# 0    Alice   25
# 1      Bob   30
# 2  Charlie   35
```

**常见场景**:
```python
# 数据清洗后重置索引
df = df.drop_duplicates()
df = df.reset_index(drop=True)  # 索引变为0,1,2...

# 分组后重置索引
result = df.groupby('category').agg({'price': 'mean'}).reset_index()
```

**面试要点**:
- 删除重复行、删除特定行后，索引会不连续
- 使用 `drop=True` 避免保留无用的旧索引列
- 分组聚合后通常需要 reset_index()

---

## 2. 数据清洗函数

### 2.1 df.drop_duplicates() ⭐⭐⭐⭐⭐

**功能**: 删除重复的行

**语法**:
```python
df.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
```

**参数**:
- `subset`: 指定用于判断重复的列 (list)
- `keep`: 'first'(保留第一个) | 'last'(保留最后一个) | False(删除所有重复)
- `inplace`: 是否原地修改
- `ignore_index`: 是否重置索引

**示例**:
```python
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Alice', 'David'],
    'age': [25, 30, 25, 35],
    'city': ['NYC', 'LA', 'NYC', 'SF']
})

# 删除完全相同的行
df.drop_duplicates()
#     name  age city
# 0  Alice   25  NYC
# 1    Bob   30   LA
# 3  David   35   SF

# 只根据name列判断重复
df.drop_duplicates(subset=['name'])
#     name  age city
# 0  Alice   25  NYC
# 1    Bob   30   LA
# 3  David   35   SF

# 保留最后一个
df.drop_duplicates(subset=['name'], keep='last')

# 删除所有重复（一个都不保留）
df.drop_duplicates(subset=['name'], keep=False)

# 原地修改 + 重置索引
df.drop_duplicates(inplace=True, ignore_index=True)
```

**面试真题应用**:
```python
# 题目1: 数据清洗
def clean_dataframe(df):
    # 步骤1: 删除重复行
    df = df.drop_duplicates()

    # 步骤2: 处理缺失值
    mean_age = df['age'].mean()
    df['age'] = df['age'].fillna(mean_age)

    # 步骤3: 删除关键列为空的行
    df = df.dropna(subset=['name'])

    return df.reset_index(drop=True)
```

**面试要点**:
- **最高频考点**，几乎每次面试都会涉及
- 注意 `subset` 参数的使用
- 多个NaN值被视为相同
- 删除后索引不连续，需要 reset_index()

---

### 2.2 df.fillna()

**功能**: 填充缺失值

**语法**:
```python
df.fillna(value, method=None, inplace=False)
```

**参数**:
- `value`: 填充值（可以是标量、字典、Series等）
- `method`: 'ffill'(前向填充) | 'bfill'(后向填充)
- `inplace`: 是否原地修改

**示例**:
```python
df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, np.nan],
    'C': [np.nan, 8, 9]
})

# 用0填充所有缺失值
df.fillna(0)
#      A    B    C
# 0  1.0  4.0  0.0
# 1  0.0  5.0  8.0
# 2  3.0  0.0  9.0

# 用均值填充
df['A'].fillna(df['A'].mean())

# 不同列用不同值填充
df.fillna({'A': 0, 'B': df['B'].mean(), 'C': -1})

# 前向填充（用前一个值填充）
df.fillna(method='ffill')

# 后向填充（用后一个值填充）
df.fillna(method='bfill')
```

**常见模式**:
```python
# 数值列用均值填充
df['age'].fillna(df['age'].mean(), inplace=True)

# 数值列用中位数填充
df['salary'].fillna(df['salary'].median(), inplace=True)

# 分类列用众数填充
df['category'].fillna(df['category'].mode()[0], inplace=True)

# 字符串列用固定值填充
df['city'].fillna('Unknown', inplace=True)
```

**面试要点**:
- 必须理解不同填充策略的适用场景
- 均值适用于正态分布数据
- 中位数适用于有异常值的数据
- 众数适用于分类数据

---

### 2.3 df.dropna()

**功能**: 删除包含缺失值的行或列

**语法**:
```python
df.dropna(axis=0, how='any', subset=None, inplace=False)
```

**参数**:
- `axis`: 0(删除行) | 1(删除列)
- `how`: 'any'(任何缺失) | 'all'(全部缺失)
- `subset`: 指定检查缺失值的列
- `inplace`: 是否原地修改

**示例**:
```python
df = pd.DataFrame({
    'name': ['Alice', 'Bob', None, 'David'],
    'age': [25, np.nan, 30, 35],
    'city': ['NYC', 'LA', 'SF', None]
})

# 删除任何包含缺失值的行
df.dropna()
#     name   age city
# 0  Alice  25.0  NYC

# 删除全部为缺失值的行
df.dropna(how='all')

# 只检查特定列的缺失值
df.dropna(subset=['name'])
#     name   age city
# 0  Alice  25.0  NYC
# 1    Bob   NaN   LA
# 3  David  35.0 None

# 删除包含缺失值的列
df.dropna(axis=1)
```

**面试真题应用**:
```python
# 组合使用
def clean_data(df):
    # 删除关键列为空的行（如ID、主键）
    df = df.dropna(subset=['id', 'customer_id'])

    # 其他列用合适的值填充
    df['age'].fillna(df['age'].mean(), inplace=True)
    df['category'].fillna('Unknown', inplace=True)

    return df
```

**面试要点**:
- 理解何时删除、何时填充
- 关键业务字段缺失 → 删除行
- 可推断的字段缺失 → 填充值

---

### 2.4 df['col'].mean() / sum() / median()

**功能**: 计算列的统计值

**常用统计函数**:
```python
df['age'].mean()      # 平均值
df['age'].median()    # 中位数
df['age'].sum()       # 总和
df['age'].min()       # 最小值
df['age'].max()       # 最大值
df['age'].std()       # 标准差
df['age'].var()       # 方差
df['age'].count()     # 非空值数量
```

**示例**:
```python
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'salary': [50000, 60000, 70000]
})

# 计算平均年龄
avg_age = df['age'].mean()  # 30.0

# 计算总薪资
total_salary = df['salary'].sum()  # 180000

# 处理缺失值时
df_with_na = pd.DataFrame({
    'age': [25, np.nan, 35]
})
df_with_na['age'].mean()  # 30.0 (自动忽略NaN)
```

**面试真题应用**:
```python
# 题目1: 用均值填充缺失值
mean_age = df['age'].mean()
df['age'] = df['age'].fillna(mean_age)

# 题目20: 检测异常值（3σ原则）
mean = df['amount'].mean()
std = df['amount'].std()
outliers = df[(df['amount'] < mean - 3*std) | (df['amount'] > mean + 3*std)]
```

**面试要点**:
- 这些函数默认忽略 NaN
- 可以用 `skipna=False` 参数使结果为 NaN

---

## 3. 数据分组和聚合

### 3.1 df.groupby() ⭐⭐⭐⭐⭐

**功能**: 按照一列或多列对数据进行分组

**语法**:
```python
df.groupby(by=None, as_index=True)
```

**参数**:
- `by`: 分组的列名（可以是字符串或列表）
- `as_index`: 是否将分组列作为索引

**基本示例**:
```python
df = pd.DataFrame({
    'product': ['iPhone', 'MacBook', 'iPhone', 'AirPods'],
    'category': ['Electronics', 'Electronics', 'Electronics', 'Electronics'],
    'price': [1000, 2000, 1000, 200],
    'quantity': [2, 1, 3, 5]
})

# 按product分组，计算总数量
df.groupby('product')['quantity'].sum()
# product
# AirPods     5
# MacBook     1
# iPhone      5

# 按多列分组
df.groupby(['category', 'product'])['price'].mean()
```

**常用聚合操作**:
```python
# 单个聚合
df.groupby('product')['price'].mean()
df.groupby('product')['quantity'].sum()
df.groupby('product')['price'].count()

# 多个聚合（使用agg）
df.groupby('product').agg({
    'price': 'mean',
    'quantity': 'sum'
})

# 对同一列使用多个聚合
df.groupby('product')['price'].agg(['mean', 'min', 'max', 'count'])

# 自定义聚合函数
df.groupby('product')['price'].agg(lambda x: x.max() - x.min())
```

**面试真题应用**:
```python
# 题目2: 数据分组聚合
def analyze_sales(df):
    # 计算revenue
    df['revenue'] = df['price'] * df['quantity']

    # 分组聚合
    summary = df.groupby('product').agg({
        'revenue': 'sum',        # 总收入
        'price': 'mean',         # 平均价格
        'product': 'count'       # 销售次数
    }).reset_index()

    # 重命名列
    summary.columns = ['product', 'total_revenue', 'avg_price', 'num_sales']

    return summary
```

**常见分组模式**:
```python
# 1. 按类别统计
category_stats = df.groupby('category').agg({
    'sales': ['sum', 'mean', 'count'],
    'revenue': 'sum'
})

# 2. 按时间分组（年、月、周）
df['date'] = pd.to_datetime(df['date'])
df.groupby(df['date'].dt.year)['sales'].sum()
df.groupby(df['date'].dt.month)['sales'].mean()

# 3. 按多个维度分组
df.groupby(['region', 'category'])['sales'].sum()

# 4. 应用自定义函数到每个组
def custom_agg(group):
    return group['price'].max() - group['price'].min()

df.groupby('category').apply(custom_agg)
```

**面试要点**:
- **超高频考点**，必须熟练掌握
- 理解 split-apply-combine 模式
- 掌握常见聚合函数：sum, mean, count, min, max
- 了解如何同时应用多个聚合函数
- 记得使用 `reset_index()` 将分组列变回普通列

---

### 3.2 df.agg()

**功能**: 对DataFrame或分组对象应用聚合函数

**语法**:
```python
df.agg(func, axis=0)
grouped.agg(func_dict)
```

**示例**:
```python
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# 对所有列应用单个函数
df.agg('sum')
# A     6
# B    15
# C    24

# 对所有列应用多个函数
df.agg(['sum', 'mean', 'std'])
#             A         B         C
# sum   6.000000  15.000000  24.000000
# mean  2.000000   5.000000   8.000000
# std   1.000000   1.000000   1.000000

# 不同列应用不同函数
df.agg({
    'A': 'sum',
    'B': 'mean',
    'C': ['min', 'max']
})
```

**与groupby结合**:
```python
# 最常见用法
df.groupby('category').agg({
    'price': 'mean',
    'quantity': 'sum',
    'revenue': ['sum', 'mean']
})

# 使用命名聚合（pandas 0.25+）
df.groupby('category').agg(
    avg_price=('price', 'mean'),
    total_qty=('quantity', 'sum'),
    max_revenue=('revenue', 'max')
)
```

**面试要点**:
- 与 groupby 配合使用最频繁
- 了解如何对不同列应用不同聚合
- 掌握常用聚合函数名称

---

### 3.3 df.sort_values()

**功能**: 按照一列或多列对DataFrame排序

**语法**:
```python
df.sort_values(by, ascending=True, inplace=False)
```

**参数**:
- `by`: 排序的列名（字符串或列表）
- `ascending`: True(升序) | False(降序)，可以是布尔值列表
- `inplace`: 是否原地修改

**示例**:
```python
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 25, 35],
    'salary': [50000, 60000, 55000, 70000]
})

# 按单列排序（升序）
df.sort_values('age')

# 按单列排序（降序）
df.sort_values('age', ascending=False)

# 按多列排序（先按age升序，再按salary降序）
df.sort_values(['age', 'salary'], ascending=[True, False])
#       name  age  salary
# 2  Charlie   25   55000
# 0    Alice   25   50000
# 1      Bob   30   60000
# 3    David   35   70000
```

**面试真题应用**:
```python
# 题目2: 分组聚合后排序
summary = df.groupby('product').agg({
    'revenue': 'sum'
}).reset_index()

# 按revenue降序排列
summary = summary.sort_values('revenue', ascending=False)

# 题目13: 字典排序转DataFrame
sorted_items = sorted(d.items(), key=lambda x: (-x[1], x[0]))
```

**面试要点**:
- 可以按多列排序，注意 ascending 参数可以是列表
- 排序后索引顺序会改变，可能需要 reset_index()
- 默认 NaN 排在最后

---

### 3.4 df['col'].value_counts()

**功能**: 统计每个值出现的次数

**语法**:
```python
df['col'].value_counts(normalize=False, sort=True, ascending=False)
```

**参数**:
- `normalize`: True返回占比，False返回计数
- `sort`: 是否排序
- `ascending`: 排序方向

**示例**:
```python
df = pd.DataFrame({
    'category': ['A', 'B', 'A', 'C', 'B', 'A', 'A']
})

# 统计每个类别的数量
df['category'].value_counts()
# A    4
# B    2
# C    1

# 返回占比
df['category'].value_counts(normalize=True)
# A    0.571429
# B    0.285714
# C    0.142857

# 升序排列
df['category'].value_counts(ascending=True)
```

**面试应用**:
```python
# 找出最常见的类别
most_common = df['category'].value_counts().index[0]

# 找出Top 3类别
top3 = df['category'].value_counts().head(3)

# 转换为字典
category_counts = df['category'].value_counts().to_dict()
```

**面试要点**:
- 返回 Series，索引是值，数据是计数
- 默认按计数降序排列
- 常用于分类数据的频率分析

---

## 4. 数据转换和重塑

### 4.1 df.pivot() ⭐⭐⭐⭐

**功能**: 将长格式数据转换为宽格式（数据透视）

**语法**:
```python
df.pivot(index, columns, values)
```

**参数**:
- `index`: 用作新DataFrame索引的列
- `columns`: 用作新DataFrame列名的列
- `values`: 用作新DataFrame值的列

**示例**:
```python
df = pd.DataFrame({
    'date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    'product': ['A', 'B', 'A', 'B'],
    'sales': [100, 200, 150, 250]
})

# 透视：date为行，product为列
pivoted = df.pivot(index='date', columns='product', values='sales')

# 结果：
# product       A    B
# date
# 2024-01-01  100  200
# 2024-01-02  150  250
```

**面试真题应用**:
```python
# 题目3: 数据透视
def pivot_sales_data(df):
    """将长格式销售数据转为宽格式"""
    pivoted = df.pivot(index='date', columns='product', values='sales')
    return pivoted
```

**常见用法**:
```python
# 用户-商品购买矩阵
user_product_matrix = df.pivot(
    index='user_id',
    columns='product_id',
    values='purchase_count'
)

# 日期-类别销售表
date_category_sales = df.pivot(
    index='date',
    columns='category',
    values='sales_amount'
)
```

**与 pivot_table 的区别**:
```python
# pivot: 不能有重复的index-column组合，不能聚合
df.pivot(index='date', columns='product', values='sales')

# pivot_table: 可以有重复，可以聚合
df.pivot_table(
    index='date',
    columns='product',
    values='sales',
    aggfunc='sum'  # 或 'mean', 'count' 等
)
```

**面试要点**:
- 理解长格式 vs 宽格式的概念
- pivot 要求 index-column 组合唯一
- 如果有重复，使用 pivot_table
- 常用于创建交叉表、用户-物品矩阵

---

## 5. 时间序列处理

### 5.1 pd.to_datetime() ⭐⭐⭐⭐

**功能**: 将字符串或数字转换为datetime类型

**语法**:
```python
pd.to_datetime(arg, format=None, errors='raise')
```

**参数**:
- `arg`: 要转换的数据
- `format`: 日期格式（如'%Y-%m-%d'）
- `errors`: 'raise'(报错) | 'coerce'(转为NaT) | 'ignore'(保持原样)

**示例**:
```python
# 转换字符串
dates = ['2024-01-01', '2024-01-02', '2024-01-03']
pd.to_datetime(dates)
# DatetimeIndex(['2024-01-01', '2024-01-02', '2024-01-03'])

# 转换DataFrame中的列
df['date'] = pd.to_datetime(df['date'])

# 指定格式
df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')

# 处理错误
df['date'] = pd.to_datetime(df['date'], errors='coerce')  # 无效日期变为NaT

# 从多个列创建日期
df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
```

**日期时间访问**:
```python
df['date'] = pd.to_datetime(df['date'])

# 提取年月日
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['weekday'] = df['date'].dt.dayofweek  # 0=Monday, 6=Sunday
df['quarter'] = df['date'].dt.quarter

# 格式化输出
df['date_str'] = df['date'].dt.strftime('%Y-%m-%d')
```

**面试真题应用**:
```python
# 题目4: 时间序列处理
def analyze_timeseries(df):
    # 转换为datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.set_index('timestamp')

    # 按日聚合
    daily_avg = df.resample('D').mean()

    return daily_avg
```

**常见日期格式**:
```python
# ISO 格式（自动识别）
pd.to_datetime('2024-01-15')

# 美国格式
pd.to_datetime('01/15/2024', format='%m/%d/%Y')

# 中文格式
pd.to_datetime('2024年1月15日', format='%Y年%m月%d日')

# Unix时间戳
pd.to_datetime(1705276800, unit='s')
```

**面试要点**:
- 几乎所有时间序列分析的第一步
- 了解常见日期格式
- 使用 `errors='coerce'` 处理脏数据
- 转换后可以使用 `.dt` 访问器提取日期部分

---

### 5.2 df.set_index()

**功能**: 将某列设置为DataFrame的索引

**语法**:
```python
df.set_index(keys, drop=True, inplace=False)
```

**参数**:
- `keys`: 要设置为索引的列名
- `drop`: 是否删除原列
- `inplace`: 是否原地修改

**示例**:
```python
df = pd.DataFrame({
    'date': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'value': [100, 150, 200]
})

# 将date列设为索引
df_indexed = df.set_index('date')
#              value
# date
# 2024-01-01    100
# 2024-01-02    150
# 2024-01-03    200

# 设置多层索引
df.set_index(['date', 'category'])

# 不删除原列
df.set_index('date', drop=False)
```

**时间序列常见用法**:
```python
# 时间序列分析标准流程
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.set_index('timestamp')

# 现在可以使用时间索引的功能
df['2024-01']  # 选择2024年1月的数据
df['2024-01':'2024-03']  # 选择时间范围
df.resample('D').mean()  # 按日重采样
```

**面试要点**:
- 时间序列分析通常需要将时间列设为索引
- 设置索引后可以使用时间切片
- 使用 `reset_index()` 可以还原为普通列

---

### 5.3 df.resample() ⭐⭐⭐

**功能**: 对时间序列数据进行重采样（降采样或升采样）

**前提**: DataFrame必须有DatetimeIndex

**语法**:
```python
df.resample(rule).agg_func()
```

**参数 rule**:
- `'D'`: 天
- `'W'`: 周
- `'M'`: 月末
- `'MS'`: 月初
- `'Q'`: 季度末
- `'Y'`: 年末
- `'H'`: 小时
- `'T'` 或 `'min'`: 分钟

**示例**:
```python
# 创建时间序列数据
dates = pd.date_range('2024-01-01', periods=30, freq='D')
df = pd.DataFrame({
    'value': np.random.randint(100, 200, 30)
}, index=dates)

# 按周聚合（求和）
weekly = df.resample('W').sum()

# 按月聚合（求平均）
monthly = df.resample('M').mean()

# 按季度聚合
quarterly = df.resample('Q').sum()

# 降采样：从小时到天
hourly_data.resample('D').mean()

# 多个聚合
df.resample('M').agg(['sum', 'mean', 'count'])
```

**面试真题应用**:
```python
# 题目4: 时间序列分析
def analyze_timeseries(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.set_index('timestamp')

    # 每日平均值
    daily_avg = df.resample('D').mean()

    # 每月总和
    monthly_sum = df.resample('M').sum()

    # 每月环比增长
    monthly_sum['mom_growth'] = monthly_sum['value'].pct_change() * 100

    return daily_avg, monthly_sum
```

**常见应用**:
```python
# 从分钟级到小时级
df.resample('H').mean()

# 从日级到周级
df.resample('W-MON').sum()  # 周一为起始日

# 从日级到月级（保留多列）
df.resample('M').agg({
    'sales': 'sum',
    'quantity': 'sum',
    'price': 'mean'
})
```

**面试要点**:
- 必须先有 DatetimeIndex（使用 set_index）
- 理解降采样（聚合）vs 升采样（插值）
- 掌握常用的时间频率代码
- 不同指标用不同聚合：销售额用sum，价格用mean

---

### 5.4 df.rolling() ⭐⭐⭐

**功能**: 创建滚动窗口，用于计算移动平均等

**语法**:
```python
df.rolling(window, min_periods=None).agg_func()
```

**参数**:
- `window`: 窗口大小（整数或时间偏移）
- `min_periods`: 最小观测数

**示例**:
```python
df = pd.DataFrame({
    'value': [10, 20, 30, 40, 50]
})

# 3天移动平均
df['ma_3'] = df['value'].rolling(window=3).mean()
#    value  ma_3
# 0     10   NaN
# 1     20   NaN
# 2     30  20.0  # (10+20+30)/3
# 3     40  30.0  # (20+30+40)/3
# 4     50  40.0  # (30+40+50)/3

# 移动求和
df['sum_3'] = df['value'].rolling(window=3).sum()

# 移动标准差
df['std_3'] = df['value'].rolling(window=3).std()

# 最小观测数
df['ma_3'] = df['value'].rolling(window=3, min_periods=1).mean()
#    value  ma_3
# 0     10  10.0  # 只有1个值
# 1     20  15.0  # (10+20)/2
# 2     30  20.0  # (10+20+30)/3
```

**时间窗口**:
```python
# 按时间窗口（而非行数）
df = df.set_index(pd.to_datetime(df['date']))
df['ma_7d'] = df['value'].rolling('7D').mean()  # 7天移动平均
```

**面试真题应用**:
```python
# 题目4: 7日移动平均
def analyze_timeseries(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.set_index('timestamp')

    daily_avg = df.resample('D').mean()

    # 7日移动平均
    daily_avg['rolling_7d'] = daily_avg['value'].rolling(window=7).mean()

    return daily_avg
```

**常见应用**:
```python
# 股票分析
df['SMA_20'] = df['close'].rolling(20).mean()  # 20日均线
df['SMA_50'] = df['close'].rolling(50).mean()  # 50日均线

# 异常检测
df['rolling_mean'] = df['value'].rolling(7).mean()
df['rolling_std'] = df['value'].rolling(7).std()
df['upper_bound'] = df['rolling_mean'] + 2 * df['rolling_std']
df['lower_bound'] = df['rolling_mean'] - 2 * df['rolling_std']

# 销售趋势
df['sales_ma_30'] = df['daily_sales'].rolling(30).mean()
```

**面试要点**:
- 用于平滑数据、识别趋势
- 前面的行会是NaN（因为窗口不够）
- 可以使用 `min_periods` 控制最小观测数
- 常与时间序列结合使用

---

### 5.5 df.pct_change()

**功能**: 计算百分比变化（环比增长率）

**语法**:
```python
df.pct_change(periods=1)
```

**参数**:
- `periods`: 计算变化的周期数

**示例**:
```python
df = pd.DataFrame({
    'value': [100, 110, 120, 115, 130]
})

# 计算环比增长率
df['growth'] = df['value'].pct_change()
#    value    growth
# 0    100       NaN
# 1    110  0.100000  # (110-100)/100 = 10%
# 2    120  0.090909  # (120-110)/110 = 9.09%
# 3    115 -0.041667  # (115-120)/120 = -4.17%
# 4    130  0.130435  # (130-115)/115 = 13.04%

# 转换为百分比
df['growth_pct'] = df['value'].pct_change() * 100

# 与2期前比较
df['growth_2'] = df['value'].pct_change(periods=2)
```

**面试真题应用**:
```python
# 题目4: 月度环比增长
def analyze_timeseries(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.set_index('timestamp')

    # 按月聚合
    monthly = df.resample('M').sum()

    # 月度环比增长
    monthly['mom_growth'] = monthly['value'].pct_change() * 100

    return monthly
```

**常见应用**:
```python
# 销售环比增长
monthly_sales['mom_growth'] = monthly_sales['sales'].pct_change() * 100

# 同比增长（与去年同期比较）
daily_sales['yoy_growth'] = daily_sales['sales'].pct_change(periods=365) * 100

# 用户增长率
df['user_growth'] = df['active_users'].pct_change() * 100
```

**面试要点**:
- 第一行总是NaN
- 返回小数，乘以100得到百分比
- 可以设置 periods 计算不同周期的变化
- 常用于分析增长趋势

---

## 6. 数据合并和关联

### 6.1 df.merge() ⭐⭐⭐⭐⭐

**功能**: 类似SQL的JOIN操作，合并两个DataFrame

**语法**:
```python
df1.merge(df2, on=None, how='inner', left_on=None, right_on=None)
```

**参数**:
- `on`: 连接的列名（两个表列名相同时）
- `how`: 'inner'(内连接) | 'left'(左连接) | 'right'(右连接) | 'outer'(全外连接)
- `left_on`: 左表的连接列
- `right_on`: 右表的连接列

**四种连接类型**:
```python
left = pd.DataFrame({
    'key': ['A', 'B', 'C'],
    'value1': [1, 2, 3]
})

right = pd.DataFrame({
    'key': ['B', 'C', 'D'],
    'value2': [4, 5, 6]
})

# 内连接（只保留匹配的）
left.merge(right, on='key', how='inner')
#   key  value1  value2
# 0   B       2       4
# 1   C       3       5

# 左连接（保留左表所有行）
left.merge(right, on='key', how='left')
#   key  value1  value2
# 0   A       1     NaN
# 1   B       2     4.0
# 2   C       3     5.0

# 右连接（保留右表所有行）
left.merge(right, on='key', how='right')
#   key  value1  value2
# 0   B     2.0       4
# 1   C     3.0       5
# 2   D     NaN       6

# 全外连接（保留所有行）
left.merge(right, on='key', how='outer')
#   key  value1  value2
# 0   A     1.0     NaN
# 1   B     2.0     4.0
# 2   C     3.0     5.0
# 3   D     NaN     6.0
```

**列名不同时**:
```python
# 使用 left_on 和 right_on
orders.merge(
    customers,
    left_on='customer_id',
    right_on='id',
    how='left'
)
```

**多列连接**:
```python
df1.merge(df2, on=['key1', 'key2'], how='inner')
```

**面试真题应用**:
```python
# 题目5: 多表关联
def merge_order_data(orders, customers, products):
    """合并订单、客户、产品三个表"""

    # 第一步：订单 + 客户
    result = orders.merge(customers, on='customer_id', how='left')

    # 第二步：结果 + 产品
    result = result.merge(products, on='product_id', how='left')

    # 选择需要的列
    result = result[['order_id', 'customer_name', 'product_name',
                     'quantity', 'price', 'order_date']]

    return result
```

**常见连接场景**:
```python
# 1. 订单表 + 客户表
orders.merge(customers, on='customer_id', how='left')

# 2. 销售表 + 产品表 + 类别表
sales.merge(products, on='product_id') \
     .merge(categories, on='category_id')

# 3. 事实表 + 多个维度表
fact.merge(dim_date, on='date_id') \
    .merge(dim_product, on='product_id') \
    .merge(dim_customer, on='customer_id')
```

**处理重复列名**:
```python
# 如果两个表有同名列，会自动添加后缀
result = df1.merge(df2, on='id', suffixes=('_left', '_right'))
```

**面试要点**:
- **超高频考点**，必须掌握
- 理解四种连接类型的区别
- left join 最常用（保留主表所有数据）
- 可以连接多个表（链式调用）
- 了解如何处理列名冲突

---

## 7. 文件读写

### 7.1 pd.read_csv()

**功能**: 从CSV文件读取数据到DataFrame

**语法**:
```python
pd.read_csv(filepath, sep=',', header='infer', names=None, usecols=None)
```

**常用参数**:
- `filepath`: 文件路径
- `sep`: 分隔符（默认逗号）
- `header`: 表头行号（None表示无表头）
- `names`: 自定义列名
- `usecols`: 只读取指定列
- `dtype`: 指定列的数据类型
- `parse_dates`: 将指定列解析为日期

**基本示例**:
```python
# 读取CSV文件
df = pd.read_csv('data.csv')

# 指定分隔符
df = pd.read_csv('data.txt', sep='\t')

# 无表头
df = pd.read_csv('data.csv', header=None, names=['A', 'B', 'C'])

# 只读取部分列
df = pd.read_csv('data.csv', usecols=['name', 'age', 'city'])

# 指定数据类型
df = pd.read_csv('data.csv', dtype={'id': str, 'age': int})

# 解析日期列
df = pd.read_csv('data.csv', parse_dates=['date'])
```

**处理缺失值**:
```python
# 指定缺失值标记
df = pd.read_csv('data.csv', na_values=['NA', 'missing', '-'])

# 不同列使用不同的缺失值标记
df = pd.read_csv('data.csv', na_values={'col1': ['NA'], 'col2': ['-']})
```

**大文件处理**:
```python
# 分块读取
for chunk in pd.read_csv('large_file.csv', chunksize=10000):
    process(chunk)

# 只读取前N行
df = pd.read_csv('data.csv', nrows=1000)
```

**面试要点**:
- 了解常用参数
- 知道如何处理不同格式的文件
- 大文件使用 chunksize

---

### 7.2 df.to_csv()

**功能**: 将DataFrame保存为CSV文件

**语法**:
```python
df.to_csv(filepath, sep=',', index=True, header=True)
```

**参数**:
- `filepath`: 文件路径
- `sep`: 分隔符
- `index`: 是否保存索引
- `header`: 是否保存列名
- `encoding`: 编码格式

**示例**:
```python
# 保存到CSV（不保存索引）
df.to_csv('output.csv', index=False)

# 指定分隔符
df.to_csv('output.txt', sep='\t', index=False)

# 指定编码
df.to_csv('output.csv', index=False, encoding='utf-8')

# 只保存部分列
df[['name', 'age']].to_csv('output.csv', index=False)

# 追加到文件
df.to_csv('output.csv', mode='a', header=False, index=False)
```

**面试真题应用**:
```python
# 题目21: ETL流程
def process_csv_file(input_file, output_file):
    # 读取
    df = pd.read_csv(input_file)

    # 清洗
    df = df.drop_duplicates()
    df = df.dropna(subset=['id'])

    # 导出
    df.to_csv(output_file, index=False)
```

---

### 7.3 pd.to_numeric()

**功能**: 将列转换为数值类型

**语法**:
```python
pd.to_numeric(arg, errors='raise', downcast=None)
```

**参数**:
- `errors`: 'raise'(报错) | 'coerce'(无效值变为NaN) | 'ignore'(保持原样)

**示例**:
```python
df = pd.DataFrame({
    'A': ['1', '2', '3', 'abc'],
    'B': ['100', '200', 'xyz', '400']
})

# 转换，无效值变为NaN
df['A'] = pd.to_numeric(df['A'], errors='coerce')
#      A
# 0  1.0
# 1  2.0
# 2  3.0
# 3  NaN

# 批量转换多列
for col in ['A', 'B']:
    df[col] = pd.to_numeric(df[col], errors='coerce')
```

**面试应用**:
```python
# ETL中的类型转换
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').fillna(0).astype(int)
```

---

## 8. 数据验证

### 8.1 df.isnull() / df.isna()

**功能**: 检查缺失值，返回布尔DataFrame

**示例**:
```python
df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, np.nan]
})

# 检查每个值是否为空
df.isnull()
#        A      B
# 0  False  False
# 1   True  False
# 2  False   True

# 统计每列的缺失值数量
df.isnull().sum()
# A    1
# B    1

# 统计总缺失值
df.isnull().sum().sum()  # 2

# 检查某列是否有缺失
df['A'].isnull().any()  # True

# 筛选有缺失值的行
df[df['A'].isnull()]
```

**面试应用**:
```python
# 数据质量检查
def check_data_quality(df):
    print("Missing values per column:")
    print(df.isnull().sum())

    print(f"\nTotal missing: {df.isnull().sum().sum()}")
    print(f"Missing percentage: {df.isnull().sum().sum() / df.size * 100:.2f}%")
```

**面试要点**:
- `isnull()` 和 `isna()` 完全相同
- 常与 `sum()` 结合统计缺失值
- 可以用 `notnull()` 或 `notna()` 检查非空

---

### 8.2 pd.notna() / pd.notnull()

**功能**: 检查非缺失值

**示例**:
```python
df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, np.nan]
})

# 检查非空
df.notna()
#        A      B
# 0   True   True
# 1  False   True
# 2   True  False

# 统计非空值数量
df.notna().sum()
# A    2
# B    2

# 筛选非空行
df[df['A'].notna()]
```

**面试应用**:
```python
# 题目20: 数据验证
def validate_data(df):
    errors = {}

    # 检查必填列的空值
    for col in ['id', 'name']:
        null_indices = df[df[col].isnull()].index.tolist()
        if null_indices:
            errors[col] = null_indices

    return errors
```

---

## 9. Numpy 常用函数

### 9.1 np.nan

**功能**: 表示缺失值（Not a Number）

**示例**:
```python
import numpy as np
import pandas as pd

# 创建包含缺失值的数据
data = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8]
}
df = pd.DataFrame(data)

# 检查是否为NaN
pd.isna(np.nan)  # True
np.isnan(np.nan)  # True

# 比较
np.nan == np.nan  # False（NaN不等于任何值，包括自己）
```

**面试要点**:
- Pandas中用 `np.nan` 表示缺失值
- NaN != NaN（必须用 `pd.isna()` 或 `np.isnan()` 判断）
- 算术运算中，NaN会传播（任何数与NaN运算结果都是NaN）

---

### 9.2 np.random 系列

**功能**: 生成随机数

**常用函数**:
```python
import numpy as np

# 随机整数
np.random.randint(low, high, size)
np.random.randint(1, 10, 5)  # [3, 7, 2, 9, 1]

# 均匀分布
np.random.uniform(low, high, size)
np.random.uniform(0, 1, 5)  # [0.23, 0.67, 0.91, ...]

# 正态分布
np.random.normal(loc, scale, size)
np.random.normal(100, 15, 1000)  # 均值100，标准差15

# 对数正态分布
np.random.lognormal(mean, sigma, size)
np.random.lognormal(5, 1.5, 1000)

# 随机选择
np.random.choice(array, size, replace=True, p=None)
np.random.choice(['A', 'B', 'C'], size=10)
np.random.choice([1,2,3], size=5, p=[0.5, 0.3, 0.2])  # 带概率

# 打乱数组
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)  # 原地打乱
```

**设置随机种子**:
```python
# 保证可重现
np.random.seed(42)
np.random.randint(1, 10, 5)  # 每次运行结果相同
```

**面试应用**:
```python
# 生成测试数据
dates = pd.date_range('2024-01-01', periods=30, freq='D')
df = pd.DataFrame({
    'date': dates,
    'value': np.random.randint(100, 200, 30),
    'category': np.random.choice(['A', 'B', 'C'], 30)
})

# 生成金融数据
amounts = np.random.lognormal(mean=5, sigma=1.5, size=1000)
```

---

### 9.3 其他常用Numpy函数

**数组连接**:
```python
# 连接数组
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
np.concatenate([arr1, arr2])  # [1, 2, 3, 4, 5, 6]

# 垂直堆叠
np.vstack([arr1, arr2])
# [[1, 2, 3],
#  [4, 5, 6]]
```

**数组统计**:
```python
arr = np.array([1, 2, 3, 4, 5])

np.mean(arr)    # 3.0
np.median(arr)  # 3.0
np.std(arr)     # 1.414...
np.sum(arr)     # 15
np.min(arr)     # 1
np.max(arr)     # 5
```

---

## 10. 面试高频组合技巧

### 10.1 完整的数据清洗流程

```python
def clean_dataframe(df):
    """标准数据清洗流程"""
    print(f"原始数据: {len(df)} 行")

    # 1. 删除完全重复的行
    df = df.drop_duplicates()
    print(f"去重后: {len(df)} 行")

    # 2. 处理缺失值
    # 2.1 删除关键列为空的行
    df = df.dropna(subset=['id', 'date'])

    # 2.2 数值列用均值/中位数填充
    for col in df.select_dtypes(include=[np.number]).columns:
        if df[col].isnull().sum() > 0:
            df[col].fillna(df[col].median(), inplace=True)

    # 2.3 分类列用众数填充
    for col in df.select_dtypes(include=['object']).columns:
        if df[col].isnull().sum() > 0:
            df[col].fillna(df[col].mode()[0], inplace=True)

    # 3. 类型转换
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

    # 4. 删除异常值（3σ原则）
    for col in ['amount', 'quantity']:
        if col in df.columns:
            mean = df[col].mean()
            std = df[col].std()
            df = df[(df[col] >= mean - 3*std) & (df[col] <= mean + 3*std)]

    # 5. 重置索引
    df = df.reset_index(drop=True)

    print(f"清洗后: {len(df)} 行")
    return df
```

---

### 10.2 分组聚合常见模式

```python
# 模式1: 单维度多指标
summary = df.groupby('category').agg({
    'sales': ['sum', 'mean', 'count'],
    'revenue': 'sum',
    'quantity': 'mean'
}).reset_index()

# 模式2: 多维度分组
summary = df.groupby(['region', 'category']).agg({
    'sales': 'sum'
}).reset_index()

# 模式3: 自定义聚合
def custom_agg(x):
    return x.max() - x.min()

summary = df.groupby('product')['price'].agg([
    ('avg', 'mean'),
    ('total', 'sum'),
    ('range', custom_agg)
]).reset_index()
```

---

### 10.3 时间序列分析流程

```python
def analyze_timeseries(df):
    """完整的时间序列分析"""
    # 1. 转换日期类型
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date')

    # 2. 按日聚合
    daily = df.resample('D').sum()

    # 3. 移动平均
    daily['ma_7'] = daily['value'].rolling(7).mean()
    daily['ma_30'] = daily['value'].rolling(30).mean()

    # 4. 月度汇总
    monthly = df.resample('M').sum()
    monthly['mom_growth'] = monthly['value'].pct_change() * 100

    # 5. 同比增长（与去年比）
    monthly['yoy_growth'] = monthly['value'].pct_change(periods=12) * 100

    return daily, monthly
```

---

### 10.4 多表关联标准模式

```python
def merge_multiple_tables(fact, dim1, dim2, dim3):
    """多表关联标准流程"""
    result = (fact
              .merge(dim1, on='dim1_id', how='left')
              .merge(dim2, on='dim2_id', how='left')
              .merge(dim3, on='dim3_id', how='left'))

    # 选择需要的列
    result = result[[
        'id', 'dim1_name', 'dim2_name', 'dim3_name',
        'value', 'date'
    ]]

    return result
```

---

## 11. 面试速记卡片 ⭐

### 必记函数（按频率排序）

| 函数 | 用途 | 频率 |
|------|------|------|
| `drop_duplicates()` | 删除重复行 | ⭐⭐⭐⭐⭐ |
| `groupby().agg()` | 分组聚合 | ⭐⭐⭐⭐⭐ |
| `merge()` | 表连接 | ⭐⭐⭐⭐⭐ |
| `fillna()` | 填充缺失值 | ⭐⭐⭐⭐⭐ |
| `dropna()` | 删除缺失值 | ⭐⭐⭐⭐ |
| `pivot()` | 数据透视 | ⭐⭐⭐⭐ |
| `resample()` | 时间重采样 | ⭐⭐⭐ |
| `rolling()` | 滚动窗口 | ⭐⭐⭐ |
| `to_datetime()` | 日期转换 | ⭐⭐⭐⭐ |
| `sort_values()` | 排序 | ⭐⭐⭐⭐ |

---

### 快速记忆口诀

**数据清洗三部曲**:
1. `drop_duplicates()` - 去重
2. `fillna()` / `dropna()` - 处理缺失
3. `reset_index()` - 重置索引

**分组聚合三步骤**:
1. `groupby()` - 分组
2. `.agg()` - 聚合
3. `.reset_index()` - 还原索引

**时间序列四件套**:
1. `to_datetime()` - 转换类型
2. `set_index()` - 设置索引
3. `resample()` - 重采样
4. `rolling()` - 移动平均

**多表关联标准流程**:
1. `merge(table1, on='key', how='left')`
2. `merge(table2, on='key', how='left')`
3. 选择需要的列

---

## 12. 常见错误和注意事项 ⚠️

### 错误1: 忘记 reset_index()

```python
# ❌ 错误
result = df.groupby('category')['sales'].sum()
# 结果是 Series，category是索引

# ✅ 正确
result = df.groupby('category')['sales'].sum().reset_index()
# 结果是 DataFrame，category是普通列
```

### 错误2: inplace=True 没有返回值

```python
# ❌ 错误
df = df.drop_duplicates(inplace=True)  # df变成None

# ✅ 正确（两种方式选一种）
df = df.drop_duplicates()  # inplace=False，返回新DF
# 或
df.drop_duplicates(inplace=True)  # 不要赋值
```

### 错误3: 时间序列没有设置索引

```python
# ❌ 错误
df.resample('D').mean()  # 报错：没有DatetimeIndex

# ✅ 正确
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
df.resample('D').mean()  # OK
```

### 错误4: merge后列名冲突

```python
# ❌ 问题：两个表都有'name'列
result = df1.merge(df2, on='id')
# 结果：name_x, name_y 很混乱

# ✅ 解决：指定后缀
result = df1.merge(df2, on='id', suffixes=('_customer', '_product'))
# 结果：name_customer, name_product
```

---

## 13. 面试前最后检查清单 ✅

- [ ] 能快速写出数据清洗流程（去重、填充、删除）
- [ ] 熟练使用 groupby + agg 进行分组聚合
- [ ] 理解四种 merge 连接类型的区别
- [ ] 知道如何处理时间序列（to_datetime + set_index + resample）
- [ ] 会用 pivot 进行数据透视
- [ ] 了解 rolling 计算移动平均
- [ ] 记住常用聚合函数：sum, mean, count, min, max
- [ ] 知道如何检查和处理缺失值
- [ ] 能读写CSV文件并进行类型转换
- [ ] 理解 reset_index() 的作用和使用时机

---

**祝你面试成功！ Good luck! 💪🚀**
