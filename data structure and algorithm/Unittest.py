# import the string method for future use
import string

#Lab #4
#Due Date: 02/01/2019, 11:59PM
########################################
#                                      
# Name: Kangdong Yuan
# Collaboration Statement:             
#
########################################

# define the function
def encrypt(message, key):
    """
        >>> encrypt("Hello world",12)
        'Tqxxa iadxp'
        >>> encrypt("We are Penn State!!!",6)
        'Ck gxk Vktt Yzgzk!!!'
        >>> encrypt("We are Penn State!!!",5)
        'Bj fwj Ujss Xyfyj!!!'
        >>> encrypt(5.6,3)
        'error'
        >>> encrypt('Hello',3.5)
        'error'
        >>> encrypt(5.6,3.15)
        'error'
    """
    # --- YOU CODE STARTS HERE

# decide whether it is the right data type
    if type(message) == str and type(key) == int:

# define a list that have the ascii number of character
        words = string.ascii_letters

# use the for loop to transfer characters with keys
        lowerchr = [chr((i - 97) % 26 + 97) for i in range(97 + key, 123 + key)]
        capchr = [chr((i - 65) % 26 + 65) for i in range(65 + key, 91 + key)]

# join the lower and upper characters together
        asc = ''.join(lowerchr) + ''.join(capchr)

# use the translate and maketrans function to transfer the ascii code to string
        return message.translate(str.maketrans(words, asc))

# if the value type is not correct return "error"
    return "error"


def decrypt(message, key):
    """
        >>> decrypt("Tqxxa iadxp",12)
        'Hello world'
        >>> decrypt("Ck gxk Vktt Yzgzk!!!",6)
        'We are Penn State!!!'
        >>> decrypt("Bj fwj Ujss Xyfyj!!!",5)
        'We are Penn State!!!'
        >>> decrypt(5.6,3)
        'error'
        >>> decrypt('Hello',3.5)
        'error'
        >>> decrypt(5.6,3.15)
        'error'
    """
    # --- YOU CODE STARTS HERE

# decide whether it is the right data type
    if type(message) == str and type(key) == int:

# define a list that have the ascii number of character
        words = string.ascii_letters

# use the for loop to transfer characters with keys
        lowerchr = [chr((i - 97) % 26 + 97) for i in range(97 + key, 123 + key)]
        capchar = [chr((i - 65) % 26 + 65) for i in range(65 + key, 91 + key)]

# join the lower and upper characters together
        asc = ''.join(lowerchr) + ''.join(capchar)

# use the translate and maketrans function to transfer the ascii code to string
        return message.translate(str.maketrans(asc, words))

# if the value type is not correct return "error"
    return "error"


