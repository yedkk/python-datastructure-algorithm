#Lab #9
#Due Date: 03/01/2019, 11:59PM
########################################
#                                      
# Name:
# Collaboration Statement:             
#  
########################################


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        

                          
class OrderedLinkedList:
    '''
        >>> x=OrderedLinkedList()
        >>> x.pop()
        'List is empty'
        >>> x.add(-6)
        >>> x.add(8)
        >>> x.add(3)
        >>> x.add(7)
        >>> print(x)
        Head:Node(8)
        Tail:Node(-6)
        List:8 7 3 -6
        >>> len(x)
        4
        >>> x.pop()
        -6
        >>> print(x)
        Head:Node(8)
        Tail:Node(3)
        List:8 7 3
    '''
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return ('Head:{}\nTail:{}\nList:{}'.format(self.head,self.tail,out))

    __repr__=__str__

    def add(self, value):
        #write your code here

# transfer the value to node class
        node = Node(value)

# see whether the linked list is empty
        if self.head == None:
            self.head = node
            self.tail = node

# see whether the lined list only have one node
        elif self.head.value < value:
            node.next = self.head
            self.head = node

# decide whether need to insert value into middle and tail of the linked list
        elif self.head.value >= value:

# set the variables
            cur = self.head
            pre = None

# set the while loop that can assign right position to variables
            while cur != None and value < cur.value:
                pre = cur
                cur = cur.next

# insert the node
            if cur == None:
                pre.next = node
                node.next = cur
                self.tail = node

# insert the node
            else:
                pre.next = node
                node.next = cur

    def pop(self):
        #write your code here

# see whether the linked list is none
        if self.head != None:

# set the variables
            cur = self.head
            pre = None
            prev = None

# use the while loop to get the tail
            while cur != None:
                prev = pre
                pre = cur
                cur = cur.next
            else:

# return the tail value and remove it
                self.tail = prev
                prev.next = None
                return pre.value
        else:
            return 'List is empty'

    def isEmpty(self):
        #write your code here

# decide whether the linked list is empty and return result
        return self.head == None

    def __len__(self):
        #write your code here

# set the variables
        cur = self.head
        count = 0

# use the while loop to get the tail and count number, then return the answer
        while cur != None:
            count += 1
            cur = cur.next
        return count
