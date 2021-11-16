# single node for DLL
class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class DLL:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def forwardTraversal(self):
        temp = self.head
        while (temp != None):
            print(temp.data, end="<->")
            temp = temp.next
        print("\n") # just for new Line..
    
    def backTraversal(self):
        temp = self.tail
        while (temp != None):
            print(temp.data, end="<->")
            temp = temp.prev
        print("\n")  

    def append(self, val): # Insersion at end..
        newNode = Node(val)
        # exit first code..
        if self.head is None:
            self.head = newNode
            self.tail = self.head # when only one node tail and head are same..
            return
        
        # if head not none you traverse unitl tail or if you have tail already you 
        # just point the 
        self.tail.next = newNode # 1 -> 2
        newNode.prev = self.tail # 1 <-> 2 -> None
        # None is Null.. so it is not a object.. so it wont have prev and next Nodes..!!!

        # change the tail..
        self.tail = newNode
    
    def insertionAtHead(self, val):
        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            self.tail = self.head # when only one node tail and head are same..
            return
        
        # None <- 1 -> None
        newNode.next = self.head # 2 -> 1 -> None
        self.head.prev = newNode # 2 -> <- 1

        self.head = newNode # 2..is the head now..

    
dll = DLL()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.append(6)

dll.forwardTraversal() # 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <->
dll.backTraversal() # 6 <-> 5 <-> 4 <-> 3 <-> 2 <-> 1 <->

dll.insertionAtHead(7)
dll.insertionAtHead(8)
dll.insertionAtHead(9)

dll.forwardTraversal() # 9 <-> 8 <-> 7 <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <->
        

        

        


