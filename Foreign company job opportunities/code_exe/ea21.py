"""
题目21：处理CSV文件并生成报表
难度：⭐⭐⭐ (Medium-Hard)
来源：Real-world scenario
考点：文件处理、数据清洗、聚合

题目描述：
Read a CSV file, clean the data, and generate a summary report:
1. Remove rows with missing critical data
2. Convert data types appropriately
3. Calculate summary statistics
4. Export cleaned data to new CSV

This simulates a real ETL task.
"""
import pandas as pd

def process_csv_file(input_file, output_file):
    """
    Solution 21: CSV处理和报表生成

    This would be a complete ETL pipeline in real scenario
    """
    # Read CSV
    df = pd.read_csv(input_file)

    # Data cleaning
    # 1. Remove duplicates
    df = df.drop_duplicates()

    # 2. Handle missing values
    df = df.dropna(subset=['id', 'date'])  # Required fields

    # 3. Convert data types
    df['date'] = pd.to_datetime(df['date'])
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

    # 4. Remove outliers (example: amounts outside 3 std devs)
    mean = df['amount'].mean()
    std = df['amount'].std()
    df = df[(df['amount'] >= mean - 3*std) & (df['amount'] <= mean + 3*std)]

    # Generate summary report
    summary = {
        'total_records': len(df),
        'date_range': f"{df['date'].min()} to {df['date'].max()}",
        'total_amount': df['amount'].sum(),
        'avg_amount': df['amount'].mean(),
        'categories': df['category'].value_counts().to_dict()
    }

    # Export cleaned data
    df.to_csv(output_file, index=False)

    return summary

# Note: This is a template. In real interview, you'd discuss approach rather than full implementation

# Test
def test_process_csv():
    print("题目21 - CSV处理和报表生成:")
    print("这是一个模板函数，展示了完整的ETL流程:")
    print("1. 读取CSV文件")
    print("2. 清洗数据（去重、处理缺失值、类型转换、异常值处理）")
    print("3. 生成统计报表")
    print("4. 导出清洗后的数据")
    print()

if __name__ == "__main__":
    test_process_csv()
