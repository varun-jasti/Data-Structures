# Queue using List
queue = []
def enqueue():
    if len(queue) == n:
        print("Queue is full")
    else:
        ele = input("Enter the element:")
        queue.append(ele)
        print(queue)
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e = queue.pop(0)
        print("removed element:",e)
def display():
    print(queue)  
n = int(input("Enter the size of queue:"))
while True:
    print("Select option: 1.enqueue 2.dequeue 3.show 4.exit")
    choice = int(input())
    if choice==1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Enter the correct option!")

# output:
# Enter the size of queue:2
# Select option: 1.enqueue 2.dequeue 3.show 4.exit
# 1
# Enter the element:2
# ['2']
# Select option: 1.enqueue 2.dequeue 3.show 4.exit
# 1
# Enter the element:3
# ['2', '3']
# Select option: 1.enqueue 2.dequeue 3.show 4.exit
# 1
# Queue is full
# Select option: 1.enqueue 2.dequeue 3.show 4.exit
# 1
# Queue is full
# Select option: 1.enqueue 2.dequeue 3.show 4.exit
# 4
# ------------------------------------------------
# Enter the size of queue:3
# Select option: 1.enqueue 2.dequeue 3.show 4.exit
# 1
# Enter the element:1
# ['1']
# Select option: 1.enqueue 2.dequeue 3.show 4.exit
# 1
# Enter the element:2
# ['1', '2']
# Select option: 1.enqueue 2.dequeue 3.show 4.exit
# 1
# Enter the element:3
# ['1', '2', '3']
# Select option: 1.enqueue 2.dequeue 3.show 4.exit
# 2
# removed element: 1
# Select option: 1.enqueue 2.dequeue 3.show 4.exit
# 3
# ['2', '3']
# Select option: 1.enqueue 2.dequeue 3.show 4.exit
# 4