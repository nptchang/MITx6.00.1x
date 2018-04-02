def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    NewL = []
    for i in L:
        i.reverse()
        NewL.append(i)
    NewL.reverse()
    L[:]=NewL # change L globally
    return NewL

L = [[0, 1, 2], [1, 2, 3]]
deep_reverse(L)
print(L)
