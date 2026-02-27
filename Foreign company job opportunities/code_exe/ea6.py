"""
题目6：字符串反转和去重
难度：⭐ (Easy)
来源：所有公司基础题
考点：字符串操作、列表推导式

题目描述：
Write a function that takes a sentence and returns:
1. Reversed sentence (word order)
2. Unique words (case-insensitive)
3. Word count

Example:
Input: "Hello World Hello Python"
Output:
- Reversed: "Python Hello World Hello"
- Unique: ['hello', 'world', 'python']
- Count: 4
"""

def analyze_sentence(sentence):
    """
    Solution 6: 字符串分析

    Time Complexity: O(n) where n is length of sentence
    Space Complexity: O(n)
    """
    words = sentence.split()

    # Reversed sentence
    reversed_sentence = ' '.join(reversed(words))

    # Unique words (case-insensitive)
    unique_words = list(set(word.lower() for word in words))
    unique_words.sort()

    # Word count
    word_count = len(words)

    return {
        'reversed': reversed_sentence,
        'unique': unique_words,
        'count': word_count
    }

# Test
def test_analyze_sentence():
    result = analyze_sentence("Hello World Hello Python")
    print("题目6 - 字符串分析:")
    print(result)
    print()

if __name__ == "__main__":
    test_analyze_sentence()
