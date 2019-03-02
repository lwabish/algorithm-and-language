# 用deque实现保留最新的N个元素
from collections import deque

# 只保留最新的5个元素，加入元素后超过5个，那么最旧的会丢掉
data = deque(maxlen=5)


# 在队列两端插入或删除元素时间复杂度都是 O(1) ，
# 而在列表的开头插入或删除元素的时间复杂度为 O(N) 。
