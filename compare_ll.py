class Node:
    def __init__(self, nodeValue):
        self.data = nodeValue
        self.next = None

#do not change anything above This
def Compare(list1 ,list2):
	head1=list1
	head2=list2
	if head1 is None and head2 is None:
		return 0
	if head1 is not None and head2 is None:
		return 1
	if head2 is not None and head1 is None:
		return -1
	num1=0
	num2=0
	while(head1!=None):
		num1=num1*10+head1.data
		head1=head1.next
	while(head2!=None):
		num2=num2*10+head2.data
		head2=head2.next
	if num1>num2:
		return 1
	if num2>num1:
		return -1
	if num2==num1:
		return 0
    #compelete the code
#do not change anything below this



def buildListFromArray(givenArray):

    numElements = len(givenArray)
    if numElements == 0:
        return None
    head = Node(givenArray[0])
    prevNode = head
    for index in range(1, numElements):
        newNode = Node(givenArray[index])
        prevNode.next = newNode
        prevNode = newNode
    return head

if __name__ == '__main__':

    numTest = int(input())

    for i in range(numTest):

        n, m = map(int, input().split())

        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))

        head1, head2 = buildListFromArray(arr1), buildListFromArray(arr2)


        flag = Compare(head1, head2)

        print(flag)