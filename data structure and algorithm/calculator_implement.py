# HW 3
# Due Date: 02/01/2019, 11:59PM
########################################
#
# Name: Kangdong Yuan
# Collaboration Statement:
#
########################################


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

    def length(self):
        return self.stack.__len__()


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
            if(len(txt[0:pos])==0 or txt[0:pos].replace('(',' ').isspace()):
                continue;
            else:
                return pos;

#if cannot search, return -1
    return -1


def isNumber(txt):
# use for loop to search

    # --- YOU CODE STARTS HERE

# try the float if correct return else return false
    try:
        float(txt)
        return True
    except :
        return False



def getNextNumber(expr, pos):
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
    mystr=expr[pos:lastPos].replace('(',' ').replace(')',' ')
    #print(isNumber(mystr),mystr)
    if isNumber(mystr):
        number = float(mystr)

    else:
        number = None
    if found:
        return (number, expr[lastPos], lastPos)
    else:
        return (number,None,None)

def postfix(expr):
# set the dictionary
    dic={
        '+':0,'-':0,
        '*':1,'/':1,
        '^':2,'(':-1
    }
# set the stack, position, and the list
    s=Stack()
    pos=-1
    postStr=[]

# set the while loop for express binary tree
    while True:
        #print(postStr)
        begin=pos+1
        result=getNextNumber(expr,begin)
        number,opr,pos=result
        #print(result)
        if(number==None):
            return 'error, invalid expression'
        postStr.append(str(number))

#travel and get the express tree
        for item in expr[begin:pos]:
            if(item=='('):
                s.push(item)
            if(item==')'):
                if(s.is_empty()):
                    return 'error, invalid expression'
                ok=False
                while(not s.is_empty()):
                    if(s.top()=='('):
                        ok=True
                        s.pop()
                        break
                    else:
                        postStr.append(s.top())
                        s.pop()
                if not ok:
                    return 'error, invalid expression'

# return the tree from an right order
        if (opr == None):
            while (not s.is_empty()):
                if (s.top() == '('):
                    return 'error, invalid expression'
                postStr.append(s.top())
                s.pop()
            return ' '.join(postStr)

# push the other things
        while(not s.is_empty() and s.top()!='(' and dic[s.top()]>=dic[opr] ):
            postStr.append(s.top())
            s.pop()
        s.push(opr)

def calculator(expr):
    """
     >>> calculator('3*(10 - 2*3)')
     12.0
     >>> calculator(' -2 / (-4) * (3 - 2*( 4- 2^3)) + 3')
     8.5
     >>> calculator('2*(4+2*(5-3^2)+1)+4')
     -2.0
     >>> calculator('2 + 3 * ( -2 +(-3) *(5^2 - 2*3^(-2) ) *(-4) ) * ( 2 /8 + 2*( 3 - 1/ 3) ) - 2/ 3^2')
     4948.611111111111
     >>> calculator('(-2)*10 - 3*(2 - 3*2)) ')
     'error, invalid expression'
     >>> calculator('(-2)*10 - 3*/(2 - 3*2) ')
     'error, invalid expression'
     """

# use the lambda method to get the result
    ops = {"+": lambda x,y:x+y, "-": lambda x,y:x-y,'*':lambda x,y:x*y,'/':lambda x,y:x/y,'^':lambda x,y:x**y }
    poststr=postfix(expr)

# if the pos is not valid then return error
    if poststr=='error, invalid expression':
        return 'error, invalid expression'
    poststrls=poststr.split(' ')
    #print(poststrls)

# use the stack to get the output in order
    s = Stack()
    for item in poststrls:
        if isNumber(item):
            s.push(float(item))
        else:
            if s.length()<2:
                return 'error, invalid expression'
            n1=s.top()
            s.pop()
            n2=s.top()
            s.pop()
            if item=='/' and n1==0.0:
                    return 'error, invalid expression'
            s.push(ops[item](n2,n1))
        #print(s.top())
    return s.top()




if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
    #print(calculator('(-2)*10 - 3*/(2 - 3*2) '))












