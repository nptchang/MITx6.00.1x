s = input("enter s: ")

ansHead = 0
lmax = 1
curHead = 0
curLength = 1

i = 1
for i in range(len(s)):
    if s[i]>=s[i-1]:
        curLength = curLength+1
        if curLength>lmax:
            ansHead = curHead
            lmax = curLength
    elif s[i]<s[i-1]:
        curHead=i
        curLength=1

print("String s: " + str(s))
print("Longest substring: " + str(s[ansHead:ansHead+lmax]))
