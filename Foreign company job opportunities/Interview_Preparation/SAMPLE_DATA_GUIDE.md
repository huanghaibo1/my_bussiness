# 样例数据生成器使用指南 📊

> 快速生成Python面试题所需的各种测试数据

---

## 🚀 快速开始

### 安装依赖
```bash
pip install pandas numpy
```

### 基本使用
```python
from sample_data_generator import generate_dirty_dataframe

# 生成样例数据
df = generate_dirty_dataframe()
print(df)
```

---

## 📋 可用的数据生成器

### 1. 数据清洗样例 ⭐ 最常用

**函数**: `generate_dirty_dataframe()`

**生成的数据**:
```
   name   age  city
0  Alice  25.0  NYC
1  Bob    NaN   LA
2  Alice  25.0  NYC
3  NaN    30.0  SF
4  David  35.0  NaN
```

**用途**: 练习数据清洗、处理缺失值、去重

**代码示例**:
```python
import pandas as pd
import numpy as np

# 方法1: 使用生成器
from sample_data_generator import generate_dirty_dataframe
df = generate_dirty_dataframe()

# 方法2: 直接创建（可以复制到任何地方）
data = {
    'name': ['Alice', 'Bob', 'Alice', None, 'David'],
    'age': [25.0, np.nan, 25.0, 30.0, 35.0],
    'city': ['NYC', 'LA', 'NYC', 'SF', None]
}
df = pd.DataFrame(data)
```

---

### 2. 销售数据样例

**函数**: `generate_sales_data()`

**生成的数据**:
```
   product     category      price  quantity
0  iPhone      Electronics   1000   2
1  MacBook     Electronics   2000   1
2  iPhone      Electronics   1000   3
3  AirPods     Electronics   200    5
4  Desk        Furniture     500    2
```

**用途**: 练习 groupby、聚合、计算

**代码示例**:
```python
from sample_data_generator import generate_sales_data

df = generate_sales_data()

# 练习聚合
df['revenue'] = df['price'] * df['quantity']
summary = df.groupby('product').agg({
    'revenue': 'sum',
    'quantity': 'sum'
})
```

---

### 3. 时间序列数据

**函数**: `generate_timeseries_data(days=30)`

**参数**:
- `days`: 生成多少天的数据（默认30天）

**生成的数据**:
```
            timestamp  value
0 2024-01-01 00:00:00    156
1 2024-01-01 12:00:00    142
2 2024-01-02 00:00:00    189
...
```

**用途**: 练习时间序列分析、resample、rolling

**代码示例**:
```python
from sample_data_generator import generate_timeseries_data

df = generate_timeseries_data(days=90)

# 设置时间索引
df.set_index('timestamp', inplace=True)

# 日平均
daily_avg = df.resample('D').mean()

# 7日移动平均
df['rolling_7d'] = df['value'].rolling(window=7).mean()
```

---

### 4. 多表关联数据 ⭐ 重要

**函数**: `generate_relational_data()`

**返回**: 3个DataFrame (orders, customers, products)

**数据结构**:

**Orders表**:
```
   order_id  customer_id  product_id  quantity order_date
0  1         101          1           2        2024-01-01
1  2         102          2           1        2024-01-02
...
```

**Customers表**:
```
   customer_id  customer_name  email
0  101          Alice          alice@email.com
1  102          Bob            bob@email.com
...
```

**Products表**:
```
   product_id  product_name  price  category
0  1           iPhone        1000   Electronics
1  2           MacBook       2000   Electronics
...
```

**用途**: 练习 merge、join、多表关联

**代码示例**:
```python
from sample_data_generator import generate_relational_data

orders, customers, products = generate_relational_data()

# 练习关联
result = orders.merge(customers, on='customer_id', how='left')
result = result.merge(products, on='product_id', how='left')

print(result[['order_id', 'customer_name', 'product_name', 'quantity']])
```

---

### 5. 透视表数据

**函数**: `generate_pivot_data()`

**生成的数据**:
```
   date        product  sales
0  2024-01-01  A        100
1  2024-01-01  B        200
2  2024-01-02  A        150
3  2024-01-02  B        250
...
```

**用途**: 练习 pivot、数据重塑

**代码示例**:
```python
from sample_data_generator import generate_pivot_data

df = generate_pivot_data()

# 长格式转宽格式
pivoted = df.pivot(index='date', columns='product', values='sales')
print(pivoted)

# 输出:
# product     A    B
# date
# 2024-01-01  100  200
# 2024-01-02  150  250
```

---

### 6. 用户行为数据

**函数**: `generate_user_behavior_data(num_users=100, num_days=30)`

**参数**:
- `num_users`: 用户数量
- `num_days`: 天数

