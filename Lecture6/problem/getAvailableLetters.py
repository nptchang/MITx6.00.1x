def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    result = string.ascii_lowercase
    for i in lettersGuessed:
        if i in result:
            result = result[:result.find(i)] + result[result.find(i)+1:]
    return result

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
