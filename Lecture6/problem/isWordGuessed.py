def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if lettersGuessed == []:
        return False
    for i in range(len(secretWord)):
        guessed = False
        for j in lettersGuessed:
            if secretWord[i] == j:
                guessed = True
        if guessed == False:
            return False
    return True









secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(isWordGuessed(secretWord, lettersGuessed))
if isWordGuessed(secretWord, lettersGuessed):
    print ("yes")
else:
    print ("no")