**生成的数据**:
```
   user_id  login_date  sessions  duration_minutes
0  1        2024-01-05  3         45
1  1        2024-01-12  2         67
2  2        2024-01-03  1         23
...
```

**用途**: 练习留存率计算、活跃度分析

**代码示例**:
```python
from sample_data_generator import generate_user_behavior_data

df = generate_user_behavior_data(num_users=500, num_days=90)

# 计算日活跃用户数
daily_active = df.groupby('login_date')['user_id'].nunique()

# 计算用户总会话数
user_sessions = df.groupby('user_id')['sessions'].sum()
```

---

### 7. 金融交易数据

**函数**: `generate_transaction_data(num_transactions=1000)`

**参数**:
- `num_transactions`: 交易数量

**生成的数据**:
```
   transaction_id  account_id  transaction_date  amount  transaction_type  category
0  1               1234        2024-01-15        125.50  debit            Food
1  2               1567        2024-02-03        89.99   credit           Shopping
...
```

**用途**: 练习异常检测、金融数据分析

---

### 8. 带异常值的数据

**函数**: `generate_data_with_outliers(num_rows=200)`

**生成的数据**: 大部分值在 85-115 范围，少量异常值（0, 300, -50, 500）

**用途**: 练习异常检测、数据清洗

**代码示例**:
```python
from sample_data_generator import generate_data_with_outliers

df = generate_data_with_outliers(500)

# 检测异常值（3σ原则）
mean = df['value'].mean()
std = df['value'].std()
outliers = df[(df['value'] < mean - 3*std) | (df['value'] > mean + 3*std)]

print(f"异常值数量: {len(outliers)}")
```

---

### 9. JSON格式数据

**函数**: `generate_json_data()`

**生成的数据**:
```python
[
  '{"id": 1, "name": "Alice", "age": 25, "address": {"city": "NYC", "zip": "10001"}}',
  '{"id": 2, "name": "Bob", "age": 30, "address": {"city": "LA", "zip": "90001"}}',
  ...
]
```

**用途**: 练习 JSON 解析、嵌套数据扁平化

**代码示例**:
```python
import json
from sample_data_generator import generate_json_data

json_strings = generate_json_data()

# 解析JSON
data = []
for js in json_strings:
    obj = json.loads(js)
    flat = {
        'id': obj['id'],
        'name': obj['name'],
        'age': obj['age'],
        'city': obj['address']['city'],
        'zip': obj['address']['zip']
    }
    data.append(flat)

df = pd.DataFrame(data)
```

---

### 10. 无效数据样例

**函数**: `generate_invalid_data()`

**生成的数据**:
```
   id  name     email           age    salary    join_date
0  1   Alice    alice@test.com  25     50000     2024-01-01
1  2   None     invalid_email   150    60000     invalid_date
2  3   Charlie  None            -5     None      2024-03-01
...
```

**用途**: 练习数据验证、错误检测

---

### 11. 电商完整数据场景

**函数**: `generate_ecommerce_data()`

**返回**: 3个DataFrame (users, products, orders)

**用途**: 综合练习、真实场景模拟

---

## 💡 快速复制代码块

### 最常用的数据清洗样例

```python
import pandas as pd
import numpy as np

# 直接复制这段代码即可使用
data = {
    'name': ['Alice', 'Bob', 'Alice', None, 'David'],
    'age': [25.0, np.nan, 25.0, 30.0, 35.0],
    'city': ['NYC', 'LA', 'NYC', 'SF', None]
}
df = pd.DataFrame(data)

print(df)
```

### 销售数据样例

```python
import pandas as pd

data = {
    'product': ['iPhone', 'MacBook', 'iPhone', 'AirPods', 'Desk'],
    'category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Furniture'],
    'price': [1000, 2000, 1000, 200, 500],
    'quantity': [2, 1, 3, 5, 2]
}
df = pd.DataFrame(data)

print(df)
```

### 多表关联样例

```python
import pandas as pd

# 订单表
orders = pd.DataFrame({
    'order_id': [1, 2, 3],
    'customer_id': [101, 102, 101],
    'product_id': [1, 2, 1],
    'quantity': [2, 1, 3]
})

# 客户表
customers = pd.DataFrame({
    'customer_id': [101, 102, 103],
    'customer_name': ['Alice', 'Bob', 'Charlie']
})

# 产品表
products = pd.DataFrame({
    'product_id': [1, 2, 3],
    'product_name': ['iPhone', 'MacBook', 'iPad'],
    'price': [1000, 2000, 800]
})

# 练习merge
result = orders.merge(customers, on='customer_id').merge(products, on='product_id')
print(result)
```

---

## 🎯 使用场景

