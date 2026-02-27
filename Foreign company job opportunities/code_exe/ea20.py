"""
题目20：数据验证和错误处理
难度：⭐⭐⭐ (Medium)
来源：Consulting firms, Financial companies
考点：数据验证、异常处理

题目描述：
Validate a DataFrame and return a report of errors:
1. Check for null values in required columns
2. Check if email format is valid
3. Check if age is within valid range (0-120)
4. Return a summary of all errors found

Example:
Input DataFrame:
   id  name     email           age
0  1   Alice    alice@test.com  25
1  2   None     invalid_email   150
2  3   Charlie  None            -5

Output:
{
  'null_values': {'name': [1], 'email': [2]},
  'invalid_email': [1, 2],
  'invalid_age': [1, 2]
}
"""
import re
import pandas as pd

def validate_data(df):
    """
    Solution 20: 数据验证

    Time Complexity: O(n*m) where n is rows, m is columns
    Space Complexity: O(k) where k is number of errors
    """
    errors = {
        'null_values': {},
        'invalid_email': [],
        'invalid_age': []
    }

    # Check null values in required columns
    required_cols = ['name', 'email']
    for col in required_cols:
        null_indices = df[df[col].isnull()].index.tolist()
        if null_indices:
            errors['null_values'][col] = null_indices

    # Validate email format
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    for idx, email in df['email'].items():
        if pd.notna(email) and not re.match(email_pattern, str(email)):
            errors['invalid_email'].append(idx)
        elif pd.isna(email):
            errors['invalid_email'].append(idx)

    # Validate age range
    for idx, age in df['age'].items():
        if pd.notna(age) and (age < 0 or age > 120):
            errors['invalid_age'].append(idx)

    return errors

# Test
def test_validate_data():
    data = {
        'id': [1, 2, 3],
        'name': ['Alice', None, 'Charlie'],
        'email': ['alice@test.com', 'invalid_email', None],
        'age': [25, 150, -5]
    }
    df = pd.DataFrame(data)

    errors = validate_data(df)
    print("题目20 - 数据验证:")
    print("Errors found:")
    for error_type, details in errors.items():
        if details:
            print(f"  {error_type}: {details}")
    print()

if __name__ == "__main__":
    test_validate_data()
