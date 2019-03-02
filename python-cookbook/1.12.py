# 序列内容计数
from collections import Counter
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

# Counter的参数必须hashable
word_counts = Counter(words)
# print(word_counts)

top_3 = word_counts.most_common(3)
print(top_3)

# 更优秀的用法：多个Counter的数学运算
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
more_counter = Counter(morewords)
total_counter = word_counts + more_counter
print(total_counter.most_common(3))
