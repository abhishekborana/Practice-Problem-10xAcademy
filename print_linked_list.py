class Node:
    def __init__(self, key):
        self.data = key
        self.next = None


class LL:
    def __init__(self):
        self.head = None
        
    #complete the Display function given below
    def display(self):
    	temp=self.head
    	if(temp.next!=None):
    		print("head",end="->")
    		while(temp.next!=None):
    			print(temp.data,end="->")
    			temp=temp.next
    			
    	print(temp.data,"->None")
    @staticmethod
    def insert_node(val, current):
        temp = Node(val)
        current.next = temp
        current = current.next
        return current


ll = LL()
num = [int(i) for i in input().split("->")]
ll.head = Node(num[0])
curr = ll.head
for i in num[1:]:
    curr = LL.insert_node(i, curr)
ll.display()