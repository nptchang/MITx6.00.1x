def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ""
    for i in range(len(secretWord)):
        str = "_ "
        for j in lettersGuessed:
            if secretWord[i] == j:
                str = j
                break
        result = result + str
    return result




secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print (getGuessedWord(secretWord, lettersGuessed))
