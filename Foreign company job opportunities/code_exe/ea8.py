"""
题目8：合并区间
难度：⭐⭐⭐ (Medium)
来源：Amazon (LeetCode 56)
考点：排序、区间合并

题目描述：
Given a collection of intervals, merge all overlapping intervals.

Example:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
"""

def merge_intervals(intervals):
    """
    Solution 8: 区间合并

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        # If overlapping, merge
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged

# Test
def test_merge_intervals():
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print("题目8 - 区间合并:")
    print(f"Input: {intervals}")
    print(f"Output: {merge_intervals(intervals)}")
    print()

if __name__ == "__main__":
    test_merge_intervals()
