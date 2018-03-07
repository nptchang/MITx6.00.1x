def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    if len(aStr)==0:
        return False
    elif len(aStr)==1:
        if char==aStr: return True
        else: return False
    else:
        if char>aStr[int(len(aStr)/2)]:
            return isIn(char, aStr[int(len(aStr)/2):])
        elif char<aStr[int(len(aStr)/2)]:
            return isIn(char, aStr[:int(len(aStr)/2)])
        elif char==aStr[int(len(aStr)/2)]:
            return True

char = input("enter char: ")
aStr = input("enter aStr: ")
print (isIn(char, aStr))
