stack =[]
def pushstk():
    if len(stack) == n:
        print("Stack is full!")
    else:
        ele = input("Enter the element:")
        stack.append(ele)
        print(stack)
def popele():
    if not stack:
        print("Stack is empty")
    else:
        e = stack.pop()
        print("element removed:",e)
        print(stack)
n = int(input("Enter the size of the stack:"))

while True:
    print("Select option: 1.push 2.pop 3.exit")
    choice = int(input())
    if choice==1:
        pushstk()
    elif choice == 2:
        popele()
    elif choice == 3:
        break
    else:
        print("Enter the correct option!")

# Sample Output:
# Enter the size of the stack:3
# Select option: 1.push 2.pop 3.exit
# 1
# Enter the element:2
# ['2']
# Select option: 1.push 2.pop 3.exit
# 1
# Enter the element:3
# ['2', '3']
# Select option: 1.push 2.pop 3.exit
# 1
# Enter the element:4
# ['2', '3', '4']
# Select option: 1.push 2.pop 3.exit
# 1
# Stack is full!
# Select option: 1.push 2.pop 3.exit
# 4
# Enter the correct option!
# Select option: 1.push 2.pop 3.exit
# 2
# element removed: 4
# ['2', '3']
# Select option: 1.push 2.pop 3.exit
# 3