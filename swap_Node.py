# Node class 
class Node: 

	# Constructor to initialize the node object 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList:
# Function to initialize head 
    def __init__(self): 
        self.head = None

# Do not change anything above this line
    def swapNodes(self): 
        # YOU ONLY NEED TO COMPLETE THIS FUNCTION.
        prev=self.head
        if prev is None or prev.next==None:
        	return
        temp=prev.next
        swap=None
        i=0
        while(temp!=None):
        	if(i==0):
        		prev.next=temp.next
        		temp.next=prev
        		self.head=temp
        		swap=self.head.next
        		prev=prev.next
        		temp=prev.next
        		i+=1
        	else:
        		prev.next=temp.next
        		temp.next=prev
        		swap.next=temp
        		swap=temp.next
        		prev=prev.next
        		if(prev==None):
        			break
        		temp=prev.next
        		
        		
  
  
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data, end=" ")
            temp = temp.next


# Do not change anything below this line
if __name__ == '__main__':
    
    n = int(input())

    # Start with the empty list 
    llist = LinkedList() 

    temp = [int(x) for x in input().split()]

    if(n<1):
        llist.head = None
    elif(n<2):
        llist.head = Node(temp[0])
    else:
        llist.head = Node(temp[0])
        second = Node(temp[1])
        llist.head.next = second
        curr = llist.head.next


    for i in range(2,n):
        t = Node(temp[i])
        curr.next = t
        curr = curr.next

    llist.swapNodes()
    llist.printList()