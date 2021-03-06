'''
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

result = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith('From') and not line.startswith('From:'):
    	words = line.split()
        email = words[1]
    	result[email] = result.get(email, 0) + 1
        

bigemail = None
bigvalue = None
for key,value in result.items():
    if bigemail is None or value > bigvalue:
        bigemail = key
        bigvalue = value
        
        
print(bigemail, bigvalue)


### sort by values 
'''
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items():
    tmp.append( (v, k) )

print(tmp)
tmp = sorted(tmp, reverse=true)
print(tmp)
'''



