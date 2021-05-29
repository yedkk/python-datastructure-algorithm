#HW 6
#Due Date: 04/26/2019, 11:59PM
########################################
#
# Name:Kangdong Yuan
# Collaboration Statement:
#
########################################

# ---Copy your code from labs 10 and 11 here (you can remove their comments)  
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__


class Stack:
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

class Queue:
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
#----- HW6 Graph code     
class Graph:
    def __init__(self, graph_repr):
        self.vertList = graph_repr


    def bfs(self, start):
        # set the list for path
        traveled_list = []
        visit_list = []
        visit_list.append(start)
        # set the Queue for travel
        x = Queue()
        x.enqueue(start)
        # when still queue
        while x:
            # get the node from top of queue
            node = x.dequeue()
            # see whether node have been visited
            if node not in traveled_list:
                # append the node and get next node
                traveled_list.append(node)
                next_node_data = self.vertList[node]
                next_node = []
                #get the next node in data
                for i in range(len(next_node_data)):
                    if type(i) == str:
                        next_node.append(i)
                    next_node.append(next_node_data[i][0])
                # sort the next node list
                next_node.sort()
                # append the node in queue
                for i in next_node:
                    if i not in visit_list:
                        visit_list.append(i)
                        x.enqueue(i)
        # return the result
        return visit_list

    def dfs(self, start):
        # set the list for path
        visited_list = []
        # set the Stack for travel
        y = Stack()
        y.push(start)
        # when still Stack
        while y:
            # get the node from top of Stack
            node = y.pop()
            # see whether node have been visited
            if node not in visited_list:
                # append the node and get next node
                visited_list.append(node)
                next_node_data = self.vertList[node]
                next_node = []
                #get the next node in data
                for i in range(len(next_node_data)):
                    if type(i) == str:
                        next_node.append(i)
                    next_node.append(next_node_data[i][0])
                # sort the next node list and reverse it
                next_node.sort()
                next_node.reverse()
                # append the node in Stack
                for i in next_node:
                    y.push(i)
        # return the result
        return visited_list

    def dijkstra(self,start):
        # Set the dict for path
        path = {}
        # set the distance for each node
        for i in self.vertList:
            path[i] = 99999
        path[start] = 0
        # set the visited list
        visited_list = []
        # set the queue for travel
        z = Queue()
        z.enqueue(start)
        # when still queue
        while z:
            # get the node from top of queue
            node = z.dequeue()
            # see whether node have been visited
            if node not in visited_list:
                # append the node and get next node
                visited_list.append(node)
                next_node_data = self.vertList[node]
                next_node = []
                # get the next node in data
                for i in range(len(next_node_data)):
                    next_node.append(next_node_data[i][0])
                    # if find short path, swap it
                    if path[next_node_data[i][0]] > next_node_data[i][1]+path[node]:
                        path[next_node_data[i][0]] = next_node_data[i][1]+path[node]
                        reomve_letter = next_node_data[i][0]
                        # if find the short list, reset all the path
                        if reomve_letter in visited_list:
                            visited_list.remove(reomve_letter)
                # append node in queue
                for i in next_node:
                    z.enqueue(i)
        # return the path
        return path






