import urllib
import urllib.request

from bs4 import BeautifulSoup

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# counts = dict()
# for line in fhand:
#     print(line.decode().strip())
#     words = line.decode().strip()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)

url = input('Enter -')
html =  urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href',None))