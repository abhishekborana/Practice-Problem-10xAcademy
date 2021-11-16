   def deletePositionX(self, x):
        if x <=0:
            # Invalid x is given..!
            return
        
        if x == 1:
            # delete head
            temp = self.head
            self.head = temp.next
            del(temp) # Freeing the a node's memory deleting it
            return
        
        temp = self.head
        temp_posi = 1
        while(temp_posi < (x-1) and temp != None):
            temp = temp.next
            temp_posi += 1
        
        if temp is None:
            # Invalid x is given..
            return
        
        # temp is at previous node of the delete node..
        # a -> b -> c -> d -> e ->None x  = 3.
        # if x = 2 temp is "a"
        delNode = temp.next # c... # if x = 2 then b..
        print(delNode)
        temp.next  = temp.next.next # b.next = d # a.next = c
        print(delNode.val)
        del(delNode)   # freeing up or deleting c.. #.. for b..
        
        
    # x, temp, temp_posi
    # 2, a , 1
    
    # we want del "d" = target
    def deleteValueX(self, target):
        prev = None
        curr = self.head

        if curr.val == target:
            # head
            self.head = curr.next
            return

        while(curr != None):
            if (curr.val == target):
                break

            prev = curr
            curr = curr.next
        
        if curr is None:
            # we didn't find the target
            return

        # now curr is delNode and prev is it's prev
        prev.next  = curr.next # prev.next.next
        del(curr)