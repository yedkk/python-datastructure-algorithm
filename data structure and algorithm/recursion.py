#Lab #7
#Due Date: 02/22/2019, 11:59PM
########################################
#                                      
# Name:
# Collaboration Statement:             
#
########################################



#### DO NOT modify the triangle(n) function in any way! 
def triangle(n):
    return recursive_triangle(n, n)

###################

def recursive_triangle(k, n):
    '''
        >>> recursive_triangle(2,4)
        '  **\\n   *'
        >>> print(recursive_triangle(2,4))
          **
           *
        >>> triangle(4)
        '****\\n ***\\n  **\\n   *'
        >>> print(triangle(4))
        ****
         ***
          **
           *
    '''

# set the string
    line_end = "\n"

    if k > n:
        return "error"
# if the k bigger than 1 no print
    elif k > 1:

# print the output
        output = (n-k)*" "+ k*"*"+line_end

# call the function and plus the output
        return output + recursive_triangle(k-1,n)

# print the last line
    else:
        return (n-k)*" "+"*"

def isPrime(n, c = 2):

    '''
        >>> isPrime(5)
        True
        >>> isPrime(1)
        False
        >>> isPrime(9)
        False
        >>> isPrime(85)
        False
        >>> isPrime(1019)
        True
    '''
    # --- Your code starts here

# if the n less than 1, return false
    if n <= 1:
        return False

# if the c is bigger enough, return True
    elif c > (n // 2):
        return True

# if the n can divide by c, return false
    elif n % c == 0:
        return False

# call the function  and c plus 1
    else:
        return isPrime(n, c + 1)
