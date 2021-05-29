#LAB X
#Due Date: 04/07/2019, 11:59PM
########################################
#                                      
# Name:
# Collaboration Statement:             
#
########################################

# use the code for max heap
class MaxHeapPriorityQueue:
    def __init__(self):
        self.heap=[]
        self.size = 0

    def __len__(self):
        # return the length by using len function
        return len(self.heap)

    def parent(self,index):
        if index == 0 or index > len(self.heap) -1:
            return None
        else:
            return (index -1) >> 1

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

    def swap(self,index_a,index_b):
        self.heap[index_a],self.heap[index_b] = self.heap[index_b],self.heap[index_a]


    def insert(self,data):
        self.heap.append(data)
        index = len(self.heap) -1
        parent = self.parent(index)
        while parent is not None and self.heap[parent] < self.heap[index]:
            self.swap(parent,index)
            index = parent
            parent = self.parent(parent)

    def deleteMax(self):
        index = 0
        remove_data = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        total_index = len(self.heap) -1
        while True:
            maxvalue_index = index
            if 2*index +1 <=  total_index and self.heap[2*index +1] > self.heap[maxvalue_index]:
                maxvalue_index = 2*index +1
            if 2*index +2 <=  total_index and self.heap[2*index +2] > self.heap[maxvalue_index]:
                maxvalue_index = 2*index +2
            if maxvalue_index == index:
                break
            self.swap(index,maxvalue_index)
            index = maxvalue_index
        return remove_data



def heapSort(numList):
    '''
       >>> heapSort([9,7,4,1,2,4,8,7,0,-1])
       [-1, 0, 1, 2, 4, 4, 7, 7, 8, 9]
    '''
    # set the max heap
    sort_heap = MaxHeapPriorityQueue()
    #write your code here
    # set the empty list
    sorted_list = []
    # insert the value in max heap
    for i in numList:
        sort_heap.insert(i)
    # pop the value from max heap and append it to list
    for i in  range(len(numList)):
        y = sort_heap.deleteMax()
        sorted_list.append(y)
    # reverse the list
    sorted_list.reverse()
    # return the value
    return sorted_list
