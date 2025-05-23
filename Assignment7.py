# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
print(fh.read().rstrip().upper())