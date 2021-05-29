# HW 3
# Due Date: 02/01/2019, 11:59PM
########################################
#
# Name: Kangdong Yuan
# Collaboration Statement:
#
########################################

# write the stack class for use
class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):  #
        if self.stack:
            self.stack.pop()
        else:
            raise LookupError("stack is empty")

    def is_empty(self):
        return not bool(self.stack)

    def top(self):
        return self.stack[-1]
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
            if(len(txt[0:pos])==0 or txt[0:pos].isspace()):
                continue;
            else:
                return pos;

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

def postfix(expr):
    """
    >>> postfix('2^4')
    '2.0 4.0 ^'
    >>> postfix('2')
    '2.0'
    >>> postfix('2 *       5        +       3      ^ 2+1+4')
    '2.0 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
    >>> postfix('-2 *    5   +   3    ^ 2+1  +     4')
    '-2.0 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
    >>> postfix('     2 *    5   +   3    ^ -2+1  +4    ')
    '2.0 5.0 * 3.0 -2.0 ^ + 1.0 + 4.0 +'
    >>> postfix('2 *  +  5   +   3    ^ -2       +1  +4')
    'error, invalid expression'
    >>> postfix('2    5')
    'error, invalid expression'
    >>> postfix('25 +')
    'error, invalid expression'

    """
# set the dictionary
    dic={
        '+':0,'-':0,
        '*':1,'/':1,
        '^':2
    }
# set the stack, position, and the list
    s=Stack()
    pos=-1
    postStr=[]

# set the while loop for express binary tree
    while True:
        result=getNextNumber(expr,pos+1)
        number,opr,pos=result
        if(number==None):
            return 'error, invalid expression'
        postStr.append(str(number))
        if(opr==None):
            while(not s.is_empty()):
                postStr.append(s.top())
                s.pop()
            return ' '.join(postStr)

        while(not s.is_empty() and dic[s.top()]>=dic[opr]):
            postStr.append(s.top())
            s.pop()
        s.push(opr)

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)









