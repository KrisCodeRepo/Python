import re
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    #print(line.rstrip())
    for word in line.rstrip().split():
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)


x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+', x)
print(y)