s=input("enter s: ")
i=0
l=0
ia=0
la=0

while i+l+1 < len(s):
    while ord(s[i+l+1])>=ord(s[i+l]):
        l=l+1
        if i+l+1 >= len(s):
            break
    if l>la:
        la=l
        ia=i
    i=i+l+1
    l=0
print("Longest substring in alphabetical order is: " + s[ia:ia+la+1])
