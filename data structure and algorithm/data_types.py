#Lab #3
#Due Date: 01/25/2019, 11:59PM
########################################
#                                      
# Name:kangdong Yuan
# Collaboration Statement:             
#
########################################

# use the function in lab2 to remove the Punctuation
def removePunctuation(txt):
    if type(txt) == str:
        punc = [".",  "$",  ".",  ",",  "(",  ")",  "?",  "!", ";"]
        new = " "
        for i in txt:
            if i not in punc:
                new += i
            else:
                new = new + " "
        new = new.strip()
        return new
    return 'error'

# define a function to find the number in str
def removenum(num):

# try to int the number
    try:
        a = int(num)
        return False

# if it is not an number return true and go to next
    except:
        return True

def countWords(txt):
    """
        >>> article1='''
        ... He will be the president of the company; right now
        ... he's a vice president.
        ... But he ..... himself,  is no sure of it...
        ... (Later he will see the importance of these 3.)
        ... '''
        >>> expected={'he': 3,"he's": 1, 'will': 2, 'be': 1, 'the': 3, 'president': 2, 'of': 3, 'company': 1, 'right': 1, 'now': 1, 'is': 1, 'a': 1, 'vice': 1, 'but': 1, 'himself': 1, 'no': 1, 'sure': 1, 'it': 1, 'later': 1, 'see': 1, 'importance': 1, 'these': 1}
        >>> countWords(article1)==expected
        True
        >>> countWords(55)
        'error'
        >>> countWords([3.5,6])
        'error'

    """
    # --- YOU CODE STARTS HERE

# decide the data type of txt
    if type(txt) == str:

# remove the Punctuation
        txt = removePunctuation(txt)

# try to lower all string
        txt = txt.lower()

# create a dictionary
        counts = dict()

# write the txt in dictionary
        words = txt.split()

# search all the dictionary to see whether words appear more than once
        for word in words:

# if the words is number reomove it
            if removenum(word):
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1

# return the dictionary
        return counts

# if the data type if wrong return error to user
    return "error"


def studentGrades(gradeList):
    """
        >>> grades = [
        ...     ['Student', 'Quiz 1', 'Quiz 2', 'Quiz 3'],
        ...     ['John', 100, 90, 80],
        ...     ['McVay', 88, 99, 111],
        ...     ['Rita', 45, 56, 67],
        ...     ['Ketan', 59, 61, 67],
        ...     ['Saranya', 73, 79, 83],
        ...     ['Min', 89, 97, 101]]
        >>> studentGrades(grades)
        [90, 99, 56, 62, 78, 95]
        >>> grades = [
        ...     ['Student', 'Quiz 1', 'Quiz 2'],
        ...     ['John', 100, 90],
        ...     ['McVay', 88, 99],
        ...     ['Min', 89, 97]]
        >>> studentGrades(grades)
        [95, 93, 93]
        >>> studentGrades(55)
        'error'
    """
    # --- YOU CODE STARTS HERE

# decide whether the data type is right
    if type(gradeList) == list:

# create the list for average grade
        ave_grade = []

# see all the data
        for x in range(1,len(gradeList)):

# set the first value for variables
            total_grade = 0
            ave = 0
            for y in range(1,len(gradeList[x])):

# count the total grade
                total_grade = total_grade + gradeList[x][y]

# count the average grade
            ave = int(total_grade /(len(gradeList[x])-1))
            ave_grade.append(ave)

# return the average grade in list
        return ave_grade

# if the data type is wrong, return error
    return "error"

