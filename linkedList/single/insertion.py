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

s1=Slinked()
s1.beg(5)
s1.beg(6)
s1.end(33)
s1.mid(25,2)
s1.display()