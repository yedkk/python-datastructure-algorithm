#LAB 15
#Due Date: 04/05/2019, 11:59PM
########################################
#                                
# Name:
# Collaboration Statement:             
#
########################################

def merge(list1, list2):
    '''
        >>> merge([12,26,35,87],[7,9,28])
        [7, 9, 12, 26, 28, 35, 87]
        >>> merge([12,35],[26,87])
        [12, 26, 35, 87]
    '''
    #write your code here
    # set the i and x for variable and empty list
    i = 0
    x = 0
    result = []
    # set the while loop
    while i < len(list1) and x < len(list2):
        # compare the item in different list, find the large one and append it and move the pointer
        if list1[i] <= list2[x]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[x])
            x += 1
    # append the last several items
    result += list1[i:]
    result += list2[x:]
    # return the value
    return result



def mergeSort(numList):
    '''
       >>> mergeSort([12,35,87,26,9,28,7])
       [7, 9, 12, 26, 28, 35, 87]
    '''
    #write your code here
    # if the num list is too short return error
    if len(numList)<=1:
        if len(numList) == 0:
            return "error"
        return numList
    # spilt the num list into two list
    mid = len(numList)//2
    left = mergeSort(numList[mid:])
    right = mergeSort(numList[:mid])
    # call the merge function
    return merge(left,right)

