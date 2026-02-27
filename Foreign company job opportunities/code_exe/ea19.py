"""
题目19：解析JSON并提取字段
难度：⭐⭐ (Medium)
来源：Microsoft, Amazon, Accenture
考点：JSON处理、数据提取

题目描述：
Given a list of JSON strings representing user data, extract and flatten
specific fields into a DataFrame.

Example:
Input:
[
  '{"id": 1, "name": "Alice", "address": {"city": "NYC", "zip": "10001"}}',
  '{"id": 2, "name": "Bob", "address": {"city": "LA", "zip": "90001"}}'
]

Output DataFrame:
   id  name  city   zip
0  1   Alice NYC    10001
1  2   Bob   LA     90001
"""
import json
import pandas as pd

def parse_json_to_dataframe(json_strings):
    """
    Solution 19: JSON解析

    Time Complexity: O(n*m) where n is number of records, m is avg fields
    Space Complexity: O(n*m)
    """
    data = []

    for json_str in json_strings:
        obj = json.loads(json_str)

        # Flatten nested structure
        flat_obj = {
            'id': obj['id'],
            'name': obj['name'],
            'city': obj['address']['city'],
            'zip': obj['address']['zip']
        }
        data.append(flat_obj)

    return pd.DataFrame(data)

# Test
def test_parse_json():
    json_strings = [
        '{"id": 1, "name": "Alice", "address": {"city": "NYC", "zip": "10001"}}',
        '{"id": 2, "name": "Bob", "address": {"city": "LA", "zip": "90001"}}'
    ]

    result = parse_json_to_dataframe(json_strings)
    print("题目19 - JSON解析:")
    print(result)
    print()

if __name__ == "__main__":
    test_parse_json()
