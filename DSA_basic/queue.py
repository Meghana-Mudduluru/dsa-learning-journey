queue=[]
def enqueue():
    element= input("Enter the element:")
    queue.append(element)
    print(element,"is added to queue")
def dequeue():
    if not queue:
        print("The queue is empty")
    else:
        e=queue.pop(0)
        print(e,"is removed from the queue")
def display():
    print(queue)

while True:
    print("Enter the operation you want : 1.enqueue(add) 2.dequeue(remove) 3.display queue 4.quit\n")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Select the correct choice")