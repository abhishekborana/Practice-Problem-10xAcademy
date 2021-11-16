class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current
 
    def remove(self, node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next
 
    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
 
# Implement this Function 
def remove_duplicates(llist):
	temp=llist.head
	prev=temp
	if temp is None:
		return
	res=[]
	while(temp!=None):
		r=temp.data
		if r not in res:
			res.append(r)
			
		temp=temp.next
	print(res)
	for i in range(len(res)):
		prev.data=res[i]
		if(i==len(res)-1):
			prev.next=None
		else:
			prev=prev.next
		
	while(prev!=None):
		c=prev
		print(c.data)
		del(c)
		prev=prev.next
	#print(res)
	
	
	
 
 
a_llist = LinkedList()
 
n = int(input())
l = list(map(int, input().split(' ')))
for data in l:
    a_llist.append(data)
 
remove_duplicates(a_llist)
 
a_llist.display()