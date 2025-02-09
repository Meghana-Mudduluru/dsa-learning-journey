stack=[]
def push():
    #if len(stack)==n:
        #print("Stack is full")
    #else:
    element=input("Enter the element:")
    stack.append(element)
    print("Stack is :",stack)
def pop():
    if not stack:
        print("Stack is empty")
    else:
        e=stack.pop()
        print("removed element:",e)
        print("Stack is:",stack)
def top():
    top=stack[-1]
    print("Top element in the stack is:",top)

#n=int(input("limit of stack:"))
while True:
    #print("Enter the operation you want , 1.push 2.pop 3.top 4.quit")
    choice=int(input("Enter the operation you want , 1.push 2.pop 3.top 4.quit\n"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        top()
    elif choice==4:
        break
    else:
        print("Select the correct choice")
