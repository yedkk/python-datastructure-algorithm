#Lab #10
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
                          

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        'Stack is empty'
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        # set the self top
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__
    
    def isEmpty(self):
        # see whether is empty and return result
        return self.top == None


    def __len__(self):
        # set the variable and count
        cur = self.top
        count = 0
        # use the loop to count the the length and return a int
        while cur != None:
            count += 1
            cur = cur.next
        return count
    
    def peek(self):
        # see whether is empty else return the top
        if self.top != None:
            return self.top.value
        else:
            return 'Stack is empty'

    def push(self,value):
        # get the value and transfer to the node
        stack = Node(value)
        # see whether is empty
        if self.top == None:
            self.top = stack
        # if is not empty, set variable and insert it
        else:
            cur = self.top
            stack.next = cur
            self.top = stack

    def pop(self):
        # if it is empty return error
        if self.top == None:
            return 'Stack is empty'
        else:
            # else set variable, inset value and return value
            cur = self.top
            self.top = self.top.next
            return cur.value



