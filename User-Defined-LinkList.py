class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next  = next

# create a linked list
# insert at head
# insert at tail
# insert in b/w
# display the linked list.
# delete position x in linkedlist.
# array.. !! a = [] , ll = SinglyLinkedList()
class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # traversal of linked list !!!
    def display(self):
        temp = self.head
        while (temp != None):
            print(temp.val, end='->')
            temp = temp.next

        print("\n")
    # Insert Head ..
    # 3 -> 2 -> 1 -> 
    def insertAtHead(self, value): # O(1)
        # create a new Node
        # point the new node to head 
        # change the head.. to new Node..

        # Exit first is always good ...
        newNode = Node(value)
        if self.head is None:
            self.head = newNode # 1 -> None..
            self.tail = self.head
            return

        newNode.next = self.head 
        self.head = newNode

        # if self.head != None:
        #     newNode.next = self.head
        #     self.head = newNode
        #     return
        
        # self.head = newNode

    def insertAtEnd(self, value): # 1-> 2 ->3  O(n)
        # without tail.. 
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
            return
        
        temp = self.head
        while (temp.next != None):
            temp = temp.next
        
        # temp will be at last node now.
        temp.next = newNode # 1 -> 2-> 3-> 4
        self.tail = newNode

    def insertAtEndWithTail(self, value): # O(1)
        newNode = Node(value)
        if self.head is None:
            self.head = newNode # 1 -> None
            self.tail = self.head
        
        # 1 -> 2 -> 3 -> 4
        self.tail.next = newNode
        self.tail = newNode
    
    # a -> b -> c -> d -> e -> None postion start from 1, 2... if x is 0 insert before head
    # a -> b -> c -> d -> e -> None position starts from 0, 1, 2,... if x -1 is insert before head
    def insertAfterPositionX(self, x, value):
        if x < 0:
            return
        
        # check if ll is empty
        if self.head is None:
            return
        
        newNode = Node(value)
        # Insert before head case..
        if x == 0:
            newNode.next = self.head
            self.head = newNode
            return
        
        temp = self.head
        temp_posi = 1
        # a -> b -> c -> e ->d -> None -> ..??? x = 10
        # you dont have to define temp_posi you can use x only to land at required posi
        # while which decreses x ..
        while (temp_posi < x and temp != None):
            temp = temp.next
            temp_posi += 1
        
        if temp is None:
            return
        
        newNode.next = temp.next # e -> d
        temp.next = newNode
    
    # def insertBeforePositionX(self, x, value):
    
    # def deletePositionX():

    # depends upon the use case..
    # @staticmethod
    # def checkIfLinkedListIsPalindrome(Node head):



linkedlist = SinglyLinkedList()

linkedlist.insertAtHead('a') # 1 -> None
linkedlist.insertAtHead('b') # 2 -> 1 -> Noe..
linkedlist.insertAtHead('c') # ...
linkedlist.insertAtHead('d') # 4 -> 3 -> 2 -> 1 -> None..

linkedlist.display() # d->c->b->a->None..!!
print("Head ::" + str(linkedlist.head.val))
print("tail ::" + str(linkedlist.tail.val))
print("\n")


linkedlist.insertAfterPositionX(0, 'e') # e->d->c->b->a->None
linkedlist.display()

linkedlist.insertAfterPositionX(3, 'n') # e->d->c->n->b->a->None
linkedlist.display()

linkedlist.insertAfterPositionX(6, 'f') # e->d->c->n->b->a->f->None
linkedlist.display()

linkedlist.insertAfterPositionX(10, 'l') # e->d->c->n->b->a->f->None
linkedlist.display()




