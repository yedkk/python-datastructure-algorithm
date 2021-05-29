# HW 3
# Due Date: 02/01/2019, 11:59PM
########################################
#                                      
# Name: Kangdong Yuan
# Collaboration Statement:             
#
########################################

def findNextOpr(txt):
    """
        >>> findNextOpr('  3*   4 - 5')
        3
        >>> findNextOpr('8   4 - 5')
        6
        >>> findNextOpr('89 4 5')
        -1
    """

# decide whether the data type is correct
    if not isinstance(txt, str) or len(txt) <= 0:
        return "error: findNextOpr"

# use for loop to search
    for pos in range(0, txt.__len__()):

# if find, return pos
        if txt[pos] == '*' or txt[pos] == '/' or txt[pos] == '+' or txt[pos] == '^':
            return pos

# search next
        if txt[pos] == '-':
            for item in txt[pos - 1::-1]:
                if item != ' ':
                    if item.isdigit():
                        return pos
                    else:
                        break

#if cannot search, return -1
    return -1


def isNumber(txt):
    """
        >>> isNumber('1   2 3')
        False
        >>> isNumber('-  156.3')
        False
        >>> isNumber('     29.99999999    ')
        True
        >>> isNumber('    5.9999x ')
        False
    """

# use for loop to search
    if not isinstance(txt, str) or len(txt) == 0:
        return "error: isNumber"
    # --- YOU CODE STARTS HERE

# try the float if correct return else return false
    try:
        float(txt)
        return True
    except ValueError:
        pass
    return False


def getNextNumber(expr, pos):
    """
        >>> getNextNumber('8  +    5    -2',0)
        (8.0, '+', 3)
        >>> getNextNumber('8  +    5    -2',4)
        (5.0, '-', 13)
        >>> getNextNumber('4.5 + 3.15         /  -5',20)
        (-5.0, None, None)
        >>> getNextNumber('4.5 + 3.15         /   5',10)
        (None, '/', 19)
    """
# decide whether the data type is correct
    if not isinstance(expr, str) or not isinstance(pos, int) or len(expr) == 0 or pos < 0 or pos >= len(expr):
        return None, None, "error: getNextNumber"

# if no operations return false else return True
# return the position
    if (findNextOpr(expr[pos:]) == -1):
        found = False
        lastPos = expr.__len__()
    else:
        found = True
        lastPos = findNextOpr(expr[pos:])+pos

# if isnumber is correct return float number, else return none
    if isNumber(expr[pos:lastPos]):
        number = float(expr[pos:lastPos])
    else:
        number = None
    if found:
        return (number, expr[lastPos], lastPos)
    else:
        return (number,None,None)


