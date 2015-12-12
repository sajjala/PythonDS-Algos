class Node:
    """ Node Class
        Basic unit of LinkedList
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addAtHead(self, item):
        new_node = Node(item)
        new_node.setNext(self.head)
        self.head = new_node

    def addInOrder(self, item):
        new_node = Node(item)
        if self.head is None:
            new_node.setNext(self.head)
            self.head = self.tail = new_node
        else:
            self.tail.setNext(new_node)
            self.tail = new_node

    def reverseListIterative(self):
        if(self.head is None or self.head.next is None):
            return self.head
        
        unrev_head, rev_head, curr_node= self.head, None, None
        while(unrev_head is not None):
            rev_head = curr_node
            curr_node = unrev_head
            unrev_head = unrev_head.getNext()
            curr_node.setNext(rev_head)

        rev_head = curr_node

        return rev_head

    def reverseListRecursive(self, head):
        if(head is None or head.next is None):
            return head

        next_node = head.getNext()
        head.setNext(None)

        rev_list = self.reverseListRecursive(next_node)
        next_node.next = head
        
        import pdb; pdb.set_trace()
        return rev_list

    def getSize(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count

    def isEmpty(self):
        return self.head == None

    def getItems(self):
        current = self.head
        items = []
        while current:
            items.append(current.getData())
            current = current.getNext()

        return items

    def searchItem(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def removeItem(self, item):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if not found:
            return

        if mprevious == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
