def biggest_2(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    if aDict == {}:
        return None
    else:
        numList = []
        for i in aDict:
            numList.append(len(aDict[i]))
        numBiggest = max(numList)
        for j in aDict.keys():
            if len(aDict[j]) == numBiggest:
                return j

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result



animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

# print (biggest(animals))
print (biggest_2({'a': [], 'b': [1, 7, 5, 4, 3, 18, 10, 0]}))
