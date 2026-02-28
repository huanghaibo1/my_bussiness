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
    dates = pd.date_range('2024-01-01', periods=30, freq='12h')
    data = {
        'timestamp': dates,
        'value': np.random.randint(100, 200, 30)
    }
    df = pd.DataFrame(data)
    print("原始数据:")  
    print(df.head())
    print()

    daily, monthly = analyze_timeseries(df)
    print("题目4 - 时间序列分析:")
    print("Daily averages (first 5):")
    print(daily.head())
    print()

if __name__ == "__main__":
    test_timeseries()
