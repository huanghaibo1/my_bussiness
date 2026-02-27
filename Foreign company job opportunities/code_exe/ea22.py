"""
题目22：SQL结果转Python数据结构
难度：⭐⭐ (Medium)
来源：Data engineering positions
考点：数据转换、字典操作

题目描述：
Given a list of tuples (simulating SQL query result),
convert it to different Python data structures:
1. List of dictionaries
2. Dictionary grouped by a key
3. Pivot table structure

Example:
Input: [('Alice', 'Sales', 5000), ('Bob', 'IT', 6000), ('Charlie', 'Sales', 5500)]
Columns: ['name', 'department', 'salary']

Output 1 (list of dicts):
[
  {'name': 'Alice', 'department': 'Sales', 'salary': 5000},
  {'name': 'Bob', 'department': 'IT', 'salary': 6000},
  ...
]

Output 2 (grouped by department):
{
  'Sales': [{'name': 'Alice', 'salary': 5000}, {'name': 'Charlie', 'salary': 5500}],
  'IT': [{'name': 'Bob', 'salary': 6000}]
}
"""

def convert_sql_result(rows, columns):
    """
    Solution 22: SQL结果转换
    """
    # 1. List of dictionaries
    list_of_dicts = [dict(zip(columns, row)) for row in rows]

    # 2. Grouped by department
    grouped = {}
    for row in rows:
        dept = row[1]  # department column
        if dept not in grouped:
            grouped[dept] = []
        grouped[dept].append({
            'name': row[0],
            'salary': row[2]
        })

    return list_of_dicts, grouped

# Test
def test_convert_sql():
    rows = [('Alice', 'Sales', 5000), ('Bob', 'IT', 6000), ('Charlie', 'Sales', 5500)]
    columns = ['name', 'department', 'salary']

    list_result, grouped_result = convert_sql_result(rows, columns)

    print("题目22 - SQL结果转换:")
    print("\nList of dicts:")
    for item in list_result:
        print(f"  {item}")

    print("\nGrouped by department:")
    for dept, employees in grouped_result.items():
        print(f"  {dept}: {employees}")
    print()

if __name__ == "__main__":
    test_convert_sql()
