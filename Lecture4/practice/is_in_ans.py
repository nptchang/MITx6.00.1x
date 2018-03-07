def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    if len(aStr)==0:
        return False
    elif len(aStr)==1:
        return char==aStr

    else:
        if char>aStr[len(aStr)//2]:
            return isIn(char, aStr[len(aStr)//2):])
        elif char<aStr[len(aStr)//2]:
            return isIn(char, aStr[:len(aStr)//2)])
        elif char==aStr[len(aStr)//2]:
            return True

char = input("enter char: ")
aStr = input("enter aStr: ")
print (isIn(char, aStr))
