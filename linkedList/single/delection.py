class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Slinked:
    def __init__(self):
        self.head=None

    def display(self):
        temp=self.head
        if self.head is None:
            print("empty")
        else:
            while temp:
                print(temp.data)
                temp=temp.next

    def beg(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb

    def end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne

    def mid(self,data,pos):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.data=data
        np.next=temp.next
        temp.next=np

    def dbeg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None

    def dend(self):
        temp=self.head.next
        prev=self.head
        while temp.next:
            temp=temp.next
            prev=prev.next
        prev.next=None

    def dmid(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None

s1=Slinked()
s1.beg(88)
s1.beg(22)
s1.end(89)
s1.end(99)
s1.mid(12,3)
s1.dbeg()
s1.dend()
s1.dmid(2)
s1.display()