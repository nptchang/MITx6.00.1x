def count7(N):
    '''
    N: a non-negative integer
    '''
    if len(str(N)) == 1:
        if N == 7:
            return 1
        else:
            return 0
    elif N % 10 == 7:
        return count7(N//10) + 1
    else:
        return count7(N//10)


print(count7(int(input("enter an interger: "))))
