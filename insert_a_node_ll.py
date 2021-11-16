class Node: 
    def __init__(self, value): 
        self.data = value 
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_value): 
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
          
    def makeListAndPrint(self):
        #####WRITE CODE HERE####
        newLL = LinkedList()
        newLL.head=None
        newLL.tail=None
        
        temp=self.head
        while(temp!=None):
        	if int(temp.next.data)==0:
        		currTemp=newLL.head
        		newLL.head=Node(int(temp.data))
        		if currTemp is None:
        			newLL.tail=newLL.head
        		newLL.head.next=currTemp
        	else:
        		newLL.push(int(temp.data))
        	temp=temp.next.next
        temp=newLL.head
        while(temp!=None):
        	print(temp.data,end=" ")
        	temp=temp.next
        	
        	
        return
            
        

def read_list_input():
    vals = input().split(' ')
    linkedList = LinkedList() 
    for val in vals:
        linkedList.push(val)
    return linkedList

test_cases = int(input())
for i in range(test_cases):
    linkedList = read_list_input()
    linkedList.makeListAndPrint()