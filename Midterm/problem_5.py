def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    return a *list* of keys with the value "target"
    '''
    ListAns = []
    for i in aDict:
        if aDict[i] == target:
            ListAns.append(i)
    ListAns.sort()
    return ListAns

tel = {1:1, 2:2, 6:3, 4:3, 5:4, 3:3}
print(keysWithValue(tel, 3))

