
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
                print(n.data,end=' - ')
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
            new_node=node(data)
            new_node.ref=n.ref
            n.ref=new_node

    # add before node
    def before_node(self,data,x):
        if self.head == None:
            print("Linked list is empty")
            return
        if self.head.data==x:
            new_node=node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n.ref!=None: # to get the previous node
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref == None:
            print("Node is not found")
        else:
            new_node=node(data)
            new_node.ref=n.ref
            n.ref=new_node

    # insert when linked list is empty
    def insert_empty(self,data):
        if self.head == None:
            new_node=node(data)
            self.head=new_node
        else:
            print("Linked list is not empty")

    # delete starting node
    def delete_begin(self):
        if self.head == None:
            print("linked list is empty can't delete")
        else:
            self.head=self.head.ref

    # delete end node
    def delete_end(self):
        if self.head == None:
            print("Linked list is empty can't delete")
        # when only one element is present
        elif self.head.ref == None:
            self.head = None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None

    # delete any node by value
    def delete_byValue(self,x):
        if self.head is None:
            print("linked list is empty can't delete")
            return
        if self.head.data==x:
            self.head=self.head.ref
            return
        # to find the previous node
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print("Node is not present")
        else:
            n.ref=n.ref.ref


ll1=LinkedList()
ll1.add_begin(10)
ll1.add_begin(20)
#ll1.add_begin(30)
#ll1.add_end(100)
#ll1.after_node(200,100)
#ll1.before_node(150,300)
#ll1.add_begin(25)
#ll1.insert_empty(10)
#ll1.insert_empty(110)
#ll1.delete_begin()
#ll1.delete_end()
ll1.delete_byValue(10)
ll1.print_LL()
