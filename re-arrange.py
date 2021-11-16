class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next  = next
    
def display_in(node):
    temp = node
    while (temp != None):
        print(temp.val, end='->')
        temp = temp.next

    print("\n")

# Input -> head of a linked list
# output -> head of the reversed linked list..
def reverse_ll(head):
    # reverse the linked list
    # define prev and curr..
    prev = None
    curr = head

    # 1(p) -> 2(c)  3 -> 4 -> None..

    while(curr != None):
        temp = curr.next # temp(3)
        curr.next = prev # lost the next here... 2 -> 1

        # moving forward..
        prev = curr #  move prev to one step ahead
        curr = temp # move curr to one step ahead..

    return prev

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    # traversal of linked list !!!
    def display(self):
        temp = self.head
        while (temp != None):
            print(temp.val, end='->')
            temp = temp.next

        print("\n")

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

    # 1->2->3->4->5->6
    def re_arrange(self):
        # 1. Find middle.
        slow = self.head
        fast = self.head

        # after this loop slow pointer will be at middle..
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        
        # 2. split into two ll and 
        print(slow.val)
        head1 = self.head # 1->2->3-> None
        head2 = slow.next # 4->5->
        slow.next = None
        display_in(head1)

        # 3. reverse the 2nd one.
        head2 = reverse_ll(head2)
        display_in(head2)

        # 4. Merge the two linked list.
        curr = Node(0)

        # 0(c) -> None..
        # 1(h1) -> 2 -> 3
        # 5(h2) -> 4
        while(head1 != None or head2 != None):
            # Add node from first list
            if (head1 != None):
                curr.next = head1 # 0(c) -> 1 
                head1 = head1.next #  # 1 -> 2(h1) -> 3
                curr = curr.next # 0 -> 1(c)

            # Add node from 2nd list..
            if (head2 != None):
                curr.next = head2 # 0 -> 1(c) -> 5
                head2 = head2.next # 5 -> 4(h2) 
                curr = curr.next # # 0 -> 1 -> 5(c)
        
        # while (head1 != None):
        #     curr.next = head1
        #     head1 = head1.next
        #     curr = curr.next


ll = SinglyLinkedList()

ll.insertAtEnd(1)
ll.insertAtEnd(2)
ll.insertAtEnd(3)
ll.insertAtEnd(4)
ll.insertAtEnd(5)
# ll.insertAtEnd(6)

ll.display()
ll.re_arrange()
ll.display()

# 1 -> 2 -> 3 -> 4 -> 5 -> 6 ->

# 1 6 2 5 3 4