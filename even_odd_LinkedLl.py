head = None
class Node:  
      
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data # Assign data  
        self.next =None
  
def segregateEvenOdd(): 
	global head
	temp=head
	if temp is None or temp.next is None:
		return
	tempOdd=None
	tempEven=None
	headOdd=None
	
	while(temp!=None):
		c=temp
		temp=temp.next
		c.next=None
		if(c.data%2==0):
			if(tempEven==None):
				tempEven=c
				head=tempEven
			else:
				tempEven.next=c
				tempEven=tempEven.next
		elif(c.data%2!=0):
			if(tempOdd==None):
				tempOdd=c
				headOdd=c
			else:
				tempOdd.next=c
				tempOdd=tempOdd.next
		
	
	tempEven.next=headOdd
		
  
  # Implement This only "BE CAREFUL HEAD IS GLOBALLY DECLARED"
          
# Given a reference (pointer to pointer) to the head 
# of a list and an int, push a new node on the front 
# of the list.  
def push(new_data): 
    global head 
  
    # 1 & 2: Allocate the Node & 
    #         Put in the data 
    new_node = Node(new_data) 
  
    # 3. Make next of new Node as head  
    new_node.next = head 
  
    # 4. Move the head to point to new Node  
    head = new_node 
  
# Utility function to print a linked list 
def printList(): 
    global head 
    temp = head 
    while(temp != None): 
          
        print(temp.data, end = " ") 
        temp = temp.next
          
    print(" ") 
  
# Driver program to test above functions  

n = int(input())
l = list(map(int, input().split()))
l.reverse()  
for i in l:
    push(i)  
segregateEvenOdd() 
printList()	