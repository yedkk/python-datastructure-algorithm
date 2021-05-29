#Lab #12
#Due Date: 03/22/2019, 11:59PM
########################################
#                                      
# Name:
# Collaboration Statement:             
#  
########################################



class MaxHeapPriorityQueue:
    '''
        >>> h = MaxHeapPriorityQueue()
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h.heap
        [10, 5]
        >>> h.insert(14)
        >>> h.heap
        [14, 5, 10]
        >>> h.insert(9)
        >>> h.heap
        [14, 9, 10, 5]
        >>> h.insert(2)
        >>> h.heap
        [14, 9, 10, 5, 2]
        >>> h.insert(11)
        >>> h.heap
        [14, 9, 11, 5, 2, 10]
        >>> h.insert(6)
        >>> h.heap
        [14, 9, 11, 5, 2, 10, 6]
        >>> h.parent(2)
        14
        >>> h.leftChild(1)
        9
        >>> h.rightChild(1)
        11
        >>> h.deleteMax()
        14
        >>> h.heap
        [11, 9, 10, 5, 2, 6]
        >>> h.deleteMax()
        11
        >>> h.heap
        [10, 9, 6, 5, 2]
    '''

    def __init__(self):
        self.heap=[]
        self.size = 0

    def __len__(self):
        # return the length by using len function
        return len(self.heap)


    def parent(self,index):
        # set the requirement of the index
        if index <= 1 or index > self.size:
            return None
        else:
            # else return the index of the parent
            return self.heap[(index//2)-1]

    def leftChild(self,index):
        # set the requirement of the index
        if index >= 1 and len(self.heap)+1 > 2*index:
            # else return the index of the left child
            return self.heap[(2*index)-1]
        return None

    def rightChild(self,index):
        # set the requirement of the index
        if index >= 1 and len(self.heap)+1 > (2*index)+1:
            # else return the index of the left child
            return self.heap[2*index]
        return None

    def swap(self, index1, index2):
        self.heap[index1-1], self.heap[index2-1] = self.heap[index2-1], self.heap[index1-1]
        

    def insert(self,x):
        # see whether the heap is empty
        if not len(self.heap) == 0:
            # append the value
            self.heap.append(x)
            self.size += 1
            # set the while loop and see whether the value greater than parent
            while self.heap.index(x) > 0 and self.parent(self.heap.index(x)+1) and x > self.parent(self.heap.index(x)+1):
                # swap these two
                self.swap(self.heap.index(x)+1,self.heap.index(self.parent(self.heap.index(x)+1))+1)
        else:
            # if it is empty, just append it
            self.heap.append(x)
            self.size += 1

    def deleteMax(self):
        if self.size<=0:
            return None
        elif self.size==1:
            self.size=0
            return self.heap[0]
        else:
            # swap the first and the last value and set the variables
            self.swap(1,self.__len__())
            max_heap = self.heap[self.__len__()-1]
            self.heap.pop()
            top = self.heap[0]
            # set the while loop, if the node don't have child then exit
            while self.rightChild(self.heap.index(top)+1) or self.leftChild(self.heap.index(top)+1):
                # if the node have left and right child find the large child, then swap these
                if self.leftChild(self.heap.index(top)+1) and self.rightChild(self.heap.index(top)+1):
                    large_one = max(self.leftChild(self.heap.index(top)+1), self.rightChild(self.heap.index(top)+1))
                    if large_one > top:
                        self.swap(self.heap.index(top)+1, self.heap.index(large_one)+1)
                    else:
                        break
                # if only have left child node and it's large than node, then swap these
                elif self.leftChild(self.heap.index(top)+1) > top:
                    left = self.leftChild(self.heap.index(top)+1)
                    self.swap(self.heap.index(top)+1, self.heap.index(left)+1)
                # if only have right child node and it's large than node, then swap these
                elif self.rightChild(self.heap.index(top)+1) > top:
                    right = self.rightChild(self.heap.index(top)+1)
                    self.swap(self.heap.index(top)+1, self.heap.index(right)+1)
            # return the max heap value
            return max_heap








