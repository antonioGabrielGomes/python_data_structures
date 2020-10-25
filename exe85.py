fname = "py4.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    if line.startswith('From') and not line.startswith('From:'):
     email = line.split()
     count += 1
     print(email[1])
	  

print("There were", count, "lines in the file with From as the first word")
