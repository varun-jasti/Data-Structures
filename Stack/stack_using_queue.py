
import queue
stack = queue.LifoQueue(3)
stack.put(1)
stack.put(2)
stack.put(3)
# stack.put(4,timeout=1) # output: queue.Full
stack.get()
while not stack.empty():
    item = stack.get()
    print(item,end = " ")