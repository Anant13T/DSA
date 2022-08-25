class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    
class DLL:
    def __init__(self):
        self.head=None
    
    def display(self):
        if self.head is None:
            print("empty list")
        else:
            temp=self.head
            while temp:
                print(temp.data)
                temp=temp.next
    
    def Ib(self,data):
        nb=Node(data)
        temp=self.head
        temp.prev=nb
        nb.next=temp
        self.head=nb
    
    def IE(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=ne
        ne.prev=temp

    def IP(self,data,pos):
        np=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        np.prev=temp
        np.next=temp.next
        temp.next.prev=np
        temp.next=np
    
    def DB(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.head.prev=None

    def DE(self):
        temp=self.head.next
        before=self.head
        while temp.next is not None:
            temp=temp.next
            before=before.next
        temp.prev=None
        before.next=None

    def DP(self,pos):
        temp=self.head.next
        before=self.head
        for i in range(1,pos-1):
            temp=temp.next
            before=before.next
        before.next=temp.next
        temp.next.prev=before
        temp.next=None
        temp.prev=None
        pass