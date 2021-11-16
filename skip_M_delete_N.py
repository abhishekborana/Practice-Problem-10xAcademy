# Python program to delete M nodes after N nodes 
  
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
  
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to prit the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.data, end=' ') 
            temp = temp.next
  
    def skipMdeleteN(self, M, N):
        # Implment This 
        if(M<0 or N<0):
        	return
        temp=self.head
        if temp is None:
        	return
        pos=1
        while(temp!=None):
        	temp=temp.next
        	pos+=1
        	if(pos==M):
        		#print(temp)
        		if(temp==None):
        			break
        		nextTemp=temp.next
        		pos2=1
        		while(pos2<N and nextTemp!=None):
        			nextTemp=nextTemp.next
        			pos2+=1
        		if nextTemp is None:
        			temp.next=nextTemp
        		else:
        			temp.next=nextTemp.next
        			temp=nextTemp.next
        		pos=1
        	
        	
          
  
# Driver program to test above function 
  

n = int(input())
M,N = map(int, input().split())
llist = LinkedList() 
l = list(map(int, input().split()))
l.reverse()
for i in l:
    llist.push(i)

llist.skipMdeleteN(M, N) 
  
llist.printList()