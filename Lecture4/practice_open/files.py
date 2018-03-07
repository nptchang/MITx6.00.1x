path = "/Users/nptchang/workspace/MITx 6.00.1x/Lecture4/practice_open/days.txt"
days_file = open(path,"r")
days = days_file.read() #define days from files
days_file.close()

title = "Days of the Week\n" #define title

new_path = "/Users/nptchang/workspace/MITx 6.00.1x/Lecture4/practice_open/new_days.txt"
new_days = open(new_path,"w")

print ("writing " + title + "...")
new_days.write(title)

print ("writing " + days + "...")
new_days.write(days)

new_days.close()
