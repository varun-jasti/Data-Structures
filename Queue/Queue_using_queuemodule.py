import queue
q = queue.Queue()
q.put(10)
q.put(50)
q.put(30)
print(q)
q.get()
print(q)