### 场景1: 面试准备
```python
# 准备面试时，快速生成数据练习
from sample_data_generator import generate_dirty_dataframe

df = generate_dirty_dataframe()

# 练习数据清洗
df_clean = df.drop_duplicates()
df_clean['age'].fillna(df_clean['age'].mean(), inplace=True)
df_clean = df_clean.dropna(subset=['name'])
```

### 场景2: 学习新技能
```python
# 学习pandas新函数时，快速生成测试数据
from sample_data_generator import generate_sales_data

df = generate_sales_data()

# 练习各种操作
print(df.groupby('category')['price'].mean())
print(df.sort_values('quantity', ascending=False))
```

### 场景3: 代码测试
```python
# 测试你写的数据处理函数
from sample_data_generator import generate_transaction_data

def analyze_transactions(df):
    # 你的分析代码
    return df.groupby('category')['amount'].sum()

# 用生成的数据测试
df = generate_transaction_data(1000)
result = analyze_transactions(df)
print(result)
```

### 场景4: 性能测试
```python
# 测试大数据处理性能
from sample_data_generator import generate_user_behavior_data
import time

df = generate_user_behavior_data(num_users=10000, num_days=365)

start = time.time()
# 你的处理代码
result = df.groupby('user_id').agg({
    'sessions': 'sum',
    'duration_minutes': 'mean'
})
end = time.time()

print(f"处理时间: {end - start:.2f}秒")
```

---

## 📦 导出数据

### 导出为CSV
```python
from sample_data_generator import generate_sales_data

df = generate_sales_data()
df.to_csv('sales_sample.csv', index=False)
```

### 导出为Excel
```python
from sample_data_generator import generate_ecommerce_data

users, products, orders = generate_ecommerce_data()

# 需要安装 openpyxl: pip install openpyxl
with pd.ExcelWriter('ecommerce_data.xlsx') as writer:
    users.to_excel(writer, sheet_name='Users', index=False)
    products.to_excel(writer, sheet_name='Products', index=False)
    orders.to_excel(writer, sheet_name='Orders', index=False)
```

### 导出为JSON
```python
from sample_data_generator import generate_sales_data

df = generate_sales_data()
df.to_json('sales_sample.json', orient='records', indent=2)
```

---

## 🔧 自定义数据

### 修改数据规模
```python
from sample_data_generator import generate_user_behavior_data

# 生成更大的数据集
df_small = generate_user_behavior_data(num_users=100, num_days=30)
df_large = generate_user_behavior_data(num_users=10000, num_days=365)

print(f"小数据集: {len(df_small)} 行")
print(f"大数据集: {len(df_large)} 行")
```

### 添加自定义字段
```python
from sample_data_generator import generate_sales_data
import numpy as np

df = generate_sales_data()

# 添加自定义列
df['discount'] = np.random.uniform(0, 0.3, len(df))
df['final_price'] = df['price'] * (1 - df['discount'])
df['revenue'] = df['final_price'] * df['quantity']

print(df)
```

---

## ⚡ 性能提示

1. **大数据集**: 生成大量数据时考虑内存限制
2. **随机种子**: 使用 `np.random.seed(42)` 确保可重现
3. **批量生成**: 需要多次使用时，生成一次保存为文件
4. **增量测试**: 先用小数据集测试，确认无误后再用大数据集

---

## 📚 相关资源

- [Python面试题库](./PYTHON_INTERVIEW_QUESTIONS.md) - 配套练习题
- [面试快速指南](./INTERVIEW_QUICK_GUIDE.md) - 面试准备
- [pandas官方文档](https://pandas.pydata.org/docs/) - 深入学习

---

## 💪 练习建议

### 初学者
1. 从 `generate_dirty_dataframe()` 开始
2. 练习基本的数据清洗操作
3. 逐步增加复杂度

### 中级
1. 使用 `generate_relational_data()` 练习 merge
2. 使用 `generate_timeseries_data()` 练习时间序列
3. 尝试多表关联和复杂聚合

### 高级
1. 使用 `generate_user_behavior_data()` 做留存分析
2. 使用 `generate_transaction_data()` 做异常检测
3. 综合使用多个数据源完成完整分析

---

## 🎯 常见问题

**Q: 数据每次运行都不一样怎么办？**
A: 在代码开头添加 `np.random.seed(42)` 固定随机种子

**Q: 如何生成特定格式的数据？**
A: 参考现有函数修改，或者手动创建 DataFrame

**Q: 生成的数据能用于生产环境吗？**
A: 不建议，这些是用于学习和测试的样例数据

**Q: 如何生成更真实的数据？**
A: 可以使用 `faker` 库生成更真实的姓名、地址等信息

---

**Happy Coding! 🚀**
