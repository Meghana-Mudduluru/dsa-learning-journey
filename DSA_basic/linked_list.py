class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None

    # traversal operation
    def print_LL(self):
        if self.head==None:
            print("Linked list is empty")
        else:
            n=self.head
            while n!=None:
                print(n.data,end='  ')
                n=n.ref

    # adding elements at the beginning of the linked list
    def add_begin(self,data):
        new_node=node(data)
        new_node.ref=self.head
        self.head=new_node

    # adding elements at the end of linked list
    def add_end(self,data):
        new_node=node(data)
        if self.head==None:
            self.head=new_node
        else:
            n=self.head
            while n.ref!=None:
                n=n.ref
            n.ref=new_node

    # add after node
    def after_node(self,data,x):
        n=self.head
        while n!=None:
            if x==n.data:
                break
            else:
                n=n.ref
        if n==None:
            print("node is not present in the list")
        else:
            

ll1=LinkedList()
#ll1.add_begin(10)
#ll1.add_begin(30)
ll1.add_end(100)
#ll1.add_begin(25)
ll1.print_LL()
