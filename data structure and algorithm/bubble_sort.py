#LAB 14
#Due Date: 04/05/2019, 11:59PM
########################################
#                                      
# Name:
# Collaboration Statement:             
#
########################################


def bubbleSort(numList):
    '''
        Takes a list and returns 2 values
        1st returned value: a dictionary with the state of the list after each complete pass of bubble sort
        2nd retucountrned value: the sorted list

        >>> bubbleSort([9,3,5,4,1,67,78])
        ({1: [3, 5, 4, 1, 9, 67, 78], 2: [3, 4, 1, 5, 9, 67, 78], 3: [3, 1, 4, 5, 9, 67, 78], 4: [1, 3, 4, 5, 9, 67, 78], 5: [1, 3, 4, 5, 9, 67, 78]}, [1, 3, 4, 5, 9, 67, 78])
    '''
    # Your code starts here
    # set empty dictionary and count
    trans_hist = {}
    count = 0
    # set the for loop for first travel
    for i in range(len(numList)-1, 0,-1):
        # set the count1
        count_1 = 0
        # set the for loop for second travel
        for j in range(i):
            # set whether order is right
            if numList[j] > numList[j+1]:
                # swap the item and count it
                count_1 += 1
                numList[j], numList[j+1] = numList[j+1], numList[j]
        # if have swaped and add to dict
        if count_1!= 0:
            count += 1
            trans_hist[count] = list(numList)
        # else add to dict and break
        else:
            count += 1
            trans_hist[count] = list(numList)
            break
    # return the value
    return (trans_hist, numList)

