    # We assume our first node position is
    # a -> b -> c -> d-> e ->
    def insertAfterPositionX(self, x, val):
        if x < 0: # (-1, -2 , -3....)
            # invalid position..
            return
        newNode = Node(val)
        if x == 0:
            # Adding at head..
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            return
        # x 5...
        temp = self.head
        temp_p = 1
        while (temp_p < x and temp != None):
            temp = temp.next
            temp_p += 1
        
        if temp is None:
            # Invalid position x is greater than linked lenght..
            return

        # Now temp is at e -> None , f - newNode..
        # e - temp, None - d_node, f - newNode
        # a -> b -> c -> d-> e ->
        d_node = temp.next
        # new nodes pointerss..
        newNode.next =  d_node # f.next = (c.next)d
        if d_node != None: # this case is last Node case..
            d_node.prev = newNode # d.prev = f
        newNode.prev = temp # f.prev = c
        temp.next = newNode # c.next = f