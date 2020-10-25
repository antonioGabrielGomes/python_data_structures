fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):continue
    words = line.split()
    print(words[2])


# 
words = line.split()
email = words[1]
pieces = email.split('@')

at = pieces[0]
host = pieces[1]



fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    if line.startswith('From'):
     email = line.split()
     print(email[1])
     count = count + 1

print("There were", count, "lines in the file with From as the first word")

