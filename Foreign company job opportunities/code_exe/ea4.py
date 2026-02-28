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
import pandas as pd
import numpy as np

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
    monthly = df.resample('ME').sum()
    monthly['mom_growth'] = monthly['value'].pct_change() * 100

    return daily_avg, monthly

# Test
def test_timeseries():
    # 生成3个月的数据（每12小时一个点，共180个点）
    dates = pd.date_range('2024-01-01', periods=180, freq='12h')
    # 模拟有增长趋势的数据（随着时间增长，基础值增加）
    np.random.seed(42)  # 设置随机种子，确保结果可复现
    base_values = np.linspace(100, 150, 180)  # 从100逐渐增长到150
    noise = np.random.randint(-20, 20, 180)   # 添加随机波动
    values = base_values + noise

    data = {
        'timestamp': dates,
        'value': values
    }
    df = pd.DataFrame(data)
    print("原始数据:")  
    print(df.head()) ## head 显示前5行数据
    print()

    daily, monthly = analyze_timeseries(df)
    print("=" * 60)
    print("题目4 - 时间序列分析")
    print("=" * 60)

    print("\n【1. 每日平均值】前5天:")
    print(daily[['value']].head())

    print("\n【2. 7日滚动平均】第7-10天（开始有数据）:")
    print(daily[['value', 'rolling_7d']].iloc[6:10]) ## iloc 从第7行开始显示，显示4行数据

    print("\n【3. 月度汇总与环比增长】:")
    print("-" * 60)
    print(f"{'月份':<15} {'月度总和':<15} {'环比增长率':<15}")
    print("-" * 60)
    for idx, row in monthly.iterrows():
        month_str = idx.strftime('%Y年%m月')
        value_str = f"{row['value']:.2f}"
        growth_str = f"{row['mom_growth']:.2f}%" if not pd.isna(row['mom_growth']) else "N/A (首月)"
        print(f"{month_str:<15} {value_str:<15} {growth_str:<15}")
    print("=" * 60)
    print()
    

if __name__ == "__main__":
    test_timeseries()
