import collections
queue = collections.deque()
queue.appendleft(10)
queue.appendleft(20)
queue.appendleft(30)
# queue.pop()
# or
# queue.append(10)
# queue.append(20)
# queue.append(30)
# queue.popleft()
#  print(not queue)
print(queue)
# print(queue[-1])
# print(queue[0])
# Output:
# False
# deque([10, 20, 30])
# 30
# 10