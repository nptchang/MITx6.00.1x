s = input("s=: ")
count = 0
i = 0
for i in range(len(s)):
    if s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
        count = count +1
print("Number of vowels: " + str(count))
