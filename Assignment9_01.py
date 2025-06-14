# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        #print(words[1])
        email = words[1]        
        counts[email] = counts.get(email,0)+1
bigCount  = None
bigword = None

for word, count in counts.items():
    if bigCount is None or count > bigCount:
        bigword = word
        bigCount = count
print(bigword, bigCount)
