#Lab #11
#Due Date: 03/15/2019, 11:59PM
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
                        
                          
class Queue:
    '''
        >>> x=Queue()
        >>> x.isEmpty()
        True
        >>> x.dequeue()
        'Queue is empty'
        >>> x.enqueue(1)
        >>> x.enqueue(2)
        >>> x.enqueue(3)
        >>> x.dequeue()
        1
        >>> print(x)
        Head:Node(2)
        Tail:Node(3)
        Queue:2 3
    '''
    def __init__(self):
        # set the head and tail
        self.head = None
        self.tail = None

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return ('Head:{}\nTail:{}\nQueue:{}'.format(self.head,self.tail,out))

    __repr__=__str__

    def isEmpty(self):
        # see whether is empty and return result
        return self.head == None

    def __len__(self):
        # set the variable and count
        cur = self.head
        count = 0
        # use the loop to count the the length and return a int
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def enqueue(self, value):
        # get the value and transfer to the node
        queue = Node(value)
        # see whether is empty
        if self.head == None:
            self.head = queue
            self.tail = queue
        # if have one, insert to tail
        elif self.head.next == None:
            self.head.next = queue
            self.tail = queue
        else:
            # else insert to tail
            cur = self.head
            pre = None
            while cur.next != None:
                pre = cur.next
                cur = cur.next
            pre.next = queue
            self.tail = queue


    def dequeue(self):
        # if it is empty return error
        if self.head == None:
            return 'Queue is empty'
        else:
            # else set variable, inset value and return value
            cur = self.head
            self.head = self.head.next
            if self.head == None:
                self.tail = None
            return cur.value